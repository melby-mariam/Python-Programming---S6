import matplotlib.pyplot as plt

years=[1903,1920,1930,1940,1950]
home=[22,33,42,51,60]
city=[12,31,56,78,81]

plt.plot(years,home,color='r-o',label='this is red')
plt.plot(years,city,'b-X',label='this is blue')

plt.xlabel('years')
plt.ylabel('home vs city',rotation=90)
# plt.xticks()
# plt.yticks()
plt.title('my line plot',color="red",size=14,y=-0.3,loc="center")
plt.legend()
plt.show()