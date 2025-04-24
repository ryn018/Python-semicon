# Program to take user input and filter all prime numbers
# Also print the missing prime numbers in the range


print("Enter Your data...")
user_data = []
while True:
    userInput = input("Enter a number: ")
    if(userInput == "!"):
        break
    else:
        if userInput.isdigit():
            user_data.append(userInput)
        
    
    