import os

comp = 0
for subdir, dirs, files in os.walk('/home/u180133/PROGECT/qualitas/'):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".py"):
            print filepath +'\n'
            comp=comp+1
            

print "number of python files in Qualitas :" , comp  
