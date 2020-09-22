# @Author  : lizhao
# @Time    : 2020/9/16 21:04
# @Function:序数
numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if(number==1):
        print(str(number)+"st")
    elif(number==2):
        print(str(number)+"nd")
    elif(number==3):
        print("3rd")
    else:
        print(str(number)+"th")