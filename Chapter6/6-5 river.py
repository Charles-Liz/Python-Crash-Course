# @Author  : lizhao
# @Time    : 2020/9/17 10:14
# @Function:
rivers = {
    'danube' : 'germany',
    'nile' : 'egypt',
    'the yellow river' : 'china'
}
for river,country in rivers.items():
    print("The "+river.title()+" runs through "+country.title())
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
