import os

if os.path.isfile("/sys/firmware/efi/fw_platform_size"):
    EFI=True
else:
    EFI=False
print("EFI:", EFI)

os.system("ip link")
temp = input("network type? ")
if temp == "wifi":
    os.system("iwctl")
elif temp == "mobile":
    os.system("mmcli")
os.system("ping -c 1 archlinux.org")

os.system("timedatectl")

os.system("fdisk -l")
while True:
    temp = input("device")
    os.system("fdisk " + temp)
    if input("continue? ") == "n":
        break
while True:
    temp = input("fs type ")
    temp2 = input("partition ")
    if input("continue? ") == "n":
        break

os.system("pacstrap -K /mnt base linux linux-firmware")

os.system("genfstab -U /mnt >> /mnt/etc/fstab")

os.system("arch-chroot /mnt")

os.system("pacman -S vim")

temp = input("Region ")
temp2 = input("City ")
os.system("ln -sf /usr/share/zoneinfo/{}/{} /etc/localtime".format(temp1, temp2))

os.system("hwclock --systohc")

os.system("vim /etc/locale.gen")
os.system("locale-gen")
os.system("vim /etc/locale.conf")

temp = input("Hostname ")
os.system("cat {} > /etc/hostname".format(temp))

os.system("passwd")

os.system("grub")

if EFI:
    pass
else:
    pass

temp = input("username of user ")
os.system("useradd -m " + temp)
os.system("passwd " + temp)
os.system("sudo")
os.system("EDITOR=vim visudo")

print("Configuration done, please reboot to user account and then continue.")
