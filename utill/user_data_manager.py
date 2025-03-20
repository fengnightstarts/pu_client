import json
from .bean import *

file_name = "user_data.json"

default_user = User("", "").to_dict()
default_config = Config(
    login_method.login_on_hand, [filt_method.default_filt], "", "", [], []
).to_dict()
config = {
    "user": default_user,
    "config": default_config,
}


def save_user_data(user: User, config: Config, file=file_name):
    try:
        f = open(file, "w", encoding="utf-8")
        data = {
            "user": user.to_dict(),
            "config": config.to_dict(),
        }
        json.dump(data, f, ensure_ascii=False)
    except Exception as e:
        raise e
    finally:
        f.close()


def load_user_data(file=file_name):
    global config
    try:
        f = open(file, "r", encoding="utf-8")
        config_data = json.load(f)
    except Exception as e:
        config_data = config
        raise e
    finally:
        config["user"] = config_data.get("user", default_user)
        config["config"] = config_data.get("config", default_config)
        f.close()


def get_user() -> User:
    global config
    return User.from_dict(config["user"])


def get_config() -> Config:
    global config
    return Config.from_dict(config["config"])


def get_target_act_list() -> list[int]:
    global config
    return Config.from_dict(config["config"]).target_act_list


def set_user(user: User):
    global config
    config["user"] = user.to_dict()


def set_config(c: Config):
    global config
    config["config"] = c.to_dict()


def set_target_act_list(target_act_list: list[Activity]):
    global config
    tmp = Config.from_dict(config["config"])
    tmp.target_act_list = target_act_list
    config["config"] = tmp.to_dict()
