#  Write functions for checkprime, getHighestPrime, getAllPrimes

def checkprime(n):
    for i in range(2, n):
        if(n % i) == 0:
            return False
    return True

def getHighestPrime(m,n):
    for i in range(n,m-1,-1):
        if (checkprime(i)):
            return i
    return None

def getAllPrimes(m,n):
    count = 0
    primeNumbers = []
    for i in range(m,n+1):
        if checkprime(i): 
            count +=1
            primeNumbers.append(i)
    return count, primeNumbers

all = getAllPrimes(5,90)
print(all)



