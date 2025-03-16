import threading
import time
import schedule
from datetime import datetime
from utill.log_to_window import add_log


class event_manager:
    def __init__(self):
        self.jobs = {}
        self.running = False
        self.lock = threading.Lock()
        self.t = None
        self.scheduler = schedule.Scheduler()

    def start(self):
        self.t = threading.Thread(target=self.__start, name="event_manager")
        self.t.daemon = True
        self.t.start()

    def __start(self):
        """启动调度器"""
        self.running = True
        add_log(f"INFO 调度器已启动 {threading.current_thread().name}")
        while self.running:
            self.scheduler.run_pending()
            time.sleep(1)  # 每秒检查一次

    def stop(self):
        """停止调度器"""
        add_log(f"INFO 调度器已停止 {threading.current_thread().name}")
        self.running = False
        self.t = None

    def add_task(self, name: str, start_time: datetime, func, *args, **kwargs):
        """
        添加一个只执行一次的定时任务
        :param name: 任务名称
        :param start_time: 执行时间
        :param func: 任务函数
        """
        if name in self.jobs:
            add_log(f"INFO 任务 '{name}' 已存在 {threading.current_thread().name}")
            return
        print(start_time)
        delay = (start_time - datetime.now()).total_seconds()
        delay = max(delay, 1)

        def wrapper():
            add_log(f"INFO 执行任务 '{name}' {threading.current_thread().name}")
            func(*args, **kwargs)
            # 执行完后自动取消任务
            try:
                self.remove_task(name)
            except KeyError:
                add_log(f"ERROR 任务 '{name}' 不存在 {threading.current_thread().name}")

        with self.lock:
            job = self.scheduler.every(delay).seconds.do(wrapper)
            self.jobs[name] = job
        add_log(
            f"INFO 任务 '{name}' 已添加 {delay}sec 后执行 {threading.current_thread().name}"
        )

    def remove_task(self, name: str):
        """删除任务"""
        with self.lock:
            if name in self.jobs:
                job = self.jobs[name]
                self.scheduler.cancel_job(job)
                del self.jobs[name]
                add_log(f"INFO 任务 '{name}' 已删除 {threading.current_thread().name}")
            else:
                raise KeyError(
                    f"任务 '{name}' 不存在 at {threading.current_thread().name}"
                )


# 运行示例
# if __name__ == "__main__":
#     scheduler = AsyncScheduler()
#     scheduler.add_task(
#         "task1", datetime.fromtimestamp(time.time() + 3), my_task, "task1", age=10
#     )  # 添加任务，每 1 秒执行一次
#     scheduler.add_task(
#         "task2", datetime.fromtimestamp(time.time() + 5), my_task, "task2", age=29
#     )  # 添加任务，每 1 秒执行一次
#     scheduler.add_task(
#         "task3", datetime.fromtimestamp(time.time() + 2), my_task, "task3", age=23
#     )  # 添加任务，每 1 秒执行一次
#     scheduler.add_task(
#         "task4", datetime.fromtimestamp(time.time() + 7), my_task, "task4", age=123
#     )  # 添加任务，每 1 秒执行一次

#     try:
#         scheduler.start()
#         print("调度器已启动")
#         time.sleep(5)

#     except KeyboardInterrupt:
#         scheduler.stop()
#         print("调度器已停止")
