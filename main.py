# Apollos Eastman
# Dec 18 2024
# password validation

password = input('Input your password:')

# Check length
def check_length():
    if len(password) < 8:
        return('Password must be at least 8 characters long.')
    else:
        return

print(check_length())

# Check first five
def check_first_five():
    if len(password) >= 5 and not password[:5].isalpha():
        return('The first five characters must be letters only!')
    else:
        return

print(check_first_five())

# Check last three
def check_last_three():
    if len(password) >= 3 and not password[-3:].isdigit():
        return ('The last three characters must be numbers only!')
    else:
        return

print(check_last_three())

# Check for letters
def check_for_letter():
    for char in password:
        if char.isalpha():
            return
        else:
            return('Password must contain at least one letter!')

print(check_for_letter)

# Check for no special
def check_no_special_chars():
   
    allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    for char in password:
        if char not in allowed_characters:
            return ('Password cannot contain special characters or symbols!')
        else:
            return

print(check_no_special_chars())

# Check for number

def check_for_number(password):
    for char in password:
        if char.isdigit():
            return
        else:
            return('Password must contain at least one number!')

print(check_for_number())
