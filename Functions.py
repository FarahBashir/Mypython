# A function is a reusable block of code that performs a specific task.
# You can call it (use it) whenever you need it, without writing the same code again.

#Example 1

def greet():          # greet is the funtion name
    print("Hello! Welcome to Python.")  # does not print through print
greet()                         #call the funtion to print

#Example 2

def say_hello(name):      #say hello is the funtion name
    print("Hello,", name)
   
say_hello("Metalearn")      #calling the funtion
say_hello("batch2")

# Parameter: A variable in the function definition
# Argument: The actual value passed to the function
# Example 3
def greet_user(name):  # 'name' is a parameter
    print("Hello,", name)

greet_user("Ali")  # "Ali" is an argument
greet_user("Ahmed")
greet_user("Sara")

def student_name(name1):      # 'name1' is a parameter
    print("Hello", name1, "Are you ready to learn?")

                            # Call the function with the argument "Aisha"
student_name("Aisha,")

#Example 4

def personal_greet(name, age):
    print("Hello", name + "!", "You are", age, "years old.")

personal_greet("Ali", 25)
personal_greet("Sara", 22)
personal_greet("Ahmed", 28)

# Value
# You can use the return keyword to return a value from a function.
# Example 1
def add(a, b):
    return a + b
                        # Using the result
result = add(7, 510)
print("The sum is:", result)

# Example 2
def sub(x,y):
  return y - x
result = sub(130, 280)
print("result = ", result)

#Example 3

def multiply(a, b):
    print("Result:", a * b)
multiply(4, 5)

