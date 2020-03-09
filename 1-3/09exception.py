def get_msg(var_name,var_type):
    value = input("请输入【%s】：" % var_name)
    if var_type == "整数":
        return int(value)
    elif var_type == "密码":
        v_len = len(value)
        if v_len < 8:
            ex = Exception("密码长度不够")
            raise ex
        else:
            return value
    else:
        return value

def recv_user():
    while True:
        try:
            username = get_msg("用户名","")
            userpwd = get_msg("密码","密码")
            userid = get_msg("自定义编号","整数")
        except:
            print("信息输入有误，需要重新输入")
        else:
            return_value = (username, userpwd ,userid)
            print("用户名：%s\n密码：%s\n自定义编号:%d" % return_value)
            return return_value
        finally:
            #print("信息登记完成")
            pass


def reg_user(usermsg):
    username,userpwd,userid = usermsg
    print(username)
    print(userpwd)
    print(userid)


def main():

   reg_user(recv_user())

if __name__ == "__main__":
    main()