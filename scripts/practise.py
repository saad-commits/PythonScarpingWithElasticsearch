# nums=['saad','maaz','saadada','efgvyqiu']
# # nums_tuple=('saad','maaz')
# # nums_set = set(["Geeks", "For", "Geeks"]) 
# # print(nums)
# # print(nums_tuple)
# # print(nums_set)

# for num in nums:
#     print(num)


# try:
#     a=4
#     b=4
#     c=a/b
# except ZeroDivisionError:
#     print("Cant divide by 0")
# finally:
#     print("hey all time")

# assert b!=4 ," b is 4 buddy , it shoudlnt be "

# temp="saad is engineer"
# temp2="saad"

# if temp2 != temp:
#     raise TypeError("both strings are different")

# my_variable1 = 20
# my_variable2 = "GeeksForGeeks"
# print(my_variable1)
# print(my_variable2)
# del my_variable1
# del my_variable2
# print(my_variable1)
# print(my_variable2)
# a=1 if 1>0 else 0

# list1 = list(map(int, input("Enter list").split()))
# print(list1)

x,y = [int(x) for x in input("Enter liost").split()]
print(x)
print(y)

with open('dummy.txt', 'w') as f:
          print("welcome",file=f)