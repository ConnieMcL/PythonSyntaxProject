import json
import ast
import os


counts= {}
#changeout file path
for subdir, dirs, files in os.walk('/home/u180133/PROGECT/qualitas/mailman'):
    for file in files:

        
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".py"):
            #print filepath +'\n'
            
            
           
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


 
with  open('/home/u180133/PROGECT/perProjQualitas.txt','a') as bean:
    #change out file path
    bean.write('/home/u180133/PROGECT/qualitas/mailman')
    bean.write('\n')
    json.dump(counts, bean)
    bean.write('\n')
    bean.close()
          


          
