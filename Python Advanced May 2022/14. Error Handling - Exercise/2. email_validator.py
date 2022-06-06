# 2.Email Validator
# You will be given some emails until you receive the command "End". Create the following custom exceptions to validate the emails:
# NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
# MustContainAtSymbolError - raise it when there is no "@" in the email
# InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
# When an error is encountered, raise it with an appropriate message:
# NameTooShortError - "Name must be more than 4 characters"
# MustContainAtSymbolError - "Email must contain @"
# InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
# Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
# If the current email is valid, print "Email is valid" and read the next one
#
# Input
# peter@gmail.com
# petergmail.com
#
# Output
# Email is valid
# Traceback (most recent call last):
#   File ".\email_validator.py", line 18, in <module>
#     raise MustContainAtSymbolError("Email must contain @")
# __main__.MustContainAtSymbolError: Email must contain @

class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = {".com", ".bg", ".org", ".net"}

while True:
    email = input()
    email_parts = email.split("@")

    if email == "End":
        break

    if len(email_parts) != 2:
        raise MustContainAtSymbolError(f"Email must contain @")

    username = email_parts[0]
    mail_server_and_domain = email_parts[1]
    domain = f'.{mail_server_and_domain.split(".")[-1]}'

    if len(username) <= 4:
        raise NameTooShortError(f"Name must be more than 4 characters")

    if domain not in domains:
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
