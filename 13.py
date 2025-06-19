# Part:1  Use of Built-in Function in Python

import random

# # import the random module to generate random number later.

# print("<==== Built-in function on list ====>")

# numbers = [4 , 2 , 7 , 9 , 5 , 6 ]

# print("list : " , numbers)

# # len()

# print("length of list : " , len(numbers))

# print("Max number : " , max(numbers))

# print("Min number : " , min(numbers))

# print("sum of list : " , sum(numbers))

# part:2 Negative Float Number 

# print("<==== part:2 opertaor  in negative value")

# num = float(input("Enter a negative float number : "))

# print("Positive Version from the user : " , abs(num))

# print("Power of value : " , pow(num , 10))

# print("Roundof value :" , round(num))

# Part:3 random List and Its Values / Analysis

print("<===  random List and Its Values / Analysis ===>")

random_num = random.sample(range(1 , 100) , 5)

print(random_num)

print("Random list: " , random_num)

print("Random Number Max count: " , max(random_num))
print("Random Number Min count: " , min(random_num))
print("Random Number sum count: " , sum(random_num))


# Part:4 Sort and Reverse a List

print("<=== sort and Reverse a List ===>")

user_list = list(map(int , input("Enter Number seperated by space : ").split()))

print(user_list)

print("Sorted List Ascending" , sorted(user_list))

print("Reverse value of list : " , list(reversed(user_list)))