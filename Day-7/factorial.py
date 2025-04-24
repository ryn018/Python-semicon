# Create nfactorial(n) which raises an exception if the input value is 0 or less, test it

def nfactorial(n):
    if n <=0 :
        raise Exception()
    fact = 1
    for i in range(1, n + 1):
        fact =  fact * i
    return(fact)



num = 8

try:
    fact = nfactorial(num)
    print(fact)
except Exception as e:
    print(f"should not be less than 0 {e}")




