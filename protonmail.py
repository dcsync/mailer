#!/usr/bin/env python3

import time
import subprocess
import fcntl
import os

_proc = None

def start(user, password):
    global _proc
    _proc = subprocess.Popen(['Desktop-Bridge', '--cli'], stdout=subprocess.PIPE,
            stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    # make stdout non-blocking
    #flags = fcntl.fcntl(_proc.stdout, fcntl.F_GETFL)
    #fcntl.fcntl(_proc.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    if _proc.poll():
        print('early exit')
        return None

    data = r"""
clear cache
yes
clear keychain
yes
login {}
{}
change mode
yes
info
""".format(user, password)

    try:
        _proc.stdin.write(data.encode())
    except Exception as e:
        print('write error: ' + str(e))
        return None

    try:
        data = b''
        while True:
            new_data = os.read(_proc.stdout.fileno(), 1024)
            if new_data:
                data += new_data
                print(new_data)
            else:
                break
    except OSError:
        pass

    print(data)

def stop():
    global _proc
    _proc.stdin.close()

start('', '')
