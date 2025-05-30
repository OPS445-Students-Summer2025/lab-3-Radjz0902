#!/usr/bin/env python3
'''Lab 3 Inv 3 - Check Disk Space'''
# Author ID: 144342235

import subprocess

def free_space():
    # Run the command to get available disk space on root '/'
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         shell=True)
    
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())
