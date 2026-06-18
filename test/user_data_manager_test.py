from utill import bean, user_data_manager
import app.main


def main():
    user_data_manager.load_user_data()
    # user = bean.User(
    #     "202311070403",
    #     "Skd@074757",
    #     school_id=208754666766336,
    #     school_name="山东科技大学",
    #     token="0461185be52011ef966200163e01086b",
    # )
    # user_data_manager.save_user_data(user)
    user = user_data_manager.get_user()
    config = user_data_manager.get_config()
    print("====================================")
    print(user.all_to_dict())
    print(config.to_dict())
    print("====================================")
    app.main.init(None, None, None)
    app.main.load_config()
    print("====================================")
    print(app.main.user.all_to_dict())
    print(app.main.config.to_dict())

    # print(config)
