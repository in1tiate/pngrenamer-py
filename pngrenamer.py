import os
import sys

dirname = "bins"

os.chdir(dirname)

for filename in os.listdir("."):
    print("Working on file: " + filename + "...")
    file = open(filename, "rb") # open in read-only binary mode
    header = file.read(4)
    # print(header)
    file.close()
    if header == b"\x89PNG":
        print("It's a PNG!")
        os.rename(filename, filename + ".png")
    else:
        print("Not a PNG.")
        
    