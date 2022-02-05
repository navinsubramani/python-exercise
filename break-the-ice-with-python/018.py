# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

# Example

# If the following passwords are given as input to the program:

# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:

# ABd1234@1


from ast import Pass
from gettext import find


def check_valid_password(password):
    check = [False, False, False, False, False]
    for s in password:
        if s.isupper():
            check[0] = True

        elif s.islower():
            check[1] = True

        elif s.isnumeric():
            check[2] = True

        elif s == "$" or s == "#" or s == "@":
            check[3] = True
    check[4] = 13 > len(password) > 5

    return check == [True, True, True, True, True]


li_pwd = input("Enter a sequence of comma seperated passwords: ").split(",")

print(list(filter(check_valid_password, li_pwd)))
