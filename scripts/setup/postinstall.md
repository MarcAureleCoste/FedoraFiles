# Post installation

## Base X
```sh
dnf install @base-x
```

## RPM FUSION
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

sudo dnf update

## Install packages
```sh
sudo dnf install \
    alsa-lib \
    alsa-utils \
    bluez-tools \
    bzip2 \
    compton \
    dbus-glib \
    feh \
    flatpak \
    fontconfig-devel \
    freetype-devel \
    fuse-exfat \
    gcc \
    git \
    gtk3 \
    htop \
    lbzip2 \
    libicu \
    libX11-devel \
    libXft-devel \
    libXrandr-devel \
    libXScrnSaver \
    mlocate \
    network-manager-applet \
    nss \
    ntfs-3g \
    p7zip \
    pciutils \
    pkgconf-pkg-conf \
    pulseaudio \
    pulseaudio-module-bluetooth \
    qtile \
    ranger \
    scrot \
    slock \
    tar \
    udisks2 \
    wget \
    xorg-x11-proto-devel \
```

## GOOGLE CHROME
Go to `https://www.google.com/chrome/`

## Flathub
```sh
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

## Applications folder
cd ~
mkdir applications
cd applications
wget "https://download.mozilla.org/?product=firefox-devedition-latest-ssl&os=linux64&lang=en-US" -O /tmp/ff.tar.bz2
tar xf /tmp/ff.tar.bz2

wget "https://go.microsoft.com/fwlink/?LinkID=620884" -O /tmp/code.tar.gz
tar xf /tmp/code.tar.gz


## Worspace
```sh
cd ~ && mkdir workspace && cd workspace
mkdir blog
```

### ST
```sh
mkdir suckless && cd suckless
git clone https://git.suckless.org/st
```

### QEMU
```sh
dnf install SDL2-devel \
    libjpeg-turbo-devel \
    glib2-devel \
    pixman-devel \
    mesa-libgbm-devel \
    libepoxy-devel \
    spice-server-devel \
    spice-protocol \
    libusb-devel \
git clone git clone https://github.com/saveriomiroddi/qemu-pinning.git qemu
cd qemu
git checkout v3.0.0-pinning

./configure --prefix=/home/cmarc/usr \
    --enable-kvm \
    --disable-xen \
    --enable-sdl \
    --enable-vnc \
    --enable-vnc-jpeg \
    --enable-opengl \
    --enable-libusb \
    --enable-vhost-net \
    --enable-spice \
    --target-list=x86_64-softmmu
make -j8
make install
```
