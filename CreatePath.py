#!/usr/bin/python

import os
import errno

# the folder where the assets will be created
targetFolder = "C:\\User\\johnDoe\\portfolio\\projects\\site-generator\\targetFolder";

# fn to replicate mkdir -p
def mkdir_p(path):
    try:
        os.makedirs(path)
        print("successfully created " + path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            print("Error: The path '" + path + "' already exists")
            pass

# end mkdir_p()

