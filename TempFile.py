#!/usr/bin/python
import shutil
import tempfile
import time

# TODO
# create a tmp directory and
# use finally to delete the tmp directory
# and the files within it

t = tempfile.mkdtemp()
try:
    print(t, "1111")
    f = open(t + "/my_temp_file.txt", "w")
    f.write("this is a test")
    f.close()
finally:
    time.sleep(10)
    shutil.rmtree(t, ignore_errors=True)