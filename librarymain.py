
# This is the main file for the library program. It will run the main menu and call the other functions in the program.
import os
import sys

# Add the directory containing your modules to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from authorclass import Author, Author_ops
from bookclass import Book, Book_ToDos
from memberclass import Member, Member_ops




def main():
    while True:
        main_menu = input('''
Welcome to Tampa Library, Home of the Whopper!
How may I help you today:

1. Book Repository
2. Tampa Membership List
3. Author Lists
4. Back to reality
    ''')
        if main_menu == '1':
            book_repository()               # Open Book Encyclopedia function
        elif main_menu == "2":
            member_list()               # Open Member List fuction
        elif main_menu == '3':
            author_info()               # Open Author List
        elif main_menu == '4':
            print("Thank you for stopping by!")
            break
        else:
            print("Please enter a valid selection.")
            continue

book_todos = Book_ToDos()
def book_repository():
    while True:
        book_menu = input('''
Welcome to the Book Repository! what would you like to do?

1. Add a new book
2. Rent a book
3. Return a book
4. Search the Repository 
5. Display the Repository
6. Back to main menu
    ''')
        if book_menu == '1':
            book_todos.add_book()
        elif book_menu == '2':
            book_todos.rent_book()
        elif book_menu == '3': 
            book_todos.return_book()
        elif book_menu == '4':
            book_todos.book_search()
        elif book_menu == '5':
            book_todos.display_books()
        elif book_menu == '6':
            return main()
        else:
            print("If it's not on the list, it's not in the library. Please enter a valid selection.")
            continue

member_ops = Member_ops()
def member_list():
    while True: 
        member_menu = input('''
Welcome to the Tampa Library Member List! What can I do for you?

1. Become a member
2. Search for a member
3. Display full member list
4. Back to main menu                         
    ''')
        if member_menu == '1':
            member_ops.add_member()
        elif member_menu == '2':
            member_ops.member_search()
        elif member_menu == '3': 
            member_ops.display_members()
        elif member_menu == '4':
            return main()
        else:
            print("If they're not on the list, they're not a member. Please enter a valid selection.")
            continue
author_ops = Author_ops()
def author_info():
    while True: 
        author_menu = input('''
Here is our Author List! What would you like to do?:

1. Add a new author
2. Search for an author
3. Display full author list
4. Back to main menu                         
    ''')
        if author_menu == '1':
            author_ops.add_author()
        elif author_menu == '2':
            author_ops.author_search()
        elif author_menu == '3': 
            author_ops.get_info()
        elif author_menu == '4':
            return main()
        else:
            print("Our authors are not in the witness protection program. Please enter a valid selection.")
            continue

if __name__ == "__main__":
    main()
        
