# Welcome to the Tampa Library Member List! What can i do for you?

# 1. Become a member
# 2. Search for a member
# 3. Display full member list
# 4. Back to main menu             

class Member():

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.current_loans = 0

   
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def get_id(self):
        return self.user_id
    def set_id(self, new_id):
        self.user_id = new_id
    
    def get_info(self):
        print(f"{self.name} at user ID: {self.user_id} currently has {self.current_loans} out on loan!")
        

class Member_ops():
     
    def __init__(self):
        self.members ={}

    def add_member(self):
        name = input("What is your name? ").title()
        user_id= int(input("Please enter your phone number with no spaces or dashes: "))
        if user_id in self.members:
            print("You are already a member.")
        else:
            add_member = Member(name, user_id)
            self.members[user_id] = add_member
            print(f"{name} has been added to the member.")

    def member_search(self):
        search = input("Please enter the name of the user you are searching for:  ").title()
        found = False
        for user_id, member in self.members.items():
            if search == member.name:
                print(f"{member.name}, currently has {member.current_loans} out on loan.")
                found = True
                break
        if not found:
            print("Member not found.")

    def display_members(self):
        for user_id, member in self.members.items():
            print(f"{member.name} at user ID: {member.user_id} currently has {member.current_loans} out on loan.")
            break
            