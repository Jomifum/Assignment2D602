#Q1
# See the correct code :
numbers = [1, 2, 3, 4, 5]
print(numbers[:])

#Q2
# Starting an empty list to store sales
sales = []

# Creating the Loop to get sales input for each day of the week (7 days)
for i in range(1, 8):
    day_sales = float(input(f"Enter sales for day {i}: "))
    sales.append(day_sales)  # Add each day's sales to the list

# Calculate the total sales for the week
total_sales = 0
for sale in sales:
    total_sales += sale

# Display the total of sales
print(f"Total sales for the week: ${total_sales:.2f}")

#Q3
# Create a list of places with not alphabetical order
travel_list = ['Paris', 'New York', 'Toronto', 'Rome', 'Prague']

# Print the list in original order
print("Original list:")
print(travel_list)

# Sort the list in alphabetical order then print it
travel_list.sort()
print("\nList sorted in alphabetical order:")
print(travel_list)

# Sort the list in reverse alphabetical order and print it
travel_list.sort(reverse=True)
print("\nList sorted in reverse alphabetical order:")
print(travel_list)

#Q4
# Create a dictionary for course numbers and room numbers
course_rooms = {
    'CST401': 'Room 900',
    'CST502': 'Room 901',
    'CST403': 'Room 902',
    'CST504': 'Room 903',
    'CST405': 'Room 904'
}

# Create a dictionary for course numbers and instructors
course_instructors = {
    'CST401': 'Dr. Milonas',
    'CST502': 'Prof. Yong',
    'CST403': 'Prof. Xiaoquan',
    'CST504': 'Prof. De Freitas',
    'CST405': 'Prof. Boulet'
}

# Create a dictionary for course numbers and meeting times
course_times = {
    'CST401': '11:00 AM',
    'CST502': '04:00 PM',
    'CST403': '09:00 AM',
    'CST504': '12:00 PM',
    'CST405': '6:00 PM'
}

# Prompt the user to enter a course number
course_number = input("Enter a course number (e.g., CST504): ")

# Check if the course number exists in the dictionaries
if course_number in course_rooms and course_number in course_instructors and course_number in course_times:
    print(f"Course: {course_number}")
    print(f"Room: {course_rooms[course_number]}")
    print(f"Instructor: {course_instructors[course_number]}")
    print(f"Meeting time: {course_times[course_number]}")
else:
    print("Course not found.")

#Q5
# Initialize a dictionary to store names and email addresses
email_directory = {
    'Peter Garcia': 'pgarcia@gmail.com.com',
    'Andrea Mcneil': 'amcneilh@yahoo.com',
    'Daniel Williams': 'dwilliams@live.com'
}

# Define a function to display the menu options
def display_menu():
    print("\nMenu:")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Exit")

# Function to look up an email address
def lookup_email():
    name = input("Enter the name of the person: ")
    if name in email_directory:
        print(f"{name}'s email address: {email_directory[name]}")
    else:
        print(f"No entry found for {name}.")

# Function to add a new name and email address
def add_entry():
    name = input("Enter the name: ")
    if name in email_directory:
        print(f"{name} is already in the directory.")
    else:
        email = input("Enter the email address: ")
        email_directory[name] = email
        print(f"Added {name} with email {email}.")

# Function to change an existing email address
def change_email():
    name = input("Enter the name of the person: ")
    if name in email_directory:
        email = input(f"Enter the new email address for {name}: ")
        email_directory[name] = email
        print(f"{name}'s email address has been updated to {email}.")
    else:
        print(f"No entry found for {name}.")

# Function to delete a name and email address
def delete_entry():
    name = input("Enter the name of the person to delete: ")
    if name in email_directory:
        del email_directory[name]
        print(f"{name} has been deleted from the directory.")
    else:
        print(f"No entry found for {name}.")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        lookup_email()
    elif choice == '2':
        add_entry()
    elif choice == '3':
        change_email()
    elif choice == '4':
        delete_entry()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
