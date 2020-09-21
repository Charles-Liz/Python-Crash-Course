file_name = 'text_files\programming.txt'

with open(file_name,'w') as file_object:
    file_object.write("i love python")

with open(file_name,'a') as file_object:
    file_object.write("\nthis is a new line")
