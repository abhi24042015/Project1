l1=[1,2,3]
print(l1)
l1.append(4)
print(l1)

l2=["John","Smith"]
print(l2)

print(l1+l2)

l3=l1+l2
print(l3)
# [1, 2, 3, 4, 'John', 'Smith']

l4=l2*3
print(l4)
print(l1[2])
# 3

s="Hello"
s = s+"World"
print(s)

print(s*3)
# 'HelloWorldHelloWorldHelloWorld'
t1=(1,2,3)
# t1.append(4)

t1 = t1 + (3,4)
print(t1)
# (1, 2, 3, 3, 4)
print(t1[2])
# 3

empId={101,102,101,104,110} 

print(empId)

empId.add(108)
print(empId)

# {101, 102, 104, 108, 110}

emp={"ecode":101,"ename":"John","esal":1000}
print(emp)
# {'ecode': 101, 'ename': 'John', 'esal': 1000}

print(emp['ecode'])
# 101

# empId[1]

print(emp['ename'])
# 'John'

