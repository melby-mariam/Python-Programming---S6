# for n in range(2,1000) :
#     i=2
#     while i<=n/2:
#         if n%i==0:
#             break
#         i=i+1
#     else:
#         print(n,end=' ')
# import math
# x1,y1=map(int,input("Enter 1st coordinates:").split())
# x2,y2=map(int,input("Enter 2nd coordinates:").split())
# print('Distance is',math.sqrt((x2-x1)**2+(y2-y1)**2))

n=int(input("Enter number:"))
for i in range(0,n+1):
    for j in range(0,i):
        print(j+1,end=' ')
    print()