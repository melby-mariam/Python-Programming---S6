import pandas as pd

my_dict = {
'Name' : ['Nikhil','Sanchit','Aditya','Sagar'],
'Branch' : ['CSE','CSE','IT','IT'],
'Year' : [2,2,2,1],
'CGPA' : [8.0,9.1,9.3,9.5],
}
df=pd.DataFrame(my_dict)
df.to_csv("student.csv",index=False)
print(df)