import random
user_choice= int(input("what do you choose? type 0 for rock,1 for paper,2for scisser\n"))
computer_choice=random.randint(0,2)
print(computer_choice)
if user_choice==computer_choice:
    print("draw")
elif user_choice>computer_choice:
    print("ajay win")
elif user_choice==0 and computer_choice==2:
    print("draw")
elif computer_choice==0 and user_choice==2:
    print("computer win")
elif computer_choice>user_choice:
   
   print("computer win")