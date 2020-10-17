#! /bin/bash -x

sudo dpkg --add-architecture i386 
sudo apt update 
sudo apt install apt-utils libc6:i386 libncurses5:i386 libstdc++6:i386 g++-multilib libgtk2.0-0:i386 dpkg-dev:i386 libxtst6:i386 default-jre unzip net-tools libtext-csv-perl libcanberra-gtk-module libcanberra-gtk3-module lsb-core opencl-headers ocl-icd-opencl-dev ocl-icd-libopencl1 wget -y 
sudo apt install tofrodos iproute2 gawk make net-tools locales cpio libncurses5-dev libssl-dev flex bison libselinux1 gnupg wget diffstat chrpath socat xterm autoconf libtool tar unzip texinfo zlib1g-dev gcc-multilib build-essential libsdl1.2-dev libglib2.0-dev screen pax gzip xvfb tftpd tftp libtool-bin default-jre -y lsb-release zlib1g:i386 git python-dev 
sudo locale-gen en_US.UTF-8 
#sudo ln -s /usr/bin/make /usr/bin/gmake

# ends here.
