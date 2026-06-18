from utill import bean


def main():
    user = bean.User("test", "test")
    user.set_sid("1")
    print(user)

    dict = user.all_to_dict()
    print(dict)
    u = bean.User.from_dict(dict)
    print(u)
