import os
import shutil

dest_dir = "parent/destination"
os.makedirs(dest_dir, exist_ok=True)

for f in txt_files:
    shutil.copy("parent/" + f, dest_dir)

print("TXT files copied.")

shutil.move("parent/notes.md", dest_dir)

print("notes.md moved.")