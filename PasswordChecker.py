import string


print("----- The BEST password security analsyer in the world -----")

password = input("Please Enter your password and I shall analyse it for you: ")
password_len = len(password)

lowercase = any(char in string.ascii_lowercase for char in password)
uppercase = any(char in string.ascii_uppercase for char in password)
numbers = any(char in string.digits for char in password)
special = any(char in string.punctuation for char in password)


print("Your password is", password)
print("Your password length is", password_len)

if password_len < 5:
    print("Your password is way too short")
else:
    print("Your password is a good length!")

print("/nAnalysis:")
print("lowercase:", lowercase)
print("uppercase:", uppercase)
print("numbers:", numbers)
print("special", special)
