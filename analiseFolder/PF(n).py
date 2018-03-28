import json
counts={}


with open('/home/u180133/PROGECT/data/xallnodes.txt') as nodes:
        content = nodes.readlines()
        content = [x.strip() for x in content]
        for y in content :
            counts[y]=0

#print counts    


nodes.close()
numfiles=0






with open('/home/u180133/PROGECT/data/fileDicts.txt') as handle:
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

            



    
handle.close()

print counts
print numfiles

for y in counts.keys():
    counts[y] = round(((counts[y] /29001.0)*100),3)

print counts

with  open('/home/u180133/PROGECT/analiseFolder/PF(n).json','a') as bean:
               
                
    json.dump(counts, bean)
    print "#####"
    bean.close()