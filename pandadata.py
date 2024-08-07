import pandas as pd

my_dict = {
'NAME' : ["a","b","c","d","e","f","g"],
'AGE': [20,27,35,55,18,21,35],
'DESIGNATION':["VP","CEO","CFO","VP","VP","CEO","MD"]
}
# df=pd.DataFrame(my_dict,index=[1,2,3,4,5,6,7])
df=pd.DataFrame(my_dict)
df.to_csv('txt.csv',index=False)
# print(df)
# emp=pd.read_csv('txt.csv',index_col=0)
# print(emp.head())
usecols=['NAME','AGE']
emp=pd.read_csv('txt.csv',index_col=0,usecols=usecols)
print(emp.tail())