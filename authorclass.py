#Here is our Author List! What would you like to do?:

#1. Add a new author
#2. Search for an author
#3. Display full author list
#4. Back to main menu

author_list = {
'Gregory David Roberts': {'Birthdate' : '6/21/1952', "Short Bio" : 'reformed convict and author of the novel Shantaram, where he turned his life experiences into one of the most riveting stories ever told.',},
'JJR Tolkien': { "Birthdate ": '1/3/1892', "Short Bio" : 'English writer who created an entire language and decided it needed a story to go with it. Author of The Silmarillion, The Hobbit and Lord Of The Rings',}, 
'Frank Herbert': {"Birthdate": '11/8/1920', "Short Bio" : " American sci-fi writer with a rich history in short stories and newspaper articles"},
'George RR Martin': {"Birthdate": '9/20/1948', "Short Bio" : "American novelist and short story writer in the fantasy, horror, and science fiction genres, screenwriter, and television producer. He is best known for his series of epic fantasy novels, A Song of Ice and Fire, which was adapted into the HBO series Game of Thrones (2011–2019)."},
'J.K. Rowling': {"Birthdate": '7/31/1965', "Short Bio" : "British author, TERF, and philanthropist. She is best known for writing the Harry Potter fantasy series, which has won multiple awards and sold more than 500 million copies, becoming the best-selling book series in history."},
'Brandon Sanderson': {"Birthdate": '12/19/1975', "Short Bio" : "American author of epic fantasy and science fiction. He is best known for the Cosmere universe, in which most of his fantasy novels, most notably the Mistborn series and The Stormlight Archive, are set."},
'Robert Jordan': {"Birthdate": '10/17/1948', "Short Bio" : "American author of epic fantasy. He is best known for the Wheel of Time series, which comprises 14 books and a prequel novel. Jordan's books have been praised for their complex characters and intricate world-building."},
'Isaac Asimov': {"Birthdate": '1/2/1920', "Short Bio" : "American writer and professor of biochemistry at Boston University. He was known for his works of science fiction and popular science. Asimov was a prolific writer, and wrote or edited more than 500 books."},
'Arthur C. Clarke': {"Birthdate": '12/16/1917', "Short Bio" : "British science fiction writer, science writer and futurist, inventor, undersea explorer, and television series host. He co-wrote the screenplay for the 1968 film 2001: A Space Odyssey, one of the most influential films of all time."},
'Darren Shan': {"Birthdate": '7/2/1972', "Short Bio" : "Irish author. Darren O'Shaughnessy who commonly writes under the pen name Darren Shan, is an Irish author. Darren Shan is the main character in O'Shaughnessy's The Saga of Darren Shan young adult fiction series, also known as the Cirque Du Freak series in the United States. AND JOHN C. REILLY RUINED ANY CHANCE OF A MOVIE FRANCHISE!!!"},
'Neil Gaiman': {"Birthdate": '11/10/1960', "Short Bio" : "English author of short fiction, novels, comic books, graphic novels, nonfiction, audio theatre, and films. His works include the comic book series The Sandman and novels Stardust, American Gods, Coraline, and The Graveyard Book."},
'Stephen King': {"Birthdate": '9/21/1947', "Short Bio" : "American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels. His books have sold more than 350 million copies, and many have been adapted into films, television series, miniseries, and comic books."}

}

class Author():
    def __init__(self, name, birth_date, short_bio):
        self.name = name
        self.birth_date = birth_date
        self.short_bio = short_bio

    def set_name(self, new_name):
        self.name =  new_name
    
    def set_birth_date(self, birth):
        self.birth_date = birth
    
    def set_short_bio(self,new_bio):
        self.short_bio = new_bio

    def get_info(self):
        print(f"{self.name} was born on {self.birth_date}. {self.short_bio}")

class Author_ops():
     
    def __init__(self):
        self.authors =[]

    def add_author(self):
        name = input("What is their name? ").title()
        birth_date= input("What is their birthdate? ").title()
        short_bio= input("Tell me a little about them? ")
        new_author = Author(name, birth_date, short_bio)
        self.authors.append(new_author)

    def author_search(self):
        search = input("Please enter the name of the author you are searching for: ").title()
        for author in author_list:
            if search == author:
                print(f"{author} was born on {author_list[author]['Birthdate']}. {author_list[author]['Short Bio']}")
                break

    def get_info(self):
        print(author_list)
            
            