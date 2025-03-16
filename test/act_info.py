{
    "code": 0,
    "message": "成功",
    # 应当在对象中保存data本身以备用
    "data": {
        "baseInfo": {
            "name": "【机电学院】“领航青春·星启未来”青年科技沙龙活动",
            "logo": "https: //img.pocketuni.net//lzlg/sys_pic/activity_xscx.png",
            "statusName": "已结束",
            "categoryName": "学术科技与创新创业",
            "credit": 1,
            "joinStartTime": "2024-12-30 14:00:00",
            "joinEndTime": "2024-12-30 19:00:00",
            "startTime": "2024-12-30 19:00:00",
            "endTime": "2024-12-30 20:30:00",
            "address": "C8二楼党员之家",
            "allowUserCount": 200,
            "joinUserCount": 129,
            "allowCollege": [
                "机械 电子工程学院",
            ],
            "signStartTime": "2024-12-30 18:00:00",
            "signOutStartTime": "2024-12-30 20:00:00",
            "allowYear": [],
            "allowTribe": [],
            "allowBranch": [],
            "signType": 1,
            "needSignOut": 1,
            "allowUserType": 1,
        },
        # userStatus中只保存hasJoin属性，为0表示未报名，为1表示已报名
        "userStatus": {
            "hasJoin": 0,
        },
    },
}


class Activity:
    def __init__(self, data, act_id):
        self.load_data(data, act_id)

    def load_data(self, data, act_id):
        base_info = data.get("baseInfo", {})
        user_status = data.get("userStatus", {})
        self.id = act_id
        self.data = data
        self.name = base_info.get("name", "")
        self.logo = base_info.get("logo", "")
        self.status_name = base_info.get("statusName", "")
        self.category_name = base_info.get("categoryName", "")
        self.credit = base_info.get("credit", 0)
        self.join_start_time = base_info.get("joinStartTime", "")
        self.join_end_time = base_info.get("joinEndTime", "")
        self.start_time = base_info.get("startTime", "")
        self.end_time = base_info.get("endTime", "")
        self.address = base_info.get("address", "")
        self.allow_user_count = base_info.get("allowUserCount", 0)
        self.join_user_count = base_info.get("joinUserCount", 0)
        self.allow_college = base_info.get("allowCollege", [])
        self.sign_start_time = base_info.get("signStartTime", "")
        self.sign_out_start_time = base_info.get("signOutStartTime", "")
        self.allow_year = base_info.get("allowYear", [])
        self.allow_tribe = base_info.get("allowTribe", [])
        self.allow_branch = base_info.get("allowBranch", [])
        self.sign_type = base_info.get("signType", 0)
        self.need_sign_out = base_info.get("needSignOut", 0)
        self.allow_user_type = base_info.get("allowUserType", 0)
        self.has_join = user_status.get("hasJoin", 0)

    def simple_info(self):
        return f"{self.name} {self.status_name} {self.category_name} {self.credit} {self.join_start_time} {self.join_end_time} {self.start_time} {self.end_time} {self.address} {self.allow_user_count} {self.join_user_count} {self.allow_college} {self.allow_year} {self.allow_tribe} {self.has_join}"

    def __str__(self):
        return f"Activity(name={self.name}, status_name={self.status_name}, category_name={self.category_name}, credit={self.credit}, join_start_time={self.join_start_time}, join_end_time={self.join_end_time}, start_time={self.start_time}, end_time={self.end_time}, address={self.address}, allow_user_count={self.allow_user_count}, join_user_count={self.join_user_count}, allow_college={self.allow_college}, allow_year={self.allow_year}, allow_tribe={self.allow_tribe}, allow_branch={self.allow_branch}, sign_type={self.sign_type}, need_sign_out={self.need_sign_out}, allow_user_type={self.allow_user_type}, has_join={self.has_join})"

    def __repr__(self):
        return f"Activity(name={self.name}, status_name={self.status_name}, category_name={self.category_name}, credit={self.credit}, join_start_time={self.join_start_time}, join_end_time={self.join_end_time}, start_time={self.start_time}, end_time={self.end_time}, address={self.address}, allow_user_count={self.allow_user_count}, join_user_count={self.join_user_count}, allow_college={self.allow_college}, sign_start_time={self.sign_start_time}, sign_out_start_time={self.sign_out_start_time}, allow_year={self.allow_year}, allow_tribe={self.allow_tribe}, allow_branch={self.allow_branch}, sign_type={self.sign_type}, need_sign_out={self.need_sign_out}, allow_user_type={self.allow_user_type}, has_join={self.has_join})"


# 示例 JSON 数据
json_data = """
{
    "code": 0,
    "message": "成功",
    "data": {
        "baseInfo": {
            "name": "【机电学院】“领航青春·星启未来”青年科技沙龙活动",
            "logo": "https: //img.pocketuni.net//lzlg/sys_pic/activity_xscx.png",
            "statusName": "已结束",
            "categoryName": "学术科技与创新创业",
            "credit": 1,
            "joinStartTime": "2024-12-30 14:00:00",
            "joinEndTime": "2024-12-30 19:00:00",
            "startTime": "2024-12-30 19:00:00",
            "endTime": "2024-12-30 20:30:00",
            "address": "C8二楼党员之家",
            "allowUserCount": 200,
            "joinUserCount": 129,
            "allowCollege": [
                "机械 电子工程学院"
            ],
            "signStartTime": "2024-12-30 18:00:00",
            "signOutStartTime": "2024-12-30 20:00:00",
            "allowYear": [],
            "allowTribe": [],
            "allowBranch": [],
            "signType": 1,
            "needSignOut": 1,
            "allowUserType": 1
        },
        "userStatus": {
            "hasJoin": 0
        }
    }
}
"""
