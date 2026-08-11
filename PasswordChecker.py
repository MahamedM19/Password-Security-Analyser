import string
from getpass import getpass


print("----- The BEST password security analsyer in the world -----")

password = getpass("Please Enter your password and I shall analyse it for you: ")


common_passwords = {
    "password",
    "hello123",
    "123456",
    "admin",
    "welcome",
    "qwerty",
    "asdfg",
    "zxcvb",
}



def check_length(password):
    return len(password)
password_len = check_length(password)


def check_character_types(password):
    lowercase = any(char in string.ascii_lowercase for char in password)
    uppercase = any(char in string.ascii_uppercase for char in password)
    numbers = any(char in string.digits for char in password)
    special = any(char in string.punctuation for char in password)

    return lowercase, uppercase, numbers, special 
lowercase, uppercase, numbers, special = check_character_types(password)

def check_common_passwords(password):
    return password.lower() in common_passwords
commonpassword = check_common_passwords(password)

score = 0

if password_len >= 6:
    score += 1
if lowercase:
    score += 1
if uppercase:
    score += 1
if numbers:
    score += 1
if special:
    score +=1




print("\n====================================")
print("      PASSWORD STRENGTH REPORT")
print("====================================")


print("\nPassword Length:", password_len)


print("\nCharacter Analysis:")

if lowercase:
    print("Lowercase letters: ✓")
else:
    print("Lowercase letters: ✗")

if uppercase:
    print("Uppercase letters: ✓")
else:
    print("Uppercase letters: ✗")

if numbers:
    print("Numbers: ✓")
else:
    print("Numbers: ✗")

if special:
    print("Special characters: ✓")
else:
    print("Special characters: ✗")


print("\nSecurity score:", score,"/ 5")

print("\nCommon password check:")
if commonpassword:
    print("\n✗ Your password has been found in the common password list.")
else:
    print("✓ Your password has NOT been found in the common password list.")

if commonpassword:
    print("\nYour password is a common password. It has been rated -1000")
elif score <= 2:
    print("\nYour password has been deemed weak.")
elif score <= 4:
    print("\nYour password has a medium strength level.")
else:
    print("\nYour password is very strong!")

