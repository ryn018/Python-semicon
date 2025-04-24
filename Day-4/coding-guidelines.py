'''
Program to separate the prime numbers from the user input
Notes:
    Use input validation

'''

# Input

print("This app separates the prime numbers from your inputs")
print("-"*80)

print("Enter your inputs: (! to quit) ")

# Collect the data from the user from the console
input_numbers = []   # Container for user input number

while True: 
    # Get the input
    user_input = input("-> ")

    # Check if the input is the terminating condition
    if(user_input == 's'):
        break

    # Otherwise, validate if it is an integer and add to the container
    if( user_input.isdigit() ):
        input_numbers.append(int(user_input))

# ----------------------- DEBUG statements -------------------------------- #
print("INFO [input_number] -> ", input_numbers)
# ------------------------------------------------------------------------- #

# Process

# Prime number container
primes = []

# Go through every number
for num in input_numbers:

    # Check if the number is prime and add to primes container
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        primes.append(num)

# Output

print("-"*80)
print('Primes -> ', *primes)


# Class-assignment:
'''
Upgrade the code to display the minimum and maximum of the list
'''

# Finding maximum and minimum using min and max functions

min_num = min(primes)
max_num = max(primes)

print(f"The minimum number in the list is : {min_num}")
print(f"The maximum number in the list is : {max_num}")






