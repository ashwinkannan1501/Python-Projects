# Library Management System

def display_books():
    for book in book_dictionary:
        print(book)


total_books = int(input("Enter the total number of books in the library : "))
book_dictionary = {}

for index in range(total_books):
    book = input("Enter the book name : ")
    copies = int(input(f"Enter the number of copies of {book} : "))
    book_dictionary.update({book : copies})
    copy_books = book_dictionary.copy()

while True:
    print(
        """
        1) Display
        2) Search
        3) Borrow a book
        4) Return a book
        5) Exit
        """
    )

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        display_books()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        break
    else:
        print("Invalid Choice... Please enter the correct choice")


