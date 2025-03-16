import view
from utill import http_client, bean, user_data_manager
import threading
from queue import Queue
import time
from enum import Enum
import threading
import concurrent.futures
import asyncio
from .scheduler_model import event_manager
from log.log_to_window import add_log

__msg_queue: Queue = None
user: bean.User = None
login_window = None
main_window = None
all_act_num = 0
getted_act_num = 0
scheduler: event_manager = None
config = None
base_url = None


class set_info_type(Enum):
    init = 0
    flush = 1


def push_msg(msg):
    add_log(f"INFO app.main.push_msg {msg.command}")
    print(msg)
    __msg_queue.put(msg)


def init(q: Queue, login_view, main_view):
    global __msg_queue
    global login_window
    global main_window
    global scheduler
    add_log("INFO init")
    __msg_queue = q
    login_window = login_view
    main_window = main_view
    scheduler = event_manager()
    scheduler.start()


def exit():
    global scheduler
    global login_window
    global main_window
    try:
        scheduler.stop()
    except:
        pass
    try:
        login_window.close_window()
    except:
        pass
    try:
        main_window.close_window()
    except:
        pass


def start(
    q: Queue,
    login_view,
    main_view,
):
    global config
    global user
    global login_window
    global main_window
    add_log("INFO start")
    init(q, login_view, main_view)
    load_config()

    if config.login_method == bean.login_method.use_this_token:
        add_log(f"INFO 使用token {user.token}")
        main_window.show_window()
        push_msg(bean.Message(bean.commands.get_activity_list, user=user))
    elif config.login_method == bean.login_method.auto_login:
        auto_login()
    else:
        init_login_window()
        login_window.show_window()
    main()


def back_to_login():
    global login_window
    global main_window
    add_log("INFO 返回登录界面")
    login_window.set_status_bar("")
    login_window.show_window()
    main_window.hide_window()


def auto_login():
    global user
    global login_window
    global main_window
    add_log(f"INFO 尝试自动登录 {user}")
    if user is None or user.username == "" or user.password == "" or user.school == "":
        log = "user is None" if not user else str(user.to_dict())
        add_log(f"ERROR 自动登录失败 {log}")
        return False
    login_window.show_window()
    push_msg(bean.Message(bean.commands.login, user=user))


def msg_to_log(msg: bean.Message):
    data_log = None
    if msg.command == bean.commands.login:
        data_log = str(msg.get_data("user").to_dict())
    elif msg.command == bean.commands.get_activity_info:
        data_log = str(msg.get_data("act_id"))
    elif msg.command == bean.commands.join_activity:
        data_log = msg.get_data("act").name + " id:" + str(msg.get_data("act").id)
    elif msg.command == bean.commands.cancel_join:
        data_log = str(msg.get_data("act_id"))
    return data_log or "无数据"


def main():
    global user
    global login_window
    global main_window
    while True:
        msg: bean.Message = __msg_queue.get()
        data_log = msg_to_log(msg)
        add_log(f"INFO 处理消息 {msg.command} {data_log}")
        if msg.command == bean.commands.login:
            login(msg.get_data("user"))
        elif msg.command == bean.commands.get_activity_info:
            set_activity_info(msg.get_data("act_id"), None, set_info_type.flush)
        elif msg.command == bean.commands.get_activity_list:
            threading.Thread(target=init_act_list, name="thread_get_act_list").start()
        elif msg.command == bean.commands.join_activity:
            join_activity(msg.get_data("act"))
        elif msg.command == bean.commands.cancel_join:
            cancel_join(msg.get_data("act_id"))
        elif msg.command == bean.commands.save_config:
            save_config()
        elif msg.command == bean.commands.get_school_list:
            init_login_window()
        elif msg.command == bean.commands.back_login:
            back_to_login()
        elif msg.command == bean.commands.login_to_server:
            login_to_server(msg.get_data("base_url"))
        elif msg.command == bean.commands.join_to_server:
            add_task_to_server(msg.get_data("act"))
        elif msg.command == bean.commands.exit_app:
            exit()
            break


def init_login_window():
    global login_window

    def func():
        for i in range(5):
            login_window.set_status_bar(f"正在获取学校列表, 第{i + 1}次尝试")
            school_list = None
            try:
                school_list = http_client.get_school_list()
            except TimeoutError as e:
                login_window.set_status_bar("请求超时, 将于10秒后重试")
                add_log(f"ERROR 请求超时\n{e}")
                print(e)
                time.sleep(10)
            except Exception as e:
                login_window.set_status_bar(
                    "学校列表获取失败, 将于三秒后重试\n" + str(e)
                )
                add_log(f"ERROR 学校列表获取失败\n{e} i={i}")
                time.sleep(3)
                print(e)
            if school_list:
                login_window.set_status_bar("学校列表获取成功")
                add_log(f"INFO 学校列表获取成功共" + str(len(school_list)) + "个")
                login_window.set_school_list(school_list)
                break
            elif i == 4:
                login_window.set_status_bar(
                    "学校列表获取失败, 请检查网络连接或稍后重启"
                )
                break

    login_window.set_status_bar("正在获取学校列表")
    t = threading.Thread(target=func)
    t.daemon = True
    t.start()


def login(u: bean.User):
    global user
    global login_window
    global main_window
    user = u
    # print(user)
    error = None
    for i in range(5):
        login_window.set_status_bar(f"正在登录, 第{i + 1}次尝试")
        try:
            token = http_client.login(user)
        except Exception as e:
            login_window.set_status_bar("登录失败, 将于三秒后重试\n" + str(e))
            add_log(f"ERROR 登录失败\n{e} i={i}")
            error = e
            time.sleep(3)
        if token:
            login_window.set_status_bar(f"INFO 登录成功 token = {token}")
            break
    else:
        login_window.set_status_bar("登录失败\n" + str(error))
        add_log(f"ERROR 登录失败\n{error}")
        return
    user.set_token(token)
    main_window.show_window()
    t = threading.Thread(target=init_act_list)
    t.daemon = True
    t.start()
    login_window.hide_window()


async def set_activity_info(act_id, locker=None, type=set_info_type.init):
    global user
    global main_window
    global getted_act_num
    try:
        act = await http_client.get_activity_info(user, act_id)
    except Exception as e:
        add_log(f"ERROR 请求活动 {act_id} 信息异常\n{e}")
        main_window.set_status_bar(f"获取活动{act_id}信息异常 请重试")
        return
    add_log(f"INFO 获取活动{act_id}信息成功 活动名称:{act.name}")
    main_window.set_act(act)
    if type == set_info_type.init:
        with locker:
            getted_act_num += 1
            main_window.set_status_bar(f"已获取{getted_act_num}/{all_act_num}个活动")
    else:
        main_window.set_status_bar(f"刷新{act.name}成功")


def init_act_list():
    global main_window
    global user
    global all_act_num
    global getted_act_num
    try:
        act_list = http_client.get_activity_list(user)
    except Exception as e:
        add_log(f"ERROR 请求活动列表异常\n{e}")
        main_window.set_status_bar(f"获取活动列表异常 请重试")
        return
    all_act_num = len(act_list)
    main_window.set_status_bar(f"活动列表获取成功, 共{len(act_list)}个")
    locker = threading.Lock()
    add_log(f"INFO 获取活动{len(act_list)}个")

    async def func():
        for act in act_list:
            await set_activity_info(act, locker)

    asyncio.run(func())

    all_act_num = 0
    getted_act_num = 0


def join_activity(act: bean.Activity):
    global user
    global scheduler
    global main_window
    add_log(f"INFO 报名活动 {act.name} id:{act.id}")
    scheduler.add_task(act.id, act.join_start_time, join_activity_single, act)


def cancel_join(act_id):
    global scheduler
    add_log(f"INFO 取消报名活动 {act_id}")
    try:
        scheduler.remove_task(act_id)
    except Exception as e:
        print(e)


def join_activity_single(act: bean.Activity):
    global user
    global main_window

    def unit(user, act):
        if act.has_join:
            return True
        i = 0
        while i < 15 and not act.has_join:
            try:
                msg = http_client.signup(act, user)
                assert msg, "msg is None"
            except Exception as e:
                add_log(
                    f"ERROR app.main.join_activity_single.unit {act.name} id:{act.id}\n{e}"
                )
                return False

            flag = msg.get_data("code")
            message = msg.get_data("message")
            if flag == bean.sign_status_code.sign_ok:
                add_log(f"INFO {act.name} 活动报名成功 id:{act.id}\n返回信息:{message}")
                act.has_join = True
                main_window.set_act(act)
                return True
            elif flag == bean.sign_status_code.so_many_requests:
                add_log(f"INFO {act.name} 请求过多 id:{act.id}\n返回信息:{message}")
                time.sleep(0.3)
            elif flag == bean.sign_status_code.sign_fail:
                act.has_join = False
                add_log(f"INFO {act.name} 报名失败 id={act.id} 返回信息:\n{message}")
                return False
            elif flag == bean.sign_status_code.unknown_response:
                add_log(
                    f"CRITICAL join_activity_single.unit {act.name}\n未知返回 id:{act.id}\n未知的返回数据:{message}"
                )
            else:
                add_log(
                    f"ERROR join_activity_single.unit {act.name}\n未知的message.status_code id:{act.id}\n:{message} {flag.__class__}"
                )
            add_log(
                f"INFO {act.name} 活动报名未成功 i={i} at {threading.current_thread().name}\n返回信息:{message}"
            )
            i += 1
            if i < 5:
                time.sleep(0.1)
            elif i < 10:
                time.sleep(0.3)
            else:
                time.sleep(0.5)

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    def thread_unit(thread_num, user, act):
        futures = [executor.submit(unit, user, act) for _ in range(thread_num)]
        for future in concurrent.futures.as_completed(futures):
            try:
                if future.result():
                    main_window.del_act_from_target_list(act.id)
                    return True
            except TimeoutError:
                add_log(
                    f"INFO join_activity_single.thread_unit {act.name} 活动某线程请求超时 id:{act.id}"
                )
            except Exception as e:
                add_log(
                    f"ERROR join_activity_single.thread_unit {act.name} 活动某线程报名异常 id:{act.id}\n{e}"
                )

        return False

    if thread_unit(5, user, act):
        return True
    else:
        add_log(f"INFO {act.name} 5线程报名失败")
    if thread_unit(5, user, act):
        return True
    else:
        add_log(f"INFO {act.name} 二次5线程报名失败")
        return False


def load_config():
    global user
    global main_window
    global login_window
    global config
    try:
        user_data_manager.load_user_data()
    except Exception as e:
        add_log(f"ERROR app.main.load_config 加载配置失败\n{e}")
    user = user_data_manager.get_user()
    config = user_data_manager.get_config()

    add_log(f"INFO 加载配置\n user:{user.to_dict()}\nconfig:{config.to_dict()}")
    login_window.load_config(user)
    main_window.load_config(config)


def save_config():
    global user
    global main_window
    global login_window
    global config
    config = bean.Config(
        login_window.get_login_method(),
        main_window.get_filt_methods(),
        main_window.get_college,
        main_window.get_grade,
        main_window.get_categories,
        main_window.get_target_act_list(),
    )
    config.categories = main_window.get_categories()
    config.grade = main_window.get_grade()
    config.college = main_window.get_college()
    add_log(f"INFO 保存配置 {user.to_dict()}\n{config.to_dict()}")
    try:
        user_data_manager.save_user_data(user, config)
    except Exception as e:
        add_log(f"ERROR 保存配置失败 {e}")


def login_to_server(baseurl: str):
    global user
    global base_url
    global main_window
    base_url = baseurl
    try:
        http_client.login_to_server(user, base_url)
    except Exception as e:
        add_log(f"ERROR app.main.login_to_server 登录到服务器失败\n{e}")
        main_window.open_message_window("登录到服务器失败", str(e))
        return False
    add_log(f"INFO 登录到服务器成功")
    main_window.open_message_window("登录到服务器成功")
    return True


def add_task_to_server(act: bean.Activity):
    global main_window
    global user
    global base_url
    try:
        http_client.add_task_to_server(user, base_url, act)
    except Exception as e:
        add_log(f"ERROR app.main.add_task_to_server 添加任务失败\n{e}")
        main_window.open_message_window("添加任务失败", str(e))
        return False
    add_log(f"INFO 添加任务成功")
    main_window.open_message_window("添加任务成功")
    return True


def get_status_from_server():
    global user
    global main_window
    global base_url
    try:
        data = http_client.get_status(user, base_url)
    except Exception as e:
        add_log(f"ERROR app.main.get_status_from_server 获取状态失败\n{e}")
        main_window.open_message_window("获取状态失败", str(e))
        return False
    add_log(f"INFO 获取状态成功")
    list = [bean.Activity.from_dict(act) for act in data]
    msg: str
    for act in list:
        act_str = f"{act.name} {act.join_start_time} {act.id}\n"
        msg += act_str
    main_window.open_message_window("获取状态成功", msg)
