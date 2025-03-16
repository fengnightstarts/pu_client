from utill import http_client
from utill.bean import Activity


token = "9c1252e5daf911ef8dd700163e0102ac"
sid = 208754666766336


def main():
    school_list = http_client.get_school_list()
    act_list = http_client.get_activity_list(token, sid)
    for act_id in act_list:
        act = http_client.get_activity_info(token, sid, act_id)
        print(act.name)
        print(act.id)
