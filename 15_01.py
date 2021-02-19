""" set operations """
z = {1,2,3,3,2,1,2,3}
print(z)
x = {1,2,3}
y ={4,5,6,2,3}
print(x|y) # Union
print(x&y) # Intersection
print(x-y) # remove y duplicte elements
print(y-x) # remove x duplicte elements
y ={4,5,6,2,3}
y.add(7)
print(y)
y.remove(7)
print(y)
y.pop() #pops first element
print(y)

