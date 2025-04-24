import random

def jumpled(word):
    list1 = list(word)
    random.shuffle(list1)
    new_str = "".join(list1)
    return new_str

dic_new = {}
score = 0
first = 0
second = 0

with open(r"C:\Users\292905\Desktop\Python semicon\Day-7\words.txt") as file:
    fruitsAndVegies = file.readline().strip().split(',')
    hints = file.readline().split(',')

    print(fruitsAndVegies)
    # print(hints)

    dic_new = zip(fruitsAndVegies,hints)
    dic_new = dict(dic_new)
    print(dic_new)
    


    random.shuffle(fruitsAndVegies)
    for i in fruitsAndVegies:
        jumpled_word = jumpled(i)
        print(jumpled_word)
        user_input = input("Enter your answer: ")
        if user_input == i:
            print("correct answer")
            score += 2
            first +=1
        elif user_input != i:
            print("Try again..")
            print(f"Here is your hint: {dic_new[i]}")
            user_input = input("Guess once more: ")

            if user_input == i:
                score += 1
                second += 1
                print("correct answer")
            else:
                print("wrong answer")
        
    print(f"Total: {score}")
    print(f"First: {first}")
    print(f"Second: {second}")
        
    if score > 15 :
        grade = "A+"
    elif score > 10:
        grade = "B+" 
    elif score > 0:
        grade = "C+"
    print(f"grade : {grade}")
            
            


    




    

