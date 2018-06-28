#!/usr/bin/env python3

import sys, os

args = sys.argv

for arg in args:
    print("  " + arg)

print(os.popen("git status").read())

