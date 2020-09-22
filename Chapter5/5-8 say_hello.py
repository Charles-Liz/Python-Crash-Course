# @Author  : lizhao
# @Time    : 2020/9/16 20:54
# @Function:
#users = ['admin', 'zhao', 'qian', 'sun', 'li']
users=[]
if users:
    for user in users:
        if(user=='admin'):
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello "+user+",thank you for logging in again")
else:
    print("we need to find some users")