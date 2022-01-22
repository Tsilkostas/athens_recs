import random
#guess the number
#def main():
print("Guess a number between 1 and 100")
    #randomNumber=35
randomNumber=random.randint(1,100)
found=False   #flag variable if thy guess it



while not found:
        userGuess=int(input("Your guess:"))
        if userGuess==randomNumber:
            print ("You got it")
            found=True
        elif userGuess > randomNumber:
            print ("GUess lower")
        else:
            print("Guess higher")    
    
          
    
    
    



