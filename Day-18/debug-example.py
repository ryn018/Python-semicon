import pdb

def divide(a,b):
    pdb.set_trace() # debugging will start here
    
    result = a / b
    return result

x = 10
y = 3
print("Before diviosn.....",x,y)
print(divide(x,y))
