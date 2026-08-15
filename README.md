# Password-Security-Analyser
A Python-based password security analyser that checks password length, character usage and common-password cross-examination. 

## About this Project:

I've created this project to further my understanding of Python while also exploring the cyber security aspect of password formats.
This analyser utilizes several security criteria when evaluating a password. I've also added a simple score system to further display elements a 'strong' password would need to have against a 'weaker' one.

## Main Features:
- Password length checker
- Lowercase character detection
- Uppercase character detection
- Number detection
- Special character detection
- common passwords detection
- Password strength scoring
- A very cool display

## Technologies used:
- Python 3
- 'String' module (allows me to segregate uppercase, lowercase, numbers and special characters)
- 'getpass' module (to hide the password input for confidentiality)

## How it works:
A password is inputted.

- Password Length
The program will begin by checking the length of the password.

- Character Complexity
The program will then check whether to password contains one of the following:
, Lowercase letters
, Uppercase letters
, Numbers
, Special characters

- Common Passowrd Detection
The program will then cross-examine the inputted password against a common password list.
If it is a common password, it is automatically considered a weak password and won't be scored.

# Scoring System
The password will then be scored based on the following:
# Password length > 6: +1 score
# Lowercase letter: +1 score
# Uppercase letter: +1 score
# Numbers: +1 score
# Special character: +1 score

The maximum score is 5.

## HOW TO RUN:
1. Clone the repository.
```bash
git clone https://github.com/MahamedM19/Password-Security-Analyser.git
