import json
import ast
import os



for subdir, dirs, files in os.walk('/home/u180133/PROGECT/ParseFiles/'):
    for file in files:

        counts= {}
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".py"):
            print filepath +'\n'
            
            
           
            try:
                tree = ast.parse(open(filepath).read())
            except SyntaxError:
                print 'Syntax Error Keep Her Lit'
                pass
            for node in ast.walk(tree):

              
                
       
                #print type(node).__name__
                nt = type(node).__name__
                if nt  not in counts:
                    counts[nt]=0

                counts[nt]+=1
        if filepath.endswith(".py"):  
            with  open('/home/u180133/PROGECT/perFileT.txt','a') as bean:
                #bean.write('Hello World' +'\n') 
                bean.write( filepath+'\n') 
                json.dump(counts, bean)
                bean.write('\n')
                bean.close()
          


          
