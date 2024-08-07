import pandas as pd

my_dict = {
    'Reg. No.' : ["ABC123","ECH265","FET345","GMT734"],
    'Name': ["Ganesh Kumar","John Mathew","Reena K","Adil M"],
    'Semester' : ["S8","S7","S6","S5"],
    'College' : ["ABC","ECH","FET","GMT"],
    'CGPA' : [9.8,9.9,9.7,9.75]}

df=pd.DataFrame(my_dict)
# df.align()
df.to_csv("result.csv",index=False)
print(df)