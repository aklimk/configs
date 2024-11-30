import os

for file_path in os.listdir("./packages"):
    with open("./packages/" + file_path) as file:
        for line in file.readlines():
            parts = [part.strip() for part in line.split(":")]
            os.system("sudo pacman -S " + parts[0])
            if len(parts) > 1:
                os.system(parts[1])
