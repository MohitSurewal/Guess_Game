import random

n = random.randint(1, 100) 
a = -1
guesses = 0

while (a != n):
    guesses += 1
    a = int(input("Enter your Number: "))
    if ( a >n):
        print("Lower Number please: ")
        
    else:
        print("Higher Number Please: ")
        
print(f"You have the guess the  Number {n} correctly in {guesses} guesses attempts")
    
