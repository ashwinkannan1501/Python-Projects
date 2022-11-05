# Library Management System

# This function is meant for displaying the available books in the library
def display_books():
    print("The available books are :- ")
    for book in book_dictionary:
        print(f'{book}')
    print(book_dictionary)

# This function is meant for searching the book and borrow the book if the searched books and the no of copies in that book is available
def search_and_borrow_books():
    display_books()
    book_query = input("Enter the book you want : ")
    if book_query in book_dictionary.keys():
        if book_dictionary.get(book_query) >= 1:
            print(f"The {book_query} is available. ")
            required_copy = int(input("How many copies do you want ? : "))
            if required_copy <= book_dictionary[book_query]:
                print(f"Yes. The {required_copy} books is available. Here's your requirements")
                book_dictionary[book_query] -= required_copy
                if book_dictionary[book_query] == 0:
                    del book_dictionary[book_query]
                    
            else:
                print(f"Sorry. The amount of copy is not sufficient. We are having only {book_dictionary.get(book_query)} of {book_query}")
                limited_copies = input(f"Do you want that {book_dictionary.get(book_query)} copies ? (y/n): ").lower()[0]
                if limited_copies == 'y':
                    print("Here's your book sir.")
                    book_dictionary[book_query] -= book_dictionary[book_query]
                    if book_dictionary[book_query] == 0:
                        del book_dictionary[book_query]
                
                    
        else:
            print(f"Sorry. The {book_query} is not available.")
            book_dictionary.popitem(book_query)

# This function is meant for returning the books back to the library
def return_books():
    return_book = input("Enter the book that you want to return :- ")
    if return_book in copy_books:
        copies = int(input(f"Enter the number of copies that you return in {return_book} book : "))
        if return_book not in book_dictionary:
            book_dictionary.update({return_book : copies})
        else:
            book_dictionary[return_book] += copies
        print("Successfully the book is returned")
    else:
        print("This book is not belong to this library")
    
        
        
        
# Main Program

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
        2) Search and borrow books
        3) Return books
        4) Exit
        """
    )

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        display_books()
    elif choice == 2:
        search_and_borrow_books()
    elif choice == 3:
        return_books()
    elif choice == 4:
        print("Thank You for coming to this library. You'll have a good day. Please visit again :)")
        break
    else:
        print("Invalid Choice... Please enter the correct choice")