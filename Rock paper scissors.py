
import random

item_list = ["Rock", "paper", "scissor"]
user_choice = input("Enter your move (Rock, paper, scissor): ")
cmp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {cmp_choice}")

if user_choice == cmp_choice:
    print("Both choices same = Match Tie!")
elif user_choice == "Rock":
    if cmp_choice == "paper":
        print("Paper covers Rock, computer wins!")
    else:
        print("Rock smashes scissor = You win!")
elif user_choice == "paper":
    if cmp_choice == "scissor":
        print("Scissor cuts paper, computer wins!")
    else:
        print("Paper covers Rock, You win!")
elif user_choice == "scissor":
    if cmp_choice == "paper":
        print("Scissor cuts paper, You win!")
    else:
        print("Rock smashes scissor, computer wins!")
else:
    print("Invalid input! Please choose Rock, paper, or scissor.")