import os

courseTitle = "Physics"
# currentDirectory = os.getcwd()
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
mainDir = os.path.join(desktop, courseTitle)

fileIDS = ['MATH', 'ACM', 'PHYC']
folderSet = []

def makeSubDirs(fID):

    for id in fileIDS:
        folderSet.append(os.path.join(mainDir, id))

    for newDir in folderSet:
        if not os.path.exists(newDir):
            print("Creating directory {}".format(newDir))
            os.makedirs(newDir)
        else:
            print("Directory {} already exists.".format(newDir))


def moveFiles(filePrefix):
    if filePrefix == "MATH":
        newPath = folderSet[0]
    elif filePrefix == "ACM":
        newPath = folderSet[1]
    elif filePrefix == "PHYC":
        newPath = folderSet[2]

    for file_prefix in os.listdir(desktop):
        # print(desktop)
        if file_prefix.startswith(filePrefix):

            # print(file_prefix)
            os.rename(desktop + "\\" +file_prefix, newPath + "\\" +file_prefix)
            # print("Moving from {} to {}".format(desktop + "\\" + file_prefix, newPath+ "\\" + file_prefix))


def main(IDs):
    if not os.path.exists(mainDir):
        print("Directory Doesn't Exist, Creating...\n")
        os.makedirs(mainDir)

    else:
        print("Directory Already Exists\n")

    makeSubDirs(IDs)
    for item in fileIDS:
        moveFiles(item)


main(fileIDS)