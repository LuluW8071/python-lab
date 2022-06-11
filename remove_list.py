from subprocess import list2cmdline


list=["red","green","crimson","tree"]
list.remove("red")
print(list)

#pop with index
list=["red","green","crimson","tree"]
list.pop(2)
print(list)

#removes all item directly
list=["red","green","crimson","tree"]
list.pop()
print(list)

#clear() list
list=["red","green","crimson","tree"]
list.clear()
print(list)