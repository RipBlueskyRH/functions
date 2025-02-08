def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

num1=int(input("enter a number: "))
num2=int(input("enter a second number: "))
print("select the operation")
print("a for addition, b for subtraction, c for multiplication, and d for dividion")
choice=str(input("enter a, b, c, or d: "))
if choice=="a":
    print("the sum is", addition (num1,num2))
elif choice=="b":
    print("the difference is", subtraction (num1,num2))
elif choice=="c":
    print("the product is", multiplication (num1,num2))
elif choice=="d":
    print("the quotient is", division (num1,num2))
else:
    print("invalid input")


