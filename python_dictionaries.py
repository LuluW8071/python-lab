dict={
    "firstletter":"A",
    "midletter":"P",
    "endletter":"z",
    "pages":1000
}
print(dict)

print(dict["midletter"])

print(len(dict))

print(type(dict))

dict["pages"]=2000
print(dict)

if "P" in  dict["midletter"]:
    print("P exists")