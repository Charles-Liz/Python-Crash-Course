# @Author  : lizhao
# @Time    : 2020/9/17 10:19
# @Function:
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
lists = ['jen','phil']
for name in favourite_languages.keys():
    if name in lists:
        print("thank you "+name)
    else:
        print("come on "+name)