import matplotlib.pyplot as plt
import numpy as np

x=np.array(["S","A+","A","B+"])
y=np.array([5,10,15,20])

# x=['A','B','C','D']
# y=[2,5,7,8]

plt.title("python")
plt.xlabel("grade")
plt.ylabel("students")

plt.bar(x,y,color="red")
# plt.barh(x,y,color="red")
# plt.xlabel("students")
# plt.ylabel("grades")
plt.show()