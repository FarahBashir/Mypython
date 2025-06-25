# String
#sequence of characters enclosed in
# single or double quotes

print("Examples of strings operations")
#  String concatenation
#Joining two or more strings to make one string
print("Examples of string concatenation")
# Example 1
greetings = "Hello"
name = 'Farah!'
course = "Python"
batch= 'Batch2'

name_greetings = (greetings + " "+ name)
Class = (course+ " "+ batch)

print(name_greetings)
print(Class)

# Example 2
make = "Honda"
model= "Civic"
year = "2023"
statement= ("I own a")
My_car = (make + " " + model + " " + year)
print(statement + " " + My_car)

# String repetition
# saying something again and again
print("Examples of String repetition")

#Example 1
song = "LaLa"
print(song * 5)
#Example 2
Design = "*"
design_output = (Design * 10)
print(design_output)

#Length
#count how many letters or characters are in a string
print("Length example")
word = "notebook"
print(word, len(word))
compliment = "You are kind."
print(compliment, len(compliment))

#picking a letter by its spot (Indexing)

print("indexing example")
print(word[0])  #printing the very first letter
print(word[5])  #printing the 6th letter
print(word[-1]) #printig the last letter
print(word[-2])  #printing the second last letter

#cutting out a peice (Slicing)
print("slicing example")
print(word[0:3]) #print from 0 to 2 
print(word[4:])  #print from 4 to end
print(word[-4:0])

#Change a letter, by making it capital or small
print(word.upper())  #All capital
print(word.lower())  #All lowercase
print(word.capitalize()) #capitalizes only the first letter

#Check if something is inside the string (Membership)
print("t" in word)  #letter t is present in the the word so it is true
print("p" in word)   #letter p is not in the word so it is false

#Change a word or letter (Replace)
annoucement = "I am going to Turkey."
new_annoucement = (annoucement.replace("Turkey", "Spain"))  #find 'Turkey' and replace it with 'Spain'
print(annoucement)
print(new_annoucement)

#Break a sentence into words (split)
#turn a string into a list
trip = new_annoucement.split()
print(trip)
sentence = "This", "is", "my", "last", "sentence."
print(sentence)
result = " ".join(sentence)
print(result)