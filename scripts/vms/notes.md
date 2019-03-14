\_SB_.PCI0.PEG0.PEGP


# REMOVE gpu from pci devices
echo 1 > /sys/bus/pci/devices/0000\:01\:00.0/remove

# Unbind gpu
echo "0000:01:00.0" > "/sys/bus/pci/drivers/vfio-pci/0000:01:00.0/driver/unbind

# POWER OFF GPU
echo "\_SB_.PCI0.PEG0.PEGP._OFF" > /proc/acpi/call

# RESCAN pci devices (not working for gpu)
echo 1 > /sys/bus/pci/rescan

# List graphic provides
xrandr --listproviders

DRI_PRIME=0 glxinfo | grep "OpenGL vendor string"
DRI_PRIME=1 glxinfo | grep "OpenGL vendor string"


# extract rpm
rpm2cpio your-rpm | cpio -idmv

# GET GPU info
lspci -nnk -s 01:00.0

# List files in packages
dnf repoquery -l your-package-name

# REBUID grub config
grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg

# REBUILD initram
dracut -f --kver `uname -r`

# Create TAP interface
tunctl -p -t qemu_w10tap0