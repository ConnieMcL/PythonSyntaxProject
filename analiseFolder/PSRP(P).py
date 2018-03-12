import json

projects={}


#with open('/home/u180133/PROGECT/data/QualitasNames.txt') as proj:
#        content = proj.readlines()
#        content = [x.strip() for x in content]
#        for y in content :
#            projects[y]=0
#
#print projects    


#proj.close()
projects={}
counts={}


with open('/home/u180133/PROGECT/data/xallnodes.txt') as nodes:
        content = nodes.readlines()
        content = [x.strip() for x in content]
        for y in content :
            counts[y]=0

print len(counts)    

countsii= counts
nodes.close()
dictdump={}
dictkey=""

with open('/home/u180133/PROGECT/data/perProjQualitas.txt') as handle:
    i=0
    for line in handle:

        try:
            dictdump = json.loads(line)
            length=len(dictdump)


            projects[progname]=length
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

with  open('/home/u180133/PROGECT/analiseFolder/PSRP(P).txt','a') as bean:
               
                
    json.dump(projects, bean)
    print "#####"
    bean.close()