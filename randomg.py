import numpy as np
# random_number=np.random.rand()
# print(random_number)

# integer=np.random.randint(0,10,(3,4))
# print(integer)
# array1=np.array([2,3,4,5,6,9])
# random_choice=np.random.choice(array1)
# print(random_choice)

arr1=np.arange(6).reshape((3,2))
arr2=np.arange(6).reshape((3,2))
arr3=arr1+arr2[0].reshape((1,2))
print(arr3)
