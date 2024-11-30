import os

for file_path in os.listdir("./packages"):
    with open("./packages/" + file_path) as file:
        for line in file.readlines():
            parts = [part.strip() for part in line.split(":")]
            choice = ""
            while not (choice == "y" or choice == "n"):
                input("Install: " + parts[0] + " ")
            if choice == "n":
                continue
            os.system("y | sudo pacman -S " + parts[0])
            if len(parts) > 1:
                os.system(parts[1])
