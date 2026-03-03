f = open("newfile.txt", "x")
with open ("newfile.txt","a") as ss:
    f.write("This is an appended line.\n")
    f.write("Another new line.\n")
    
with open("newfile.txt","r") as f:
  print(f.read())