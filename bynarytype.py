# binary type bytes

list1 = [1,2,3,4,5,6,121,244]
x = bytes(list1)
print(type(x))
print(list1)

# binary type bytearray

list2 = [2,4,34,56,123]

y = bytearray(list2)
print(y)
y[1] = 20
print(y[1] )