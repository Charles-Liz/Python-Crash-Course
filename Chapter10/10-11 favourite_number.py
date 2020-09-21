import json
def get_new_number():
    file_name = 'favourite_number.json'
    number = input("input your favourite number:")
    with open(file_name,'w') as file_object:
        json.dump(number,file_object)
    return number
def get_stored_number():
    file_name = 'favourite_number.json'
    try:
        with open(file_name,'r',encoding='utf-8') as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return number
def say():
    '''zhichuzuixihuandeshuzi'''
    number = get_stored_number()
    if number:
        print(number)
    else:
        number = get_new_number()
        print(number)

say()