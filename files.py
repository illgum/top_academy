# symbol = input('Введите символ: ')

# with open('text.txt', 'r') as file:
#     text = file.read().split()

# count = 0
# for word in text:
#     if word.startswith(str(symbol)):
#         count += 1
# print(count)


# with open('text.txt', 'r') as file:
#     text = file.read()
#     for symbol in text:
#         modified_text = text.replace('*', '&').replace('&', '*')

# with open('output.txt', 'w') as new_file:
#     new_file.writelines(text)

# # list_words = ['words', 'words', 'words', 'words', 'words', 'words']

# list_nums = [1, 1, 1, 1, 1, 1, 1]

# with open('list_words.txt', 'w') as new_file:
#     for item in list_nums:
#         new_file.write(str(item) + '\n')


# list_nums = ['zwords', 'qwords', 'hwords', 'twords', 'mwords', 'swords']
# # list_nums.sort()
# with open('list_nums.txt', 'w') as new_file:
#     for item in list_nums:
#         new_file.write(str(item) + '\n')

count = 0
with open('text.txt', 'r') as file:
    text = file.readlines()
    count = len(text)
print(count)
