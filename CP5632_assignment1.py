__author__ = 'jc444921'
# Initialize the constants

book_list = []
# load csv
def load_book_menus():
    load_book = open("books.csv")
    lines = load_book.readlines()
    for line in lines:
        line = line.strip().split(",")
        print(line)
        book_list.append(line)
    load_book.close()
    return book_list

# end of load_books()

def main():
    print("Reading List 1.0 - by Xiting Jia")
    book_list = load_book_menus()
    choice = display_menu()
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
# end of main()

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
# end of defined display menu

def list_required_book(book_list):
    print("Required books:")
    lst = []
    pages = 0
    books = 0
    for i in range(0, len(book_list)):
        menu = book_list[i]
        if menu[3] == "r":
            lst.append(i)
            print("{:d}. {:<44s} by {:>33s} {:>20s} pages".format(i, menu[0], menu[1], menu[2], menu[3]))
            page = int(menu[2])
            pages += page
            books += 1
    print("Total pages for {} books: {}".format(books, pages))

def list_completed_book(book_list):
    print("Completed books: ")
    lst = []
    pages = 0
    books = 0
    for i in range(0, len(book_list)):
        menu = book_list[i]
        if menu[3] == "c":
            lst.append(i)
            output = "{:d}. {:<44s} by {:>33s} {:>20s} pages".format(i, menu[0], menu[1], menu[2], menu[3])
            print(output)
            page = int(menu[2])
            pages += page
            books += 1
    print("Total pages for {} books: {}".format(books, pages))

def add_new_book(book_list):
    title = ""
    author =""
    book_pages = 0
    while True:
        title = input("Title: ")
        title = title.strip()
        if title == "":
            print("Input can not be blank")
        else:
            break
    while True:
        author = input("Auther: ")
        author = author.strip()
        if author == "":
            print("Input can not be blank")
        else:
            break
    while True:
        pages = input("Pages: ")
        pages = pages.strip()
        try:
            book_pages = int(pages)
            if book_pages <= 0:
                print("Number must be > 0")
            else:
                break
        except:
            print("Invalid input; Enter a valid number")

    print("{} by {}, ({} pages) added to reading list".format(title, author, book_pages))
    list_of_book = [title, author, str(book_pages), "r"]
    book_list.append(list_of_book)
# end of add books

def mark_book_completed(book_list):
    list_required_book(book_list)
    print("Enter the number of a book to mark as completed")
    try:
        num_of_book = int(input(">>>"))
        if book_list[num_of_book][3] == 'c':
            print("That book is already completed")
            mark_book_completed(book_list)
        else:
            book_list[num_of_book][3] = 'c'
            print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
    except ValueError:
        print("Invalid input; enter a valid number")
        mark_book_completed(book_list)
    except TypeError:
        print("Invalid type; Enter a valid number:")
        mark_book_completed(book_list)
# end of complete_a_book()

def save_books(books):
    """
    update data into books.csv
    """
    books_file = open("books.csv", 'w')
    for i in books:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=books_file)
            else:
                print(j, end=',', file=books_file)
        print(file=books_file)
    books_file.close()


main()
