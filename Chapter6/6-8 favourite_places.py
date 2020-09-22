# @Author  : lizhao
# @Time    : 2020/9/17 10:49
# @Function:
favourite_places = {
    'zhao': ['africa', 'china', 'japan'],
    'qian': ['sichuan']
}
for name,favourite_place in favourite_places.items():
    print(name+" ‘s favorite place is")
    for place in favourite_place:
        print(place)