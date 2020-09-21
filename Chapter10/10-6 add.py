def check_number(number):
    try:
        number = float(number)
        print(number)
        return True
    except ValueError:
        return False

def add_number():
    while True:
        number1 = input("input first number:")
        if check_number(number1):
            number2 = input("input second number:")
            if check_number(number2):
                result = int(number1)+int(number2)
                print(result)
                break
            else:
                print("please input number")
                continue
        else:
            print("please input number!")
            continue
add_number()