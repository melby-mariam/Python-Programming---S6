import numpy as np
arr1=np.random.randint(0,20,(3,3))
arr2=np.random.randint(0,20,(3,3))
madd=np.add(arr1,arr2)
print("After matrix addition:\n",madd)
mmul=np.dot(arr1,arr2)
print("After matrix multiplication:\n",mmul)
print("Transpose of addition matrix:\n",np.transpose(madd))
print("Transpose of multiplication :\n",np.transpose(mmul))

