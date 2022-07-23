######
# Name: JoshFuncs
# Author: Joshcubes
# Last Edit: 23/07/2022
######

def intinput(prompt):
    while True:
        raw = input(prompt)
        try:
            return(int(raw))
        except(ValueError):
            print("Please Enter A Number: ")

def intinputrange(prompt, min, max):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number between " + str(min) + " and " + str(max) + ".")
