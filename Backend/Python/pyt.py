import random

def printHello():
    lst = []
    num = None
    r = None
    
    for number in range(51):
        lst.append(number)
    
    r = random.choice(lst)
    while num != r or num < 0 or num > 50 or ValueError: 
        try:
            num = int(input("Choose a number (0-50): "))
            
            if num == r:
                print("Awesome")
                return

            elif r - 10 <= num <= r + 10:
                print ("You are very close")

            elif 0 > num > 50:
                print ("Please enter a number between {0 - 50}")

            else:
                print ("Not yet but you got this")

        except ValueError:
            print ("Please input a integer")

printHello()
