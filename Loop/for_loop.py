fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry

string = "banana"
for char in string:
    print(char)
# b
# a
# n
# a
# n
# a

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
# apple

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
# apple
# cherry

fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)
else:
    print("Finally Finished!")
# apple
# banana
# cherry
# Finally Finished!

adjectives = ["small", "big"]
fruits = ["apple", "banana", "cherry"]
for adjective in adjectives:
    for fruit in fruits:
        print(adjective, fruit)
# small apple
# small banana
# small cherry
# big apple
# big banana
# big cherry
