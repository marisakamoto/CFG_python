import random

x = 0

while x == 0:
    user_input = input("password:")
    if user_input == '1234':
        x = 1
    print("Incorrect Password!")

if (x == 1):
    print("Success!")
