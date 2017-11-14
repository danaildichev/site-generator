#!/usr/bin/python

#
#   /rcm/main.py
#
#   given a list of domain & filePath strings create a folder structure
#   that matches and create and populate an index.php for every folder.
#

# ---------------------------------------------------------------------
# imports

import os
import CreatePath as CP

# ---------------------------------------------------------------------
# constants - Only this section is editable

# domains purchased
domains = [
    "domain1.com",
    "domain2.com",
    "domain3.com",
    "domain4.com",
    "domain5.com"
]

# file paths to create
# on windows use \\ notation for separating folders
# on linux use /
file_paths = [
    "\one\\two\\three\\four",
    "\one\\two",
    "\one\\two\\three",
    "\one\\two\\three\\four",
    "\one"
]

# landing pages
landing_pages = [
    "landingPage1.com/",
    "landingPage2.com/",
    "landingPage3.com/",
    "landingPage4.com/",
    "landingPage5.com/"
]

# end constants

# ---------------------------------------------------------------------
# step 1

# join file paths to domains
fullPath = []
for i in range(len(domains)):
    fullPath.append(domains[i] + file_paths
[i])

# go to target folder
os.chdir(CP.targetFolder)

# make directories on target folder
for i in fullPath:
    CP.mkdir_p(i)

# end step 1

# ---------------------------------------------------------------------
# step 2

# -----------------------------------------------------------------
# step 2.1 - create a list of every folder that needs an index file

# build the url that will be forwarded to
landing_urls = []
for i in range(len(landing_pages)):
    landing_urls.append("http://" + landing_pages[i])

# build the list of sub targets
target_paths = []
for i in range(len(domains)):
    target_paths.append(CP.targetFolder + "\\" + domains[i] + file_paths[i])

# append all branches of target paths to a list
target_branches = []

for i in target_paths:
    os.chdir(i)
    while os.getcwd() != CP.targetFolder:
        target_branches.append(os.getcwd())
        os.chdir(os.path.dirname(os.getcwd()))

# verify contents of target_branches
# print "\nThe following branches will be acted on: "
# for i in target_branches:
#     print i

# end step 2.1

# ---------------------------------------------------------------------------------
# step 2.2 - go to every folder and create an index file pointed at the landing url

print("")

# go to every folder
for i in target_branches:

    print("Target folder: " + i)

    # create an index.php
    file_name = i + "\\index.php"
    IFH = open(file_name, 'w')
    print("created index.php")

    # write the forwarding script to the index
    # todo write the proper php statement
    payload = "<?php echo 'success' ?>"
    IFH.write(payload)
    print("forwarding script written to file")
    IFH.close()
    print("File saved\n")

# end step 2

# end main.py