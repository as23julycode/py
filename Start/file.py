def write(file_name, stuff):
    file = open(file_name, "w")
    file.write(stuff)
    file.close()
def read(file_name):
    try:
        file = open(file_name, "r")
        store = file.read()
        print(store)
        file.close()
    except:
        print("something went wrong")    
def appen(file_name , input):
    file = open(file_name, "a")
    file.write(input)
    file = open(file_name, "r")
    store = file.read()
    print(store)    
    file.close()
appen("apple.txt", "hdjshfkdjhfkjsdhk\nksdfkjsdhfkjgsdkjfgsdkjf\nsjkdfkjsdgfkdsgkfjgsd\ndskfgsdkhgfkjsdgfkjgsd")           
read("apple.txt")    
write("apple.txt", "hey how are you")    
password = "123456789"
if len(password) < 10:
    raise Exception("pasword should be more")

