import os
import sys

for file_path in sorted(os.listdir("./packages")):
    if len(sys.argv) > 1 and sys.argv[1] == "--debug":
        print("~~~Loaded file: ", file_path)
    with open("./packages/" + file_path) as file:
        for line in file.readlines():
            if len(sys.argv) > 1 and sys.argv[1] == "--debug":
                print("~~~Reading line: ", line)
            parts = [part.strip() for part in line.split(":")]
            if len(sys.argv) > 1 and sys.argv[1] == "--debug":
                print("~~~Line parts: ", parts)
            choice = ""
            while not (choice == "y" or choice == "n"):
                choice = input("~~~Install: " + parts[0] + "? (y/n) ")
            if choice == "n":
                continue
            os.system("echo y | sudo pacman -S " + parts[0])
            if len(parts) > 1:
                os.system(parts[1])
