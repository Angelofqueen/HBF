import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from HBF64 import menu

    menu()

elif bit == '32bit':

    from HBF32 import menu

    menu()
