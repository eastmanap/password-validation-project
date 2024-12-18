# Apollos Eastman
# Dec 18 2024
# password validation

# Check length
def check_length(password):
    if len(password) < 8:
        return('Password must be at least 8 characters long.')
    return

# Check first five
def check_first_five(password):
    if len(password) >= 5 and not password[:5].isalpha():
        return('The first five characters must be letters only!')
    return

# Check last three
def check_last_three(password):
    if len(password) >= 3 and not password[-3:].isdigit():
        return ('The last three characters must be numbers only!')
    return

# Check for letters
def check_for_letter(password):
    for char in password:
        if char.isalpha():
            return
    return('Password must contain at least one letter!')

# Check for no special
def check_no_special_chars(password):
    allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
    for char in password:
        if char not in allowed_characters:
            return ('Password cannot contain special characters or symbols!')
    return

# Check for number

def check_for_number(password):
    for char in password:
        if char.isdigit():
            return
    return('Password must contain at least one number!')

# Validate password

def validate_password(password):
    errors = []

    checks = [
        check_length(password),
        check_first_five(password),
        check_last_three(password),
        check_for_letter(password),
        check_for_number(password),
        check_no_special_chars(password)
    ]

    for check in checks:
        if check:
            errors.append(check)
    
    if errors:
        return errors
    else:
        return ['Password is valid.']

# Main

def main():
    password = input('Enter your password: ')
    
    result = validate_password(password)

    if 'Password is valid.' in result:
        print(result[0])
    else:
        print('Invalid password! Reasons:')
        for error in result:
            print("- " + error)
        
        main()

if __name__ == "__main__":
    main()
