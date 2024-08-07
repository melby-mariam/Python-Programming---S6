import pandas as pd
import matplotlib.pyplot as plt

my_dict = {
'NAME' : [6,5,7,8,9,55],
'AGE': [20,27,35,55,18,21],
'DESIGNATION':[1,2,3,55,66,88]
}
# df=pd.DataFrame(my_dict,index=[1,2,3,4,5,6,7])
df=pd.DataFrame(my_dict)
df.to_csv('txt.csv',index=False)

emp=pd.read_csv('txt.csv')
# print(emp)
# emp.plot(kind='scatter',x = 'Duration', y = 'Calories')
# emp["Duration"].plot(kind='hist')
emp.plot(kind='bar',x='name',y='age')
plt.show()