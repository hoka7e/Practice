a = "Hello" #Assigning a string 
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" # multiline string
print (a)

for x in "programming principles ":
  print(x) # Loop through the letters in the word "programming principles"

#sliing strings
b = "Hello, World!"
print(b[2:5]) # Get the characters from position 2 to position 5 (not included)

#modify strings
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#f-string
age = 18
txt = f"Hello , I am {age}"
print (txt)