str='Hi Hello'
dict={}
for i in str.lower():
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
