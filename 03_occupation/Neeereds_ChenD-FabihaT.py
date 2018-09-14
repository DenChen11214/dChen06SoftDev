def dictFile(filename):
    try:
        f= open(filename,'r')
    except:
        print("File does not exist")
        return 0
    fText = f.read()
    lines = fText.split('\n')[1:]
    allOcc = []
    for occ in lines:
        if "\"" in occ:
            allOcc.append(occ.split("\"")[1:])
            allOcc[-1][-1] = allOcc[-1][-1][1:]
        else:
            allOcc.append(occ.split(','))
    occDict = dict(allOcc)
    print(occDict)
def chooseOcc():
    
dictFile("occupations.csv")
