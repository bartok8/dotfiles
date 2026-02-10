#! /bin/bash -x

source ~/.local/bin/myenv/bin/activate
cd u_2021_01
./bs.sh
cd ..
python lucky.py

# ends here.

