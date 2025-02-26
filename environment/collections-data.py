#lists
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(f"List item at index zero is: {myFruitList[0]}")
print(f"List item at index one is: {myFruitList[1]}")
print(f"List item at index two is: {myFruitList[2]}")


#Accessing a list item by index
print(myFruitList[0])
print(f"Before altering the list: {myFruitList[2]}")

myFruitList[2] = "orange"
print(f"After altering the list values: {myFruitList[2]}")
print(myFruitList)

#tuples
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple by position

print(f"Tuple item at index two is: {myFinalAnswerTuple[0]}")
print(f"Tuple item at index two is: {myFinalAnswerTuple[1]}")
print(f"Tuple item at index two is: {myFinalAnswerTuple[2]}")

# Dictionaries
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])