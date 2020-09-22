# @Author  : lizhao
# @Time    : 2020/9/15 20:44
# @Function:
odd_numbers = list(range(1,21,2))
print(odd_numbers)
#4-7 3的倍数
tribles = []
for number in range(1,11):
    trible = number*3
    tribles.append(trible)
print(tribles)
#4-8 立方
cubes = []
for cube in range(1,11):
    cube = cube**3
    cubes.append(cube)
print(cubes)
#4-9 立方解析 列表解析
cubes = [cube**3 for cube in range(1,11)]
print(cubes)

