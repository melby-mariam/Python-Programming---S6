# def divide(x,y):
#     try:
#         result=x//y
#         print("Result is",result)
#     # except ZeroDivisionError:
#         # print("Cant divide by 0")

#     except Exception as e:
#         print("The error is",e)
        
# divide(3,"CSE")
# divide(3,0)

def divide(x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print("Division by zero not possible")
    else:
        print("Yeah! Your result is ",result)
    finally:
        print("I am always executed!")
divide(3,0)
divide(3,2)
