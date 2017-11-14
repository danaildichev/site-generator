import os

# -------------------------------------------------------------------
# constants

# where we want our folders, subfolders, and files to be created
targetFolder = "C:\Users\Danail\Documents\python\\fiddle\\rcm\\targetFolder"

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
filePaths = [
    "\one\\two\\three\\four",
    "\one\\two",
    "\one\\two\\three",
    "\one\\two\\three\\four",
    "\one"
]

# landing pages
landingPages = [
    "landingPage1.com/",
    "landingPage2.com/",
    "landingPage3.com/",
    "landingPage4.com/",
    "landingPage5.com/"
]

# end constants

# -----------------------------------------------------------------
# step 2.1 - create a list of every folder that needs an index file

# build the list of sub targets
targetPaths = []
for i in range(len(domains)):
    targetPaths.append(targetFolder + "\\" + domains[i] + filePaths[i] )

# print "\ntarget paths:"
# for i in targetPaths:
#     print i

# append all branches of target paths to a list
targetBranches = []

for i in targetPaths:
    os.chdir(i)
    while os.getcwd() != targetFolder:
        targetBranches.append(os.getcwd())
        os.chdir(os.path.dirname(os.getcwd()))

# verify contents of targetBranches
print "targetBranches: "
for i in targetBranches:
    print i

# end step 1

# ---------------------------------------------------------------------
# step 2.2 - go to every folder and create an index file pointed at
#            the landing url

# go to every folder
for i in targetBranches:
        # create an index.php
        fileName = i + "\\index.php"
        IFH = open(fileName, 'w')
        print "created index on " + i

        # write the forwarding script to the index
        # todo write the proper php statement
        payload = "<?php echo 'success' ?>"
        IFH.write(payload)
        print "payload written"
        IFH.close()













