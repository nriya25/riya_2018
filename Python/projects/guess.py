import random
while input("\n\n press any key to continue:") :
    cguess=random.randint(1,50)

    i=0
    while i <= 6 :
        if i == 6:
            print("you lose")
            print("computer guess was",cguess)
            break
        guess=int(input("enter your guess"))  
        if guess < cguess :
          print("type greater value")
        elif guess > cguess :
          print("type smaller value")
        else :
          print("your guess is correct. CONGRATULATONS!!")
          print("computer guess was",cguess)
          break
        i = i+ 1 
