import datetime
file_name = 'text_files\guest_book.txt'
active = True
while active:
    name = input("input your name(Press 'q' to quit):")
    if name != 'q':
        print("Hello "+name)
        with open(file_name,'a') as file_object:
            file_object.write(name+'  visit time: '+str(datetime.datetime.now())+"\n")
    else:
        active = False