# 53 Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# 54 Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

from distutils.sysconfig import EXEC_PREFIX
import re

while True:
    email = input("Enter the email address: ")
    email_format = re.compile(r"^[a-zA-Z]+[@][a-zA-Z]+.com$")
    username = re.compile(r"^[a-zA-Z]+")
    companyname = re.compile(r"[@]([a-zA-Z]+)[.]")

    try:
        compare = email_format.fullmatch(email)
        if compare is None:
            raise Exception()
        else:
            user = username.findall(email)
            company = companyname.findall(email)
            print(user[0] + " , "+company[0])

    except(Exception) as err:
        print("unsupported email address format. type the proper email address.")
