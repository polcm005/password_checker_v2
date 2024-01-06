class lengthError(Exception):
    """Exception class for <8 character password"""
    pass


class upperError(Exception):
    """Exception class for password without uppercase characters"""
    pass


def length_check(password: str):
    # check whether password is 8 characters or longer
    try:
        if len(password) <= 8:
            raise lengthError(f"{password} Password too short")
    except lengthError as error:
        print(error)
    else:
        print(f"{password} Password meets length requirements")


def upper_case_check(password: str):
    # check whether password has any upper case characters
    try:
        if not any(character.isupper() for character in password):
            raise upperError(f"{password} does not contain upper case letters")
    except upperError as error:
        print(error)
    else:
        print(f"{password} contains an upper case letter")
    finally:
        print()


def password_checker(password: str):
    length_check(password)
    upper_case_check(password)


password_list = ["#&*#@", "aaaaaaaaa", "BBBBBBBBB", "1223545452",
                 "DWghh23(&@*&"]

for element in password_list:
    password_checker(element)

