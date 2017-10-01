import os, sys
from os.path import join, getsize

for root, dirs, files in os.walk(sys.argv[1]):
    size = sum(getsize(join(root, name)) for name in files)
    print root.replace("/", ";") + " " + str(size)
