import os
import shutil
source = "sample.txt"
destination = "newfile.txt"
shutil.copy(source, destination)
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print(f"{"sample.txt"} deleted successfully.")
else:
    print(f"{"sample.txt"} does not exist.")
