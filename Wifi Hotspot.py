#!/usr/bin/python3
#wifi Hotspot Enabler

import os
os.system('cls')
cmd = 0
while cmd != 3:
    print ('1-Enable Wifi Hotspot')
    print ('2-Stop Wifi Hotspot')
    print ('3-exit program')
    cmd = input ('Enter Your Choice (1,2,3)==>  ' )

    if cmd == '1':
        print ('Wifi Hotspot is Enable...')
        os.system ('netsh wlan set hostednetwork mode=allow ssid=AKK-Network key=123456789')
        os.system ('netsh wlan start hostednetwork')
    elif cmd == '2':
        print ('Wifi Hotspot is Disable')
        os.system ('netsh wlan stop hostednetwork')
    elif cmd == '3':
        quit()
    else:
        print('\n')
        print ('Bad input Sir! You can only choose (1,2,3)')
        print('\n')
        os.system('pause')
