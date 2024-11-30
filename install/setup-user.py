import os
import sys

choice = input("~~~~ Install vim? (y/n) ")
if choice == "y":
    os.system("echo y | pacman -S vim")

username = input("~~~~ Choose a username ")
os.system("useradd -m " + username)
os.system("passwd " + username)

print("~~~~ Installing sudo")
choice = input("~~~~ Install sudo? (y/n) ")
if choice == "y":
    os.system("echo y | pacman -S sudo")
    os.system("EDITOR=vim visudo")
    os.system("exit")
