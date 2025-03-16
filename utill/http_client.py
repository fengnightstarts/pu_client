import requests
import json
import time
import random
from utill import headers, urls
from utill.bean import *
import datetime
import aiohttp


def login(user: User):
    user_data = user.to_login_dict()
    response = requests.post(urls.LOGIN, headers=headers.LOGIN, json=user_data)
    response.raise_for_status()
    res_json = response.json()
    token = response.json().get("data", {}).get("token")
    if token:
        # print("token = " + token)
        return token
    else:
        print("登录失败,返回信息：")
        print(response.text)
        raise Exception(f"登录失败 {response.text}")


def get_school_list() -> list[School]:
    response = requests.post(urls.SCHOOL_LIST, headers=headers.GET_SCHOOL, timeout=30)
    response.raise_for_status()
    print(response.text)
    # res_json = response.json()
    school_list_json = response.json()
    school_list = [School.from_dict(school) for school in school_list_json]
    return school_list


def get_activity_list(user: User) -> list[Activity]:
    token = user.token
    sid = user.get_sid()
    list_header = headers.ALL_ACTIVITY.copy()
    list_header["Authorization"] = f"Bearer {token}" + ":" + str(sid)
    list_json = {"sort": 1, "page": 1, "limit": 10}
    all_activity_data = []
    for i in range(1, 12):
        list_json["page"] = i
        list_response = requests.post(
            url=urls.ACTIVITY_LIST, headers=list_header, json=list_json
        )
        list_response.raise_for_status()
        res_json = list_response.json()
        list_data = list_response.json().get("data", {}).get("list", [])
        flag = True
        if not list_data:
            print("没有活动了")
            break
        for act in list_data:
            all_activity_data.append(act["id"])

    return all_activity_data


async def get_activity_info(user: User, act_id):
    token = user.token
    sid = user.get_sid()
    assert token is not None and sid is not None, f"token or sid is None"
    info_header = headers.ACTIVITY_INFO.copy()
    info_header["Authorization"] = f"Bearer {token}" + ":" + str(sid)
    info_json = {"id": act_id}

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=urls.ACTIVITY_INFO, headers=info_header, json=info_json
        ) as response:
            if response.status != 200:
                raise IOError(
                    f"请求失败, {await response.text()} token={token} sid={sid} id={act_id}\n{response.text}"
                )
            info_data = await response.json()
            act = Activity(info_data.get("data"), act_id)
            return act


def signup(act: Activity, user: User):
    if not user.token:
        raise ValueError("token is None")
    if not user.get_sid():
        raise ValueError("sid is None")
    token = user.token
    sid = user.get_sid()
    data = {"activityId": act.id}
    header = headers.JOIN_ACTIVITY.copy()
    header["Authorization"] = f"Bearer {token}" + ":" + str(sid)
    nowTime = datetime.datetime.now()
    gap = act.join_start_time - nowTime
    if gap.total_seconds() > 1:
        time.sleep(gap.total_seconds() - 1)
    if gap.total_seconds() > 0:
        nowTime = datetime.datetime.now()
        time.sleep(
            (act.joinStartTime - nowTime).total_seconds() * random.random(0.9, 1.5)
        )
    response = requests.post(url=urls.JOIN_ACTIVITY, headers=header, json=data)
    print(response.text)
    print(response.status_code)
    if response.status_code == 200:
        command = commands.common_message
        if (
            response.text
            == '{"code":0,"message":"成功","data":{"msg":"PU君提示：报名成功，请留意活动签到时间哦~"}}'
            or response.text
            == '{"code":9405,"message":"您已报名，请勿重复操作","data":{}}'
        ):
            return Message(
                command, code=sign_status_code.sign_ok, message=response.text
            )
        elif response.text == '{"code":500,"message":"请勿频繁点击","data":{}}':
            return Message(
                command.common_message,
                code=sign_status_code.so_many_requests,
                message=response.text,
            )
        elif response.text == '{"code":9405,"message":"活动已停止报名","data":{}}':
            return Message(
                command, code=sign_status_code.sign_fail, message=response.text
            )
        else:
            return Message(
                command, code=sign_status_code.unknown_response, message=response.text
            )
    else:
        raise IOError(f"请求失败, {response.text} code={response.status_code}")


def login_to_server(user: User, base_url: str):
    token = user.token
    sid = user.get_sid()
    assert token is not None and sid is not None, f"token or sid is None"
    data = user.to_login_to_server_dict()
    response = requests.post(url=base_url + "/login", json=data)
    response.raise_for_status()
    res_json = response.json()
    if res_json.get("code") == 0:
        return res_json.get("msg")
    else:
        raise Exception(f"登录失败 {response.text}")


def add_task_to_server(user: User, base_url: str, act: Activity):
    data = {
        "userName": user.username,
        "sid": user.get_sid(),
        "activity": {
            "id": str(act.id),
            "name": act.name,
            "joinStartTime": act.join_start_time,
            "joinEndTime": act.join_end_time,
        },
    }
    response = requests.post(url=base_url + "/join", json=data)
    response.raise_for_status()
    res_json = response.json()
    if res_json.get("code") == 0:
        return res_json.get("msg")
    else:
        raise Exception(f"添加失败 {response.text}")


def get_status(user: User, base_url: str):
    data = user.to_login_dict()
    response = requests.post(url=base_url + "/status", json=data)
    response.raise_for_status()
    res_json = response.json()
    return res_json.get("data")
