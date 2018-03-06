import json
import ast
counts={}

dictdump={}
with open('/home/u180133/PROGECT/data/allNodeCount.txt') as handle:
    for line in handle:
        
        dictdump = ast.literal_eval(json.dumps(json.loads(line)))
         
            
       # print dictdump
    




    



combinedVal=0.0
for y in dictdump.keys():
    
    combinedVal= combinedVal + dictdump[y]

print combinedVal

for y in dictdump.keys():
    dictdump[y] = round(((dictdump[y]/combinedVal)*100),3)

print dictdump