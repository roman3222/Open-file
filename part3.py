import os
general_lst  = []
file_names = ('1.txt', '2.txt', '3.txt')
for file_name in file_names:
    with open(file_name, 'r', encoding='UTF-8') as file:
       text = file.read()
       general_lst.append([text.count('\n') + 1, file_name, text])
general_lst.sort()
with open('general_file.txt', 'w', encoding='utf-8') as f:
    for generals in general_lst:
       f.write(f"{generals[1]}\n  {generals[0]}\n  {generals[2]}\n")
















