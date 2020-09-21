file_name = 'text_files\learning_python.txt'

'''读取整个文件'''
with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)

'''遍历文件对象'''
with open(file_name) as file_object:
    for line in file_object:
        print(line)

'''将各行存储到列表中'''
with open(file_name) as file_object:
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.strip())