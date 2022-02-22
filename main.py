

li = [1, 3, 5, ["new data", 12]]
li.insert(3, "new")
print(li)
st = str(li)
st = st[:-6] + "new data"
print(st)