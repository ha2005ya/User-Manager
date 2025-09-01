import os
import time

def clear_screen():
	os.system('cls' if os.name == "nt" else 'clear')

class User :
	def __init__(self , first_name , last_name , email , password , status = 'inactive'):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password 
		self.status = status
	
	def display_user(self):
		print(f"First Name: {self.first_name}")
		print(f"Last Name: {self.last_name}")
		print(f"Email:  {self.email}")
		print(f"Status: {self.status}")
		print("-" * 20)
		
def create_user():
	first_name = input("Enter first name: ")
	last_name = input("Enter last name: ")
	email = input("Enter email: ")
	password = input("Enter password: ")
	return User(first_name , last_name , email , password)

new_users = []
while True :
	print("\nWelcome to user management\n")
	print("\nChoose an Action:\n1. Add new user\n2. Display all users\n3. Exit\n")
	choice = input("Enter your choice: ")
	if choice == '1' :
		new_users.append(create_user())
		print("User added successfully! ")
		time.sleep(2)
	elif choice == '2' :
		clear_screen()
		if new_users :
			print("Displaying all users....")
			time.sleep(1)
			for e in new_users :
				e.display_user()
			time.sleep(2)
		else :
			print("Sorry , didn't find any user to display! ")
			time.sleep(2)
	elif choice == '3':
		print("Exiting....")
		break
	else :
		print("Invalid choice! Please try again.")