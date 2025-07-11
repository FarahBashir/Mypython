# loops are used to repeatedly execute a block of code

# for loop is used to repeat something a fixed number of times
 

# num = 50
for num in range(20,31):
    print(num)

for x in range(-30,-20):
    print(x)

colors = ["red", "blue", "oragne", "green"]
for color in colors:
    print(color)
    
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

    # while loop runs as long as a condition is true
# Example 1
    x = 2                    # Begins with x = 2.
while x < 7:                    # Checks x < 7: if true, enters loop
    print(x)                    # Prints the current x, then increments.
    x += 1                      # Stops once x reaches 7

#Example 2

batch = 2               # batch starts at 2.
while batch <=6:        #Is batch <= 6? (2 <= 6) → True, so enter loop.
  print("Python")       #Inside loop:  Prints "Python".
  batch += 1            # Executes batch += 1, so now batch becomes 3.
#   Once batch increments to 7, the condition (7 <= 6) is False, so the loop ends.

#  Nested loop is A loop inside another loop.
#Example 1

for i in range(2):       #0, 1
    for j in range(3):   # 0, 1, 2
        print(f"i = {i}, j = {j}")

#Example 2

        for v in range(1, 4):   # 1, 2, 3
         for w in range(3):    # 0, 1, 2
             print(f"v = {v}, w = {w}")

#  Break and continue in Loops
# break is Used to stop the loop completely when a condition is met and loop stops
#Example 1 

for t in range(5):
    if t == 3:
        break
    print(t)

#Example 2

items = ("pencil", "eraser", "sharperner", "book", "bag")
for item in items:
    if item == "book":
        break
    print(item)

# Using continue
# continue is used to skip the current loop step and move to the next one

#Example 1

for i in range(1, 6):       # 1, 2, 3, 4, 5
    if i ==3:               # This loop will skip when i is 3
        continue
    print(i)

#Example 2

for item in items:
    if item == "sharperner":
        continue
    print(item)