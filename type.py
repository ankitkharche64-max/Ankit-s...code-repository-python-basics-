a = 2
t=type(a) #class<int>
print(t)

a = 2.4
t=type(a) #class<float>
print(t)

b = "2.4"
t=type(b) #class<string>
print(t)
print()


b = "2 "
c = float(b)
e = int(b)
t=type(c) #class<float>
print(t)
t=type(e) #class<int>
print(t)
print()

b = 24
c = float(b)
e = str(b)
t=type(c) #class<float>
print(t)
t=type(e) #class<string>
print(t)
print()

