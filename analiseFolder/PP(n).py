import json
import ast
counts={}


with open('/home/u180133/PROGECT/data/xallnodes.txt') as nodes:
        content = nodes.readlines()
        content = [x.strip() for x in content]
        for y in content :
            counts[y]=0

print counts    

nodes.close()
    










with open('/home/u180133/PROGECT/data/projectDicts.txt') as handle:
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

            


handle.close()
    


print counts

for y in counts.keys():
    counts[y] = round(((counts[y] /48.0)*100),3)

print counts

with  open('/home/u180133/PROGECT/analiseFolder/PP(n).json','a') as bean:
                #bean.write('Hello World' +'\n') 
                
    json.dump(counts, bean)
    print "#####"
    bean.close()