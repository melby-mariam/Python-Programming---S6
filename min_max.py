# list=[]
# num=int(input("Enter no.of elements:"))
# for i in range(num):
#     a=input()
#     list.append(a)



# def min_max(list2):
#     return min(list2), max(list2)
   

# list1=list(map(int,input("Enter elemnts:").split()))
# # list2=input("enter elements:").split()
# min,max=min_max(list1)

# print("Smallest is",min)
# print("Largest is",max)

# list1=list(map(int,input("Enter elements:").split()))
# pos=[]
# neg=[]
# for i in list1:
#     if i>=0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f"Positive list is {pos}\nNegative list is {neg}")

dict1={}
lim=int(input("Enter the no.of person:"))
for i  in range(lim):
    name=input("Enter name:")
    dict1[name]=input("Enter DOB")
print(dict1)
name=input("Enter a name to check:")
if name in dict1:
    print(dict1[name])
    



