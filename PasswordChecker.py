import string

print("----- The BEST password security analsyer in the world -----")

password = input("Please Enter your password and I shall analyse it for you: ")


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




print("Your password is", password)
print("Your password length is", password_len)
print("Common password:", commonpassword)


print("\nAnalysis:")
print("lowercase:", lowercase)
print("uppercase:", uppercase)
print("numbers:", numbers)
print("special", special)

if score <= 2:
    print("Your password is WEAK")
elif score <= 4:
    print("Your password is meh")
else:
    print("Wow! your password is very strong")

if commonpassword:
    print("\nTHIS IS A COMMON PASSWORD")
    print("PLEASE DO NOT USE THIS PASSWORD!")
