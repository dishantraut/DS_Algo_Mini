""" Dict Operations """
a = {"key1":1,"key1":3,"key1":5}
print(a)
f = {"Father":43,"Mother":38,"Sister":19,"Brother":23}
print(f.keys())
print(f.values())
print(f.items())
print(f.get("Mother"))
print(f.get("Uncle","Did not find")) # specifiy our mesage
print(f.setdefault("Uncle",48))
print(f)
print(f.pop("Uncle"))
print(f)
f["Uncle"] = 43
print(f)

