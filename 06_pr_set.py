# --------Question 1-------- #
# create dictionary of hindi words with values as their english translation

myDict={
    "Pankha": "Fan",
    "Dabba": "Box",
    "Samajhdar": "Amisha"
}
print("Options are:", myDict.keys())
a=input("Enter the hindi word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is 
# not present in the dictionary
print("The meaning of your word is:", myDict.get(a))

# --------Question 2-------- #
# input eight numbers from the user and display all the unique numbers

# num1=int(input("Enter number 1\n"))
# num2=int(input("Enter number 2\n"))
# num3=int(input("Enter number 3\n"))
# num4=int(input("Enter number 4\n"))
# num5=int(input("Enter number 5\n"))
# num6=int(input("Enter number 6\n"))
# num7=int(input("Enter number 7\n"))
# num8=int(input("Enter number 8\n"))

# s={num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)

# --------Question 3-------- #

# s={3,'3'} #both are different; one string one int
# print(s)

# --------Question 4-------- #

# s= set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s)
# ----or----
# s={20,20.0,'20'}
# print(s)
# print(len(s))

# --------Question 5-------- #
# run in console:
#     >>>s={}
#     >>>type(s)

# --------Question 6-------- #
# favLang = {}
# a = input("Enter your favorite language Shubham\n")
# b = input("Enter your favorite language Ankit\n")
# c = input("Enter your favorite language Sonali\n")
# d = input("Enter your favorite language Harshita\n")
# favLang['shubham'] = a
# favLang['ankit'] = b
# favLang['sonali'] = c
# favLang['harshita'] = d

# print(favLang)