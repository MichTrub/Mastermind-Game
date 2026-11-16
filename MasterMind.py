import random

def create_random(level):
    random_integer = ""
    for i in range(level):
        rand = random.randint(0,9)
        rand = str(rand)
        random_integer += rand
    return random_integer


def invalid_input_int(text1,text2,text3):
    text = text1 + text2 + text3
    Right_input = False
    while not Right_input:
        inp = input(text)
        strf = inp
        try:
            strf = int(inp)
        except:
            print("Not valid input, try again")
        else:
            return inp
        


def Wincheck(User_guess,random_integer):
    Right_numbers = 0
    Right_position = 0
    for i in range(len(random_integer)):
        if User_guess[i] in random_integer:
            Right_numbers += 1
            if User_guess[i] == random_integer[i]:
                Right_position += 1
    if Right_position == len(random_integer):
        print("You won")
        return False
    print("Right numbers: ",Right_numbers)
    print("In right position: ",Right_position)
    return True




PlayerName = input("Input your username: ")
level = invalid_input_int("Input the dificulty leve","l",": ")
level = int(level)
tries = 12
random_integer = create_random(level)
Game_run = True
while Game_run:
    Right_inp = False
    while not Right_inp:
        User_guess = str(invalid_input_int("Input your guess, you have ", str(tries)," left: "))
        if len(User_guess) == level:
            Right_inp = True
            tries -= 1
        if tries <= 0 :
            Game_run = False
            Right_inp = True
            print("You lost, loser")
            print(random_integer)
    if tries>0:
        Game_run=Wincheck(User_guess,random_integer)
    

