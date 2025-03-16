import json
from enum import Enum
import datetime

# __all__ = [
#     "School",
#     "User",
#     "Activity",
#     "login_method",
#     "commands",
#     "Message",
#     "sign_status_code",
# ]


class filt_method(Enum):
    default_filt = 0
    filt_by_capacity = 1
    filt_by_has_join = 2
    filt_by_join_end_time = 3
    filt_by_category = 4
    filt_by_credit = 5
    filt_by_tribe = 6
    filt_by_join_type = 7
    filt_by_college = 8
    filt_by_grade = 9

    def to_dict(self):
        return self.value

    @staticmethod
    def from_dict(data):
        return filt_method(data)


class School:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = None if id == None else int(id)

    def __str__(self):
        return f"school_name:{self.name} school_id:{self.id}"

    def set_id(self, id: int):
        self.id = int(id)

    def get_id(self):
        return self.id

    def to_dict(self):
        return {"name": self.name, "go_id": self.id}

    @staticmethod
    def from_dict(data: dict) -> "School":
        return School(data["name"], data["go_id"])


class User:

    def __init__(
        self,
        username: str,
        password: str,
        school_id: int = 0,
        token: str = "",
        device: str = "pc",
        school_name: str = "",
    ):
        self.username = username
        self.password = password
        self.token = token
        self.device = device
        self.school = School(school_name, school_id)

    def __str__(self) -> str:
        return f"username:{self.username} password:{self.password} school_id:{self.get_sid()} token:{self.token} device:{self.device}"

    def set_sid(self, school_id: int):
        if not self.school:
            self.school = School("", school_id)
        else:
            self.school.set_id(school_id)

    def set_school(self, school: School):
        self.school = school

    def get_sid(self):
        return self.school.id

    def get_school_name(self):
        return self.school.name

    @staticmethod
    def from_dict(data: dict):
        user = User(data.get("userName", ""), data.get("password", ""))
        user.device = data.get("device", "pc")
        user.token = data.get("token", None)
        user.school = School.from_dict(data.get("school", {}))
        return user

    def to_login_dict(self):
        return {
            "userName": self.username,
            "password": self.password,
            "sid": self.school.id,
            "device": self.device,
        }

    def to_login_to_server_dict(self):
        return {
            "userName": self.username,
            "password": self.password,
            "sid": self.school.id,
            "password": "",
            "token": self.token,
        }

    def to_dict(self):
        tmp = self.to_login_dict()
        tmp["token"] = self.token
        tmp["school"] = self.school.to_dict()
        return tmp

    def set_token(self, token: str):
        self.token = token


class Activity:
    def __init__(self, data, id):
        base_info = data.get("baseInfo")
        user_status = data.get("userStatus")
        assert id is not None, f"Activity.__init__ Error: id is None, {data}"
        assert base_info, f"Activity.__init__ Error: baseInfo is None, {data}"
        assert user_status, f"Activity.__init__ Error: userStatus is None, {data}"
        self.data = data
        self.id = id
        self.name = base_info.get("name")
        self.logo = base_info.get("logo", "")
        self.status_name = base_info.get("statusName")
        self.category_name = base_info.get("categoryName")
        self.credit = base_info.get("credit")
        self.join_start_time = self.parse_datetime(base_info.get("joinStartTime"))
        self.join_end_time = self.parse_datetime(base_info.get("joinEndTime"))
        self.start_time = self.parse_datetime(base_info.get("startTime", ""))
        self.end_time = self.parse_datetime(base_info.get("endTime", ""))
        self.address = base_info.get("address", "")
        self.allow_user_count = base_info.get("allowUserCount")
        self.join_user_count = base_info.get("joinUserCount")
        self.allow_college = [
            college.get("name") for college in base_info.get("allowCollege", [])
        ]
        self.allow_year = base_info.get("allowYear", [])
        self.allow_tribe = base_info.get("allowTribe", [])
        self.allow_branch = base_info.get("allowBranch", [])
        self.need_sign_out = base_info.get("needSignOut", 0)
        self.allow_user_type = base_info.get("allowUserType", 1)
        self.has_join = user_status.get("hasJoin", 0)
        self.join_type = base_info.get("joinType", 1)

    def parse_datetime(self, date_str):
        try:
            result = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            error_str = f"Activity.parse_datetime Error in {self.name}: {date_str}, {e}"
            print(error_str)
            raise ValueError(error_str)
        return result

    def to_dict(self):
        return {"data": self.data, "id": self.id}

    def __dict__(self):
        return self.to_dict()

    @staticmethod
    def from_dict(data):
        return Activity(data["data"], data["id"])


class login_method(Enum):
    login_on_hand = 0
    auto_login = 1
    use_this_token = 2

    def to_dict(self):
        return self.value

    @staticmethod
    def from_dict(data):
        return login_method(data)


class commands(Enum):
    exit_app = -1
    join_activity = 0
    login = 1
    get_activity_list = 2
    get_activity_info = 3
    cancel_join = 4
    get_img_data = 5
    common_message = 6
    save_config = 7
    get_school_list = 8
    back_login = 9
    login_to_server = 10
    join_to_server = 11


class Message:
    def __init__(self, command: commands, **data):
        self.command = command
        self.data = data

    def get_data(self, key):
        return self.data.get(key, None)

    def to_dict(self):
        return {"command": self.command, "data": self.data}

    @staticmethod
    def from_dict(data: dict):
        return Message(data["command"], data["data"])

    def __str__(self):
        return f"command:{self.command} data:{self.data}"


class MessageCode(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    ERROR = "ERROR"


class sign_status_code(Enum):
    unknown_response = -1
    sign_ok = 0
    so_many_requests = 1
    sign_fail = 2


class Config:
    def __init__(
        self,
        login_method: login_method,
        filt_method: list[filt_method],
        college: str,
        grade: str,
        categories: list[str] = [],
        target_act_list: list[Activity] = [],
        server_url: str = "",
    ):
        self.login_method = login_method
        self.filt_method = filt_method
        self.college = college
        self.grade = grade
        self.categories = categories
        self.target_act_list = target_act_list
        self.server_url = server_url
        print(self.target_act_list)

    def to_dict(self):
        return {
            "login_method": self.login_method.to_dict(),
            "filt_method": [filt.to_dict() for filt in self.filt_method],
            "college": self.college,
            "grade": self.grade,
            "categories": self.categories,
            "target_act_list": [act.to_dict() for act in self.target_act_list],
            "server_url": self.server_url,
        }

    @staticmethod
    def from_dict(data: dict):
        return Config(
            login_method.from_dict(data["login_method"]),
            [filt_method.from_dict(filt) for filt in data["filt_method"]],
            data["college"],
            data["grade"],
            data["categories"],
            [Activity.from_dict(act) for act in data["target_act_list"]],
            server_url=data.get("server_url", ""),
        )
