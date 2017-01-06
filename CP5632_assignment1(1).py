__author__ = 'jc444921'

# Initialize the constants
# book_list = [("Computing Using Python", "Punch and Enbody", "792", "r"), ("The 360 Degree Leader", "John Maxwell", "369", "r")]

def main():
	print("Reading List 1.0 - by Xiting Jia")
	book_list=[]
	#load_book from the file
	load_book(book_list)
	display_menu()

	choice = input(">>> ").upper()

	while choice != "Q":
		if choice == "R":
			list_required_book(book_list)
		elif choice == "C":
			list_completed_book(book_list)
		elif choice == "A":
			add_new_book(book_list)
		elif choice == "M":
			mark_book_completed()
		else:
			print("Please input R, C, A, M or Q")
		display_menu()
		choice = input(">>> ").upper()
	print("Have a nice day :)")

# end of main()

def display_menu():
	"""
	"""
	print("Menu")
	print("R - List required books")
	print("C - List completed books")
	print("A - Add new book")
	print("M - Mark a book as completed")
	print("Q - Quit")

def load_book(book_list):
	"""
	"""
	print("4 books loaded from books.csv")

	# end of load_books()

def list_required_book():
	print("list_required_book")

def list_completed_book():
	print("list_completed_book")

def add_new_book():
	print("add_new_book")

def mark_book_completed():
	print("mark_book_completed")


def complete_a_book():
	"""
	"""
	print("complete a book")

# end of complete_a_book()
# Start the program
main()