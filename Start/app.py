import myfunction
import os
myfunction.print_options()
option = input()
books = []
while option != 'X' and option != "x":
    # do stuff here
    if option == '1':
        books.append(myfunction.create_book())
    elif option == '2':
        myfunction.save_books(books)
    elif option == '3':
        books = myfunction.load_books()
    elif option == '4':
        myfunction.issue_book(books)
    elif option == '5':
        myfunction.return_book(books)
    elif option == '6':
        myfunction.update_book(books)
    elif option == '7':
        myfunction.show_all_books(books)
    elif option == '8':
        myfunction.show_book(books)
    else:
        print("the given command doesnt exist..")
    input("press enter to continue...")
    # asking for input
    os.system("cls")
    myfunction.print_options()
    option = input()
