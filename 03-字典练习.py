# 写一个程序管理用于登陆系统的用户信息，登陆名字和密码。登陆用户建立后，已存在用户可以用登陆名字和密码重返系统，新用户不能用别人的
# 用户名建立用户账号

# 模拟从数据库取出来的用户名和密码

user_pass = {"loatie":"password", "huniu":"adminf"}

def create_user(username, password):
    '''
    :param username: 用户要建立账号的名称
    :param password: 用户建立账号的密码
    :return:
    '''
    # 判断是否已经存在
    username_old = user_pass.keys()

    if username in username_old:
        print("此用户名已被注册！")
    else:
        # 未被注册则更新进数据user_pass中，实际是会存进数据库
        user_pass[username]= password
        print("恭喜，注册成功！")

# 建立用户登陆的函数，创建用户的操作实际在这个后面
def login_user(username, password):
    # 判断该用户是否存在

    username_old = user_pass.keys()

    if username not in username_old:
        print("该用户不存在！")
    elif password != user_pass[username]:
        print("密码错误！")
    else:
        print("登陆成功")

login_user("loatie","password")
