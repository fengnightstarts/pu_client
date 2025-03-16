import requests
import json
import time

token = "9c1252e5daf911ef8dd700163e0102ac"
sid = 208754666766336

LOGIN = "https://apis.pocketuni.net/uc/user/login"
JOIN_ACTIVITY = "https://apis.pocketuni.net/apis/activity/join"
ACTIVITY_INFO = "https://apis.pocketuni.net/apis/activity/info"
ACTIVITY_LIST = "https://apis.pocketuni.net/apis/activity/list"
SCHOOL_LIST = "https://pocketuni.net/index.php?app=api&mod=Sitelist&act=getSchools"

ACTIVITY = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Authorization": "",
    "Origin": "https://class.pocketuni.net",
    "Connection": "keep-alive",
    "Referer": "https://class.pocketuni.net/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}
ALL_ACTIVITY = {
    "Connection": "keep-alive",
    "Content-Length": "30",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://class.pocketuni.net",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://class.pocketuni.net/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}


def get_activity_info(id):
    info_header = ACTIVITY.copy()
    info_header["Authorization"] = f"Bearer {token}" + ":" + str(sid)
    info_json = {"id": id}
    info_response = requests.post(
        url=ACTIVITY_INFO, headers=info_header, json=info_json
    )
    info_response.raise_for_status()
    info_data = info_response.json().get("data", {}).get("baseInfo", {})
    print(info_response.json())
    # act = activity.Activity(info_data,id,info_response.json().get("data", {}).get("userStatus").get("hasJoin"))


def main():
    get_activity_info(26441367453696)


if __name__ == "__main__":
    main()
