import string


print("----- The BEST password security analsyer in the world -----")

password = input("Please Enter your password and I shall analyse it for you: ")
password_len = len(password)
score = 0

lowercase = any(char in string.ascii_lowercase for char in password)
uppercase = any(char in string.ascii_uppercase for char in password)
numbers = any(char in string.digits for char in password)
special = any(char in string.punctuation for char in password)

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


print("/nAnalysis:")
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
