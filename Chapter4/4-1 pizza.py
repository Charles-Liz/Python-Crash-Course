# @Author  : lizhao
# @Time    : 2020/9/15 20:25
# @Function:
pizzas = ['pepperoni pizza','durian pizza','margaret pizza']
for pizza in pizzas:
    print("i like "+pizza)
print("i really love pizza")
#4-11 your pizza and my pizza
friend_pizzas = pizzas[:]
pizzas.append('new pizza')
friend_pizzas.append('new friend pizza')
print("my favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("my friend's favourite pizza are:")
for pizza in friend_pizzas:
    print(pizza)
