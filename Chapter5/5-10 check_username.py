# @Author  : lizhao
# @Time    : 2020/9/16 20:59
# @Function:
current_users = ['admin', 'zhao', 'qian', 'sun', 'li']
new_users = ['admin', 'LI', 'zhang', 'yu', 'liu']
for new_user in new_users:
    if(new_user.lower() in current_users):
        print("already used")
    else:
        print("you can use")