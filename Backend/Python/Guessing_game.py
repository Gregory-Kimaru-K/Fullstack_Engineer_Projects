import random
game_list = []

for num in range(11):
    game_list.append(num)

def display_game():
    print ("From the following list")
    print (game_list)

def user_choice():

    #choose a random number and holding a place for user number choice

    guessed_number = random.choice(game_list)
    number = None

    #once the user chooses a correct number it stops

    while guessed_number != number:
        number = int(input("Guess a number: "))

        #Prints once correct

        if number == guessed_number:
            print("Awesome you got it correct")
            stop()

        #prints when the number is not bettween the assigned values 

        if number not in game_list:
            print ("Invalid number!")
                     

def stop():

    #Placeholder of user input

    tired = None



    while tired not in ('y', 'n'):
        
        #user input

        tired = input("Do you want to continue (Y or N): ").lower()
        
        #wrong input written

        if tired not in ('y', 'n'):
            print("Invalid choice")

        if tired == 'y':
            return True
        
        if tired == 'n':
            return False

game_on = True

while game_on:
    display_game()
    user_choice()
    game_on = stop()