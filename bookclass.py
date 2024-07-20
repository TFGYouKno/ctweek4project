# Welcome to the Book Repository! what would you like to do?:

# 1. Add a new book
# 2. Borrow/Rent a book
# 3. Return a book
# 4. Search the Repository 
# 5. Display the Repository
# 6. Back to main menu

Book_list = {
'Dune': {"author" : 'Frank Herbert', "Genre": 'Science Fiction', "Summary" : 'The battle for spice is on and there can only be one victor in charge of the spice fields', "Available" : 'YES'},
'The Hobbit': {"author" :  'JRR Tolkien', 'Genre' : 'Fantasy', 'Summary' : 'A group of friend must travel through Middle Earth to defeat a dragon and save the Dwarven Homeland','Available': 'YES'},
'Shantaram': {"author": 'Gregory David Roberts', 'Genre': 'Memoir', 'Summary' : 'An escaped convict flees an Australian prison, and escapes to Bombay, India. He starts a new life for himself in a completely foreign land, and finds beauty wherever he looks', 'Available' : 'YES'},
'Game of Thrones': {"author": 'George RR Martin', 'Genre': 'Fantasy', 'Summary' : 'The battle for the Iron Throne is on, and there can only be one victor', 'Available' : 'YES'},
'Harry Potter and the Sorcerer\'s Stone': {"author": 'J.K. Rowling', 'Genre': 'Fantasy', 'Summary' : 'A young orphan finds out he is a wizard and is sent to a school for magic', 'Available' : 'YES'},
'Harry Potter and the Chamber of Secrets': {"author": 'J.K. Rowling', 'Genre': 'Fantasy', 'Summary' : 'A young wizard must solve the mystery of the Chamber of Secrets', 'Available' : 'YES'},
'Harry Potter and the Prisoner of Azkaban': {"author": 'J.K. Rowling', 'Genre': 'Fantasy', 'Summary' : 'A young wizard must solve the mystery of the escaped prisoner', 'Available' : 'YES'},
'Harry Potter and the Goblet of Fire': {"author": 'J.K. Rowling', 'Genre': 'Fantasy', 'Summary' : 'A young wizard must compete in the Triwizard Tournament', 'Available' : 'YES'},
'Harry Potter and the Order of the Phoenix': {"author": 'J.K. Rowling', 'Genre': 'Fantasy', 'Summary' : 'A young wizard must fight against the dark forces', 'Available' : 'YES'},
'Harry Potter and the Half Blood Prince': {"author": 'J.K. Rowling', 'Genre': 'Fantasy', 'Summary' : 'A young wizard must uncover the truth about the dark lord', 'Available' : 'YES'},
'Harry Potter and the Deathly Hallows': {"author": 'J.K. Rowling', 'Genre': 'Fantasy', 'Summary' : 'A young wizard must defeat the dark lord', 'Available' : 'YES'},
'The Final Empire': {"author": 'Brandon Sanderson', 'Genre': 'Fantasy', 'Summary' : 'A world of magic and intrigue, where the highstorms can kill', 'Available' : 'YES'},
'The Way of Kings': {"author": 'Brandon Sanderson', 'Genre': 'Fantasy', 'Summary' : 'First in the Stormlight series, it sets the stage for the rest of the series', 'Available' : 'YES'},
'Wheel of Time': {"author": 'Robert Jordan', 'Genre': 'Fantasy', 'Summary' : 'An epic battle between light and dark, culminating in a fight against The Dark One', 'Available' : 'YES'},
'Foundation': {"author": 'Isaac Asimov', 'Genre': 'Science Fiction', 'Summary' : 'Someone predicts the end of a galactic empire by using math, but you won\'t care.', 'Available' : 'YES'},
'2001: A Space Odyssey': {"author": 'Arthur C. Clarke', 'Genre': 'Science Fiction', 'Summary' : 'The story of Human\'s evolution from apes to Star Child.', 'Available' : 'YES'},
'Cirque Du Freak': {"author": 'Darren Shan', 'Genre': 'Horror', 'Summary' : 'A young boy named Darren Shan must become a vampire to save his best friend', 'Available' : 'YES'},
'American Gods': {"author": 'Neil Gaiman', 'Genre': 'Fantasy', 'Summary' : 'Old gods vs new gods, who will win?', 'Available' : 'YES'},
'The Stand': {"author": 'Stephen King', 'Genre': 'Horror', 'Summary' : 'A plague wipes out most of humanity, and the survivors must choose between good and evil', 'Available' : 'YES'},
'IT': {"author": 'Stephen King', 'Genre': 'Horror', 'Summary' : 'A group of friends must face their fears and defeat an ancient evil, but the real horror is a two page occurence in a sewer. How is this guy not on a registry?', 'Available' : 'YES'},
'The Shining': {"author": 'Stephen King', 'Genre': 'Horror', 'Summary' : 'A family must survive a haunted hotel, and the father must fight his own demons', 'Available' : 'YES'},

    }

class Book():
    

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = "Available"

    def set_title(self, new_title):
        self.title = new_title
    
    def set_author(self, author):
        self.author = author
    
    def set_genre(self,new_genre):
        self.genre = new_genre

    def get_info(self):
        print(f"{self.title} by {self.author}, Genre: {self.genre}, Availability: {self.availability}")

class Book_ToDos():
    def __init__(self):
        self.books =[]
        self.rented = []

    def add_book(self):
        title = input("What is the title of the book? ").title()
        author = input("Who wrote the book?  ").title()
        genre = input("What genre would you list it under?  ").title()
        added_book = Book(title, author, genre)
        self.books.append(added_book)
        print(f"{title} by {author} has been added to the repository.")

    def rent_book(self):
        requested_title = input("Enter the title of the book you want to rent: ")
        if requested_title in Book_list:
            if Book_list[requested_title]['Available'] == 'YES':
                Book_list[requested_title]['Available'] = 'NO'
                print(f"You have successfully rented '{requested_title}'.")
            else:
                print(f"Sorry, '{requested_title}' is currently unavailable.")
        else:
            print(f"Sorry, '{requested_title}' is not in the repository.")


    def display_books(self):
        for title in Book_list:
            print(f"{title} by {Book_list[title]['author']}, Availability: {Book_list[title]['Available']}")


      
            


            

    def return_book(self):
        rental = input("What book are you trying to return?  ").title()
        if rental in Book_list:
            if Book_list[rental]['Available'] == 'NO':
                Book_list[rental]['Available'] = 'YES'
                print(f"Thank you for returning '{rental}'.")
            else:
                print(f"'{rental}' is not currently checked out.")
        else:
            print(f"'{rental}' is not in the repository.")
        
    
    def book_search(self):
        search = input("Please enter the case sensitive title of the book you are looking for:  ").title()
        if search in Book_list:
            print(f"{search} by {Book_list[search]['author']}, Genre: {Book_list[search]['Genre']}, Summary: {Book_list[search]['Summary']}, Availability: {Book_list[search]['Available']}")
        else:
            print("Book not found, try again.")
            return
        