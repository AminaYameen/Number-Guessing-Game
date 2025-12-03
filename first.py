import random

NUM_ROUNDS = 3



def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    score=0

    for i in range(1,NUM_ROUNDS+1):
        print("Rounds",i)
    
     # Generate random numbers
    user_number=random.randint(1,100)
    computer_number=random.randint(1,100)

    print("your number is :", user_number)
    print("The computer number is :" ,computer_number)
    #Get user input
    choice=input("Do you think your number is higher or lower than the computer's?:")

    # Extension 1: Make sure the player inputs a valid choice (higher or lower)
    while choice != "higher" and choice != "lower":
        choice = input("Please enter either higher or lower: ")

    if choice=="higher"and user_number>computer_number:
        print("You were right! The computer's number was" , computer_number)
        score+=1
    elif choice=="lower"and  user_number<computer_number:
         print("You were right! The computer's number was", computer_number)
         score+=1
    else:
        print("Aww, that's incorrect. The computer's number was", computer_number)
    print("Your score is now", score)
    print()  # blank line between rounds

    print("Thanks for playing!")
    if score==NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score>=NUM_ROUNDS//2:
        print("Good job, you played really well!")
    else:
        print("good luck next time!")



if __name__ == "__main__":
    main()
