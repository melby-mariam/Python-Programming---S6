# string1="Python rules!"
# # list1=string1.split()
# # list1=string1.upper()
# # list1=string1.find("rules")
# list1=string1.replace("!","?")
# print(list1)

# fp=open("myfile.txt","r")
# file1=fp.read()
# splited=file1.split()
# count=0
# for i in splited:
#     if len(i) == 4:
#         count+=1
# print(count)

fp=open("numbers.txt","r")
file1=fp.read()
tolist=list(map(int,file1.split()))
tolist.sort()
length=len(tolist)
if length%2==0:
    print("Medians are:",tolist[length//2],tolist[(length//2)+1])
else:
    print("Median is:",tolist[length//2])
fp.close()


