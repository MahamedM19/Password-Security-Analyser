print("----- The BEST password security analsyer in the world -----")

password = input("Please Enter your password and I shall analyse it for you: ")
password_len = len(password)


print("Your password is", password)
print("Your password length is", password_len)

if password_len < 5:
    print("Your password is way too short")
else:
    print("Your password is a good length!")
