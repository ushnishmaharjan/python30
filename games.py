import random

# print(int(random.random()*100))

# print(random.randint(40,90))

#count = 1
#random_num = random.randint(40, 90)
#print(random_num)

#while True:
#    if count == 5:
#        user_num = int(input("Enter a number: "))
#        print("limit reached", "the number was", random_num)
#        print("Do you want to play again? ")
#        play = input(" (yes/no): ")
#        if play.lower() == "yes":
#            count = 1
#            random_num = random.randint(40, 90)
#        else:
#            print("Thank you for playing!")
#            break
#    if user_num == random_num:
#        print(f"Congratulations! You guessed the number in {count} tries.")
#        print("Do you want to play again? ")
#        play = input(" (yes/no): ")
#        if play.lower() == "yes":
#            count = 1
#            random_num = random.randint(40, 90)
#        else:
#            print("Thank you for playing!")
#            break
#    else:
#        print("Try again!")
#    count = count + 1

#random_num = random.randint(40, 90)
#computer=0
#user=0
#
#while True:
#  
#    user_num = int(input("Enter a number: "))
#    
#    if user_num == random_num:
#        user = user + 5
#        print("Congratulations! You guessed the number.")       
#    else:
#        print("Try again!")
#    if user==20 or computer==20 :
#        print("Do you want to play again? ")
#        play= input(" (yes/no): ")
#        if play.lower() == "yes":
#            computer=0
#            user=0    
#            random_num = random.randint(40, 90)
#            print(point)
#        else:
#            print("Thank you for playing!")
#            break       
#        computer = computer + 5
#    if computer < user:
#        point=f"You scored {user} points and computer scored {computer} points"
#    elif computer > user:
#        point=f"You scored {user} points and computer scored {computer} points"
#    elif computer == user:
#        point="It's a tie!"
#print(point)
    

computer=0
user=0
a=["rock","paper","scissors"]
while True:
    computer_choice = random.choice(a)
    input1= input("Enter rock, paper, or scissors: ")
    print(f"Computer chose: {computer_choice}")
    user_choice = input1.lower()
    if (user_choice == "rock" and computer_choice == "scissors") : 
        user = user + 2
        print(f"you won {user} points and computer scored {computer} points")
    elif(user_choice== "paper" and computer_choice == "rock"):
        user = user + 2
        print(f"you won {user} points and computer scored {computer} points")
    elif(user_choice == "scissors" and computer_choice == "paper"):
        user = user + 2
        print(f"you won {user} points and computer scored {computer} points")
    elif (user_choice == "scissors" and computer_choice == "rock") : 
        computer = computer + 2
        print(f"you won {user} points and computer scored {computer} points")
    elif(user_choice== "rock" and computer_choice == "paper"):
        computer = computer + 2
        print(f"you won {user} points and computer scored {computer} points")
    elif(user_choice == "paper" and computer_choice == "scissors"):
        computer = computer +2
        print(f"you won {user} points and computer scored {computer} points")
    elif user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice<computer_choice:
        print(f"you scored {user} points and computer scored {computer} points")    
    if user==10 or computer==10 :
        print("Do you want to play again? ")
        play= input(" (yes/no): ")
        if play.lower() == "yes":
            computer=0
            user=0    
            computer_choice = random.choice(a)      
        else:
            print("Thank you for playing!")
            break       


