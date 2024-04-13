import random
import string

def generate_password(min_length,number=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
#create a string which has all of the diffrent characters and special characters
    
    characters = letters
    if number :
        characters += digits
    if special_characters :
        characters += special

    pwd = "" #password set to empty
    meets_criteria =  False #we dont number and special character
    has_numbers =  False
    has_special = False

    while not meets_criteria or len(pwd) <= min_length: #either of these are true wwe will continue
        new_char = random.choice(characters) #generate a new password by randomly selecting
        pwd += new_char #put in place of password

        if new_char in digits:
            has_numbers = True  #both the condition check ifthe things are there in numbers,special etc
        elif new_char in  special:
            has_special = True

        meets_criteria = True
        if number :
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length : "))
has_number = input("Do you want to have numbers (y/n)?").lower() == "y"
has_special = input("Do you wwant to have special characters : (y/n)").lower() == "y"
pwd = generate_password(min_length,has_number,has_special)
print(pwd)
