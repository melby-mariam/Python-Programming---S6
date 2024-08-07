import pandas as pd

my_dict = {
    'Reg no' : [10001,10002,10003],
    'Name' : ["Jack","John","Alex"],
    'Sub_Mark1' : [76,77,74],
    'Sub_Mark2' : [88,84,79],
    'Sub_Mark3' : [76,79,81]}

df=pd.DataFrame(my_dict)
df.to_csv("pyq.csv",index=False)
print(df)