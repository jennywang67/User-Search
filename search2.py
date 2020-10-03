import json # Imports JSON module

with open('usernames3.json') as f: # Reads the JSON file "usernames3"
  data = json.load(f) # Parses the JSON file and stores the information in dictionary "data"

pattern = input("Enter a string pattern: ") # Prompts user to enter a string pattern in the terminal
print("Looking for: " + pattern) # Tells the user program is starting to search


i = 1 # The first username in the JSON file is indexed as 1

# Parses through all the users and checks if the the user inputted string pattern matches with any code
# in the usernames3 JSON file
# Prints all the usernames with matching code
while i<=len(data): # Parses through all users
  if pattern in data[str(i)]["code"]: # Checks if the string pattern is a substring of any of the user's code
    print(data[str(i)]["user"]) # If it is a substring then the user's username is printed
  i+=1 # Increments to the next user

# Additional Functionality to add users and their code---------------------------------------------------------
print("Would you like to add a new user and their code?")
answer = input("Enter 'Y' if yes and 'N' if no: ")

# Excecutes only if the user wants to add more users and code to the usernames3 JSON file
if(answer == 'Y'):
    newUser = input("Enter their username: ") # Prompts user for a new username
    newCode = input("Enter their code: ") # Prompts user for new code
    newJSON = {"user": str(newUser), "code" : str(newCode)} # Organizes the new information into dictionary "newJSON"

    with open('usernames3.json', 'r+') as f: # Opens usernames3 to edit
        data = json.load(f) # Stores the JSON information
        data[str(len(data)+1)] = newJSON # Stores newJSON as a part of a new index, which is +1 of the previous
                                         # highest index
        f.seek(0) # Resets JSON file position
        json.dump(data, f, indent=4) # Converts newJSON to a JSON object
        f.truncate() # Resizes file
