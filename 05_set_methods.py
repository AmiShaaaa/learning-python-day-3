# Creating a set
b=set()
b.add(4)
b.add(5)
b.add(9)
b.add(9) # adding a value repeatedly doesn't change a set
print(b)

# b.ad([4,5,6]) : Will throw error bcz lists can't be added to set
# b.ad([4:5]) : Will throw error bcz dictionaries can't be added to set
# items in sets can't be changed

print(len(b)) # prints the length of the set
print(b)

b.remove(9) # Removes 5 from set b
# b.remove(15) # Throws error
print(b)

print(b.pop())
print(b)

