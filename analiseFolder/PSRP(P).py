import json
projects={}


with open('/home/u180133/PROGECT/data/QualitasNames.txt') as proj:
        content = proj.readlines()
        content = [x.strip() for x in content]
        for y in content :
            projects[y]=0

print projects    


proj.close()

counts={}


with open('/home/u180133/PROGECT/data/xallnodes.txt') as nodes:
        content = nodes.readlines()
        content = [x.strip() for x in content]
        for y in content :
            counts[y]=0

print counts    


nodes.close()
dictdump={}
dictkey=""

with open('/home/u180133/PROGECT/data/perProjQualitas.txt') as handle:
    while True:
        try:
            dictdump = json.loads(line)
            #ast.literal_eval(dictdump)
            for y in counts.keys():
                if y in projects.keys():
                   projects[y]=1
            
            print projects
        except NameError:
            dictkey=handle.readline()
            print dictkey
            


            


handle.close()
    
