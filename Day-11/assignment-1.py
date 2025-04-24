"""

3. Implement the Guess-my-Number game in the OOP framework

    Computer has chose a number (1, 100), can you guess? Max. 10 guesses

    -> 35
    Higher

    -> 65
    Lower

    -> 44
    Higher

    -> 45
    Correct

    Number of attempts 4/10
    Excellent playing!

    
"""
import random

class Game:
    def __init__(self):
        self.attempts = 0
    def check_answer(self,user_input,num):
        if user_input < num:
            self.attempts += 1
            print(f"Your guess is lower!!")
        elif user_input > num:
            self.attempts += 1
            print(f"Your guess is Higher!!")
        else:
            self.attempts += 1
            return True

game1 = Game()
computer_num = random.randint(1,100)
print(computer_num)
n = 0
while n < 10:
    user_num = int(input("Enter your guess(1-100): "))
    ans = game1.check_answer(user_num,computer_num)
    n += 1
    if ans:
        print(f"Congragulations your answer is correct❤️")
        break
    if n == 10:
        print("Sorry You ran out of chances..")




"""
random
 
class Guessthenumber:
    def __init__(self):
        self.number = random.randint(1, 80)
        self.no_of_gusess = 10
 
    def start_game(self):
        for attempt in range(1, self.no_of_gusess + 1):
            guess = int(input(f"Attempt {attempt}/{self.no_of_gusess} - Give your guess: "))
            if guess < self.number:
                print("Give a bit higher")
            elif guess > self.number:
                print("Give a bit lower")
            else:
                print(f"WooHoo...yeah...you guessed it Correct! in {attempt} attempts.")
                print("really you have a brain...!!!") 
                break
        else:
            print(f"ohh...ohh...Sorry! the number is {self.number}.")
            print("get your brain and try again")
 
game = Guessthenumber()
 
game.start_game()
"""




        


