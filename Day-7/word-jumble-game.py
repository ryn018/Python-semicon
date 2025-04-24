
'''
    Jumbled Word: "otpcomure"
    Your Guess: "computer"
    ✅ Correct! 

'''

import random

# function to jumble the word

def jumble(w):
    temp = list(w)
    random.shuffle(temp)
    return ''.join(temp)


# Welcome message

print("\n")
print("Welcome to the WORD JUMBLE GAME")
print("-" * 80)

print("The computer presents a jumbled word")
print("You need to guess it. For every correct guess")
print("you will be offered a point")
print("-" * 80)

# Get the words and process it 
f = open(r"C:\Users\292905\Desktop\Python semicon\Day-7\words.txt")
content = f.readlines()
words = content[0].strip().split(",")
hints = content[1].strip().split(",")

word_hint_dict = dict(zip(words, hints))

print(word_hint_dict)

f.close()



 

# print("INFO content -> ", content)

points = 0
first = 0
second = 0

# for every word in list of words
random.shuffle(words)

for word in words:

    print("\n")

    # jumble the word
    jumbled_word = jumble(word)

    # show to the user
    print(jumbled_word)

    # ask user input
    user_word = input("Can you guess -> ")

    # compare user input and update points
    if(user_word != word):
        print(f"Wrong answer ! Here is the hint {word_hint_dict[word]}")
        user_word = input("Guess once more: ")


        if user_word == word:
                points += 1
                print("\U00002705 Correct")
        else:
                print("\U00002745 In-correct")


    elif(user_word == word):
        points += 2
        print("\U00002705 Correct")

    else:
        print("\U00002745 In-correct")

    

# show the results

print("-" * 80)

if(points > 6):
    print("You have played well")
else:
    print("You need to improve on your vocabulary")

