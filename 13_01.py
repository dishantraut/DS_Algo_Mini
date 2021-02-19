""" List Operations """
z = [1,12,33,4,5,5]
print(z)
z.sort(reverse=True)
print(z)
print(z.count(5))
z = ["C","c","a","A","b","B"]
z.sort()
print(z)
z.sort(reverse=True)
print(z)
z.sort(key=str.lower)
print(z)
z = [1,12,33,4,5,5]
z.reverse()
print(z)
z.append("and so on")
z.append([33,22,11])
print(z)
z = [1,12,33,4,5,5]
z.extend("and so on")
z.extend([33,22,11])
print(z)
a = "hey yoo man"
b = "hello world"
z = a.join(b.split())
print(z)
b = [1,2,3]
print(2 in b)
print(5 not in b)
z = [1,12,33,4,5,5]
z[:2] = ["one","two"]
print(z)
z[2:4] = [0,0]
print(z)
z[2:4] = []
print(z)
del z
print(z)
