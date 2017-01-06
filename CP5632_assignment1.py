__author__ = 'jc444921'


# Initialize the constants
# load csv
def menus():
    book_list = []
    load_book = open("books.csv")
    lines = load_book.readlines()
    for line in lines:
        line = line.strip()
        p = line.find(",")
        menu1 = line[0:p]
        line = line[(p + 1):]
        p = line.find(",")
        menu2 = line[0:p]
        line = line[(p + 1):]
        p = line.find(",")
        menu3 = line[0:p]
        menu4 = line[(p + 1):]
        menu =[menu1,menu2,menu3,menu4]
        book_list.append(menu)
    load_book.close()
    return book_list

# end of load_books()

def main():
    print("Reading List 1.0 - by Xiting Jia")
    choice = display_menu()
    book_list = menus()
    while choice != "Q":
        if choice == "R":
            list_required_book(book_list)
        elif choice == "C":
            list_completed_book(book_list)
        elif choice == "A":
            add_new_book(book_list)
        elif choice == "M":
            mark_book_completed(book_list)
        else:
            print("Please input R, C, A, M or Q")
        choice = display_menu()
    print("{} books saved to books.csv".format(len(book_list)))
    save_books(book_list)
    print("Have a nice day :)")

def display_menu():
    print("Menu")
    print("R - List required books")
    print("C - List completed books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")
    choice = input(">>>")
    choice = choice.strip().upper()
    return choice

# end of main()

def list_required_book(book_list):
    print("Required books:")
    lst = []
    pages=0
    books=0
    for i in range(0, len(book_list)):
        menu = book_list[i]
        if menu[3] == "r":
            lst.append(i)
            output = "{:d}. {} by {} {} pages".format(i, menu[0], menu[1], menu[2], menu[3])
            print(output)
            page = int(menu[2])
            pages += page
            books +=1
    print("Total pages for {} books: {}".format(books,pages))


def list_completed_book(book_list):
    print("Completed books: ")
    lst = []
    pages=0
    books=0
    for i in range(0, len(book_list)):
        menu = book_list[i]
        if menu[3] == "c":
            lst.append(i)
            output = "{:d}. {} by {} {} pages".format(i, menu[0], menu[1], menu[2], menu[3])
            print(output)
            page = int(menu[2])
            pages += page
            books +=1
    print("Total pages for {} books: {}".format(books, pages))


def add_new_book(book_list):
    menu1 = ""
    menu2 = ""
    menu3 = ""
    menu4 = 0
    while True:
        menu1 = input("Title: ")
        menu1 = menu1.strip()
        if menu1 == "":
            print("Input can not be blank")
        else:
            break
    while True:
        menu2 = input("Auther: ")
        menu2 = menu2.strip()
        if menu2 == "":
            print("Input can not be blank")
        else:
            break
    while True:
        pages = input("Pages: ")
        pages = pages.strip()
        try:
            menu3 = int(pages)
            if menu3 < 0:
                print("Number must be >= 0")
            else:
                break
        except:
            print("Invalid input; enter a valid number")

    print("{} by {}, ({} pages) added to reading list".format(menu1, menu2, menu3))
    menu =[menu1, menu2, menu3, "r"]
    book_list.append(menu)


def mark_book_completed(book_list):
    list_required_book(book_list)
    print("Enter the number of a book to mark as completed")
    try:
        num_of_book = int(input(">>>"))
        if book_list[num_of_book][3] == 'c':
            print("That book is already completed")
        else:
            book_list[num_of_book][3] = 'c'
            print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
    except ValueError:
        print("Invalid input; enter a valid number")
        complete_a_book(book_list)

def save_books(books):
    """
    This function will help the program to update data into file books.csv
"""
    books_file = open("books.csv", 'w')
    for i in books:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=books_file)
            else:
                print(j, end=',', file=books_file)
        print(file)
    books_file.close()
# end of complete_a_book()
    
main()