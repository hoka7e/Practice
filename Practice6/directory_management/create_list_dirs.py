import os
import shutil

#
nested_dir = "parent/child/grandchild"
os.makedirs(nested_dir, exist_ok=True)  
print(f"Nested directories created: {nested_dir}\n")

for root, dirs, files in os.walk("parent"):
    print("Current folder:", root)
    for d in dirs:
        print("  Folder:", d)
    for f in files:
        print("  File:", f)
    
    print()
#
file_names = ["file1.txt", "file2.txt", "image.png", "notes.md"]
for f in file_names:
    with open(os.path.join("parent", f), "w") as file:
        file.write(f"This is {f}\n")


txt_files = [f for f in os.listdir("parent") if f.endswith(".txt")]
print("Text files in 'parent':", txt_files, "\n")


#
dest_dir = "parent/destination"
os.makedirs(dest_dir, exist_ok=True)


for f in txt_files:
    shutil.copy("parent/" + f, dest_dir)
print("TXT files copied.")


shutil.move("parent/notes.md", dest_dir)
print("notes.md moved.")