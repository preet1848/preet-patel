#  break statement in python 

# for i in range(1 , 6):
#    if i == 4:
#       break
#    print("for loop : " , i)

# continue statement in python 

# for i in range(1 , 6):
#     if i == 4: 
#         continue
#     print("For loop : " , i)

# break and continue in nested loop

# for i in range(1 , 4):
#     for R  in range(1 , 2):
#         if R == 2:
#             break
#         print("R loop: ", R)
#     print("i loop: " , i)

# for i in range(1 , 4):
#     print("i loop: " , i)
#     for R in range(2):
#         if i == 2:
#             break
#         print("R loop: " , R)


# pattern print in python 

# for i in range(1 , 7):
#     for S in range(1 , i):  
#         print(f"{S}" , end="")
#     print()

# pattern 2

# for i in range(6):
#     for S in range(i , -1 , -1):  
#         print(f"{S+1}" , end="")
#     print()

# pattern 3

# for i in range(1 , 7):
#     for S in range(i):  
#         print(f"{i}" , end="")
#     print()

# pattern 4 

# for i in range(5):
#     for S in range(i+1):  
#         print(f"{5-i}" , end="")
#     print()


# pattern 5

# for i in range(5):
#     for S in range(i , -1 , -1):  
#         print(f"{5-S}" , end="")
#     print()


# pattern 6


for i in range(5):
    for S in range(i+1):  
        print(f"{5-S}" , end="")
    print()

