file_name = 'text_files\learning_python.txt'

with open(file_name) as file_objects:
    contents = file_objects.read()
new_contents = contents.replace('python', 'java')
print(contents)
print(new_contents)