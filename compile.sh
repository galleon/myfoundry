#/bin/bash
cd /home/shared
cmake -DINSTALL_LIB_DIR=lib/x86_64-linux-gnu -DCMAKE_INSTALL_PREFIX=$(pwd)
make -j8 install clean
