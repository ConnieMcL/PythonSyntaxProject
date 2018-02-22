import json
import ast
counts={}


with open('/home/u180133/PROGECT/data/xallnodes.txt') as nodes:
        content = nodes.readlines()
        content = [x.strip() for x in content]
        for y in content :
            counts[y]=0

#print counts    



numfiles=0






with open('/home/u180133/PROGECT/data/perFileQualitas.txt') as handle:
    for line in handle:
        try:
            dictdump = json.loads(line)
            #ast.literal_eval(dictdump)
            for y in counts.keys():
                if y in dictdump.keys():
                   counts[y]+=1
            
            #print dictdump
        except ValueError:
            print line
            numfiles+=1

            



    


print counts
print numfiles