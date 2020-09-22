# @Author  : lizhao
# @Time    : 2020/9/15 11:10
# @Function:
lists = ['zhao','qian','sun']
print("i want to invite "+lists[0]+lists[1]+lists[2]+" to eat dinner with me")
print("qian have no time,so i need to invite annother one")
lists[1] = "li"
for l in lists:
    print("Hi "+l+",let's eat dinner tonight")
print("i find a bigger table")
lists.insert(0,"zhou")
lists.insert(1,"wu")
lists.append("zheng")
print(lists)
print(len(lists))
p = lists.pop()
print("sorry "+p)
p = lists.pop()
print("sorry "+p)
p = lists.pop()
print("sorry "+p)
p = lists.pop()
print("sorry "+p)
del lists[0]
del lists[0]
print(lists)