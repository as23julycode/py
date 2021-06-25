stri = input("Enter the string\n")
abc = 'abcdefghijklmnopqrstuvwxyz'
trans = ''
for i in range(len(stri)):
    char = stri[i]
    for i in range(len(abc)):
        if(char[i] == char1[i]):
            char[i] = char1[i+4]
            

# lists = list(stri)
# i = len(stri) - 1
# for i in range(len(stri)):
#     trans = trans + stri[i]
#     i = i - 1
# print(lists)
# print(trans)
print(char)
print(i)