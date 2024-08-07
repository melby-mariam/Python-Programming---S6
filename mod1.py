# num=int(input("Enter a no."))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# num=int(input("Enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("Factorial is",+fact)

# n=int(input())
# i=1
# while i<=n:
#     print("Square of",i,":",i**2)
#     print("Cube of",i,":",i**3)
#     i=i+1

# sqroot and cuberoot
# import math
# n=int(input())
# squareroot = math.sqrt(n)
# cuberoot = n ** (1/3)
# print(f"Square root of {n} is {squareroot}")
# print("cube root of",n,"is",cuberoot)

# reverse of no
# n=int(input())
# number_str = str(n)
# rev_str = number_str[::-1]
# rev_number = int(rev_str)
# print(f"Reverse of {n} is {rev_number}")

# sum of digits
# n=int(input())
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(f"Sum of is {sum}")

# prime less than 1000
# for n in range(2, 1000):
#     prime = True
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             prime = False
#             break
#     if prime:
#         print(n, 'is prime')

# reverse a string
# str1=input()
# str2=str1[::-1]
# print(f"Reverse of {str1} is {str2}")

# each char count
# n=input()
# freq=input()
# for letter in n:
#     freq=freq+1
# else:
#     freq=1
# print(f"Count of {letter} is {freq}")

# import math
# x1,y1=map(int,input('Enter the 1st Coordinates : ').split())
# x2,y2=map(int,input('Enter the 2nd Coordinates : ').split())
# print('Distance = ',math.sqrt((x2-x1)**2+(y2-y1)**2))

# to upprt
# n=input()
# string_upper=n.upper()
# print(f"Uppercase of {n} is {string_upper}")

# sort a list of number
n=input().split()
numbers=[]
for num in n:
    numbers.append(int(num))
numbers.sort()
print("Sorted numbers are:",numbers)

n1=len(numbers)
if n1%2 ==0:
    median= (numbers[n1//2]+numbers[n1//2+1])/2
else:
    median= numbers[(n1+1)/2]
print("median is:",median)