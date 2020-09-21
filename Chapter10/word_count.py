def word_count(file_name):
    '''jisuanyigewenjiandazhibaohanduoshoagedanci'''
    try:
        with open(file_name,encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = 'sorry, the file'+file_name+' does not exist'
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print(num_words)
file_names = ['The Man Inside.txt', 'Alice.txt']
for filename in file_names:
    word_count("text_files\\"+filename)#zifuchuanmoweizhiyouyigexiegang
