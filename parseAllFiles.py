import ast
import os

count=0

for subdir, dirs, files in os.walk('/home/u180133/PROGECT/ParseFiles/'):
    for file in files:
    #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".py"):
            print filepath
            
            try:
                tree = ast.parse(open(filepath).read())
            except SyntaxError:
                print 'Syntax Error Keep Her Lit'
                pass
           
        #print ast.dump(tree, annotate_fields=False, include_attributes=False)  
            count=count+1
            print count 
            print 'parsed file' '\n'
                


    