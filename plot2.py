import pandas as pd
import matplotlib.pyplot as plt

my_dict ={
    'name' : [1,2,3],
    'age' : [4,5,6]
}
df1=pd.DataFrame(my_dict)
df1.to_csv('data.csv')
df=pd.read_csv('data.csv')
# df.plot()
# df.plot(kind='scatter',x='name',y='age')
# df["name"].plot(kind='hist')
df.plot(kind='bar',x='name',y='age')

plt.show()
