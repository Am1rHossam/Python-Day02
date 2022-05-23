import re


def user_data():
    name=input("Please enter your name: ")
    if name.isalpha():
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email=input("Please enter you email: ")
        if(re.fullmatch(regex,email)):
            print("Valid Email")
        else:
            print("invalid email")
    else:   
        print("Please enter alphabetic only")



user_data()