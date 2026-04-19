name="John"
sal=100
print("The Emp "+ name + " earns sal "+ str(sal))
print("List:")
l1=list(input("Enter the list elements:"))
print(l1)
age=int(input("Enter your age John:"))
to_retire=65-age
print("John can retire post ",to_retire,"years")

x=11
y=5
z=x+y
print(x,"+",y,"=",z)
z=x-y
print(x,"-",y,"=",z)
z=x-y
print(x,"-",y,"=",z)
z=x*y
print(x,"*",y,"=",z)
z=x/y
print(x,"/",y,"=",z)
z=x//y
print(x,"//",y,"=",z)
z=x**y
print(x,"**",y,"=",z)

z=x
x+=y
print(z,"+=",y,"=",x)

x = 11
y = 5
z = x > y
print(x,">",y,"is",z)
z = x < y
print(x,"<",y,"is",z)
z = x >= y
print(x,">=",y,"is",z)
z = x < y
print(x,"<",y,"is",z)
z = (x == y)
print(x,"==",y,"is",z)
z = x > y or x > 9
print(x,">",y,"or",x,">",9,"is",z)
z = x > y and x > 9
print(x,">",y,"and",x,">",9,"is",z)
l1=[1,2,3,4,5,6]
z = 4 in l1
print(4, "is a member of",l1,"is",z)
z = 4 not in l1
print(4, "is not a member of",l1,"is",z)

def add(x,y):
    """This is a function to add 2 numbers"""
    # first number is x 
    """The second
    number is y"""
    return x+y
x=int(input("Enter x:"))
y=int(input("Enter y:"))
print("The function returns: ",add(x,y))
print("The documentation of add() is")
print(add.__doc__)