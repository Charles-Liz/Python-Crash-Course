import json
file_name = 'favourite_number.json'
def new_number():
    number = eval(input("input your number:"))
    with open(file_name,'w') as file_object:
        json.dump(number,file_object)

def get_stored_number():
    try:
        with open(file_name,'r') as file_object:
            number = json.load(file_object)
    except:
        return None
    else:
        return number

if get_stored_number():
    print(get_stored_number())
else:
    new_number()
    get_stored_number()