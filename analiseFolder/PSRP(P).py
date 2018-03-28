import json

projects={}



projects={}
counts={}


with open('/home/u180133/PROGECT/data/xallnodes.txt') as nodes:
        content = nodes.readlines()
        content = [x.strip() for x in content]
        print content
        for y in content :
            counts[y]=0.0

print len(counts)    

countsii= counts
nodes.close()
dictdump={}
dictkey=""

with open('/home/u180133/PROGECT/data/projectDicts.txt') as handle:
    i=0.0
    for line in handle:

        try:
            dictdump = json.loads(line)
            length=len(dictdump)


            projects[progname]=length +0.0
            #print length

            #if i <= len(projects):
                #print "xxxx"
                #print progname
                #print i
                #print "yyyy"
                



        except ValueError:
            progname =line.rstrip()
            #print "oops"

           

            


handle.close()

print projects

for y in projects.keys():
    projects[y] =  round(((projects[y] /91)*100),3)
    
print projects
with  open('/home/u180133/PROGECT/analiseFolder/PSRP(P).json','a') as bean:
               
                
    json.dump(projects, bean)
    print "#####"
    bean.close()