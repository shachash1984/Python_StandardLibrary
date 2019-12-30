#!/usr/bin/python
import os
import re
import tempfile
import shutil

t = tempfile.mkdtemp()
try:
    for entry in os.scandir(t):
        stats = entry.stat()
        reg = re.compile("^t")

        if reg.search(entry.name):
            print("starts with 't'")
        print(entry.name, stats.st_size)
finally:
    shutil.rmtree(t, ignore_errors=True)
