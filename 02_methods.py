myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "harks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'},
     1:2
}
print(list(myDict.keys()))
print(list(myDict.values()))
print(list(myDict.items()))

updateDict={
    "friend":"ayush"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("amy"))
print(myDict["amy"])
