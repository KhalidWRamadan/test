#Question 1

# list = input("Enter Text : ")
# a = 0
# for i in list:
#     a += 1
# print(a)



#Question 2

# a,b,c = int(input("Enter First Num : ")) , int(input("Enter Second Num : ")) , int(input("Enter Third Num : "))
#
# if a == b == c:
#     print("DUPLICATES <- A = B = C")
# elif a == b:
#     print("DUPLICATES <- A = B")
# elif a == c:
#     print("DUPLICATES <- A = C")
# elif b == c:
#     print("DUPLICATES <- B = C")
# else: print("ALL UNIQUE")









#Question 3


# a,b,c = int(input("Enter First Num : ")) , int(input("Enter Second Num : ")) , int(input("Enter Third Num : "))
#
#
# if a == b == c :
#     print("All values are equal")
# else:
#     if a < b:
#         if a == c:
#             print("A & C are the smallest")
#         elif a < c:
#             print("A is the smallest num")
#         else:
#             print("C is the smallest")
#     elif a > b:
#         if b == c:
#             print("B & C are the smallest")
#         elif b < c:
#             print("B is the smallest num")
#         else:
#             print("C is the smallest")
#     elif a == b:
#         print("A & B is the smallest num")
#




# Question 4
# positive = 0
# negative = 0
# count = 0
# sum = 0
#
# while True:
#     value = int(input("Enter number : "))
#     if value != 0:
#         count += 1
#     sum = sum + value
#     avg = sum / count
#     if value >0:
#         positive +=1
#     elif value < 0:
#         negative +=1
#     else: break
#
# print("Number of positive values is : ",positive)
# print("Number of negative values is : ",negative)
# print("The total of values is : ", sum)
# print("The average of the values : ",avg)




