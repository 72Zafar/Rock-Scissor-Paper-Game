"""Rock Scisor Paper Game """

import random

item_list = ["rock", "scisor", "paper"]

user = input("Enter your move = Rock Scisor Paper : ")

comp = random.choice(item_list)

print (f"user choice = {user} computer choice =  {comp}")

if user == comp:
    print ("both choice same, match tie")

elif user == "rock":
    if comp == "paper ":
        print ("paper covers rock = computer win ") 

    else:
        print ("rock  smashes sciser = you win ")      


elif user == "paper":
    if comp == "scisor":
        print ("scisor cute the paper , computer win ")

    else:
        print ("paper covers rock, you win ")


elif user == "scisor":
    if comp == "paper":
        print (" scisor cute the paper, you win ")

    else :
        print ("rock smashes scisor, computer win ")                