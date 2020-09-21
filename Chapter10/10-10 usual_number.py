file_name = 'text_files\The Man Inside.txt'
with open(file_name,encoding='utf-8') as file_object:
    contents = file_object.read()
    number = contents.lower().count('the')
    print(number)