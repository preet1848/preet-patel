# 1. print your name 

# print("Hello , my name is preet!!")

# 2. Ask name and Print 

# name = input("what is your name : ")
# print("Nice to meet you, " , name)

# 3. sum of two number 

# a = 10
# b = 30

# sum = a + b

# print('this sum is:' , sum)

# 4. simple calculator

# a = int(input("Entre first number : "))
# b = int(input("Entre second number : "))


# print("addition : " , a + b)
# print("substraction : " , a - b)
# print("multiplication : " , a * b)
# print("devision : " , a / b)

# 5. sandwich make

# bread = input("choose Your bread (white/brown)")
# filling = input("Choose Your filling (cheese / jam / potato / banabna )")

# print("Here you silly sandwich: 🍔")
# print("[" + bread + " bread " + filling + " rainbow silly sandwich 🌈" + " ]")

# 6. rock , paper , scissors game

import random 

choices = ["rock" , "paper" , "scissors"]
computer = random.choice(choices)
player = input("choose rock , paper and scissor : ")

if player == computer: 
    print("🤣 it's tie!!!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("🎉🎊 You win..../")     
else: 
    print("🎉🎊 computer win....")