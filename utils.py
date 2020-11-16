import re
import os
import subprocess
import sys
import random
import string
import binascii

# print
debug_enabled = False

def debug(s):
    global debug_enabled
    if debug_enabled:
        print('[D] ' + s, file=sys.stderr)

def info(s):
    print('[.] ' + s, file=sys.stderr)

def good(s):
    print('[+] ' + s, file=sys.stderr)

def bad(s):
    print('[!] ' + s, file=sys.stderr)

def die(s):
    bad(s)
    sys.exit(1)
