# class SumClass:
#     def sum(self,a,b):
#         print("sum =",a+b)
#     def sum(self,a,b,c):
#         print("sum =",a+b+c)
# obj=SumClass()

# obj.sum(20,11)
# obj.sum(19,20,21)

class SumClass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print("Two nos")
            print("sum=",a+b)
        elif a!=None and b!=None and c!=None:
            print("Three nos")
            print("sum=",a+b+c)
        else:
            print("more")
obj=SumClass()

obj.sum(20,11)
obj.sum(19,20,21)