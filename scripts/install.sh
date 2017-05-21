#!/bin/bash

# to get the motors working
apt-get install python3 python3-pygame python3-dev python3-rpi.gpio

# servoblaster
apt-get install git
git clone https://github.com/richardghirst/PiBits.git
cd PiBits/ServoBlaster/user
sudo make install
# if compilation fails, go take a look at https://github.com/richardghirst/PiBits/issues/84
