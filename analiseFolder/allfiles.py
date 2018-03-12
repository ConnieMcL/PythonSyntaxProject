import json



with open('/home/u180133/PROGECT/data/allFilesQualitas.txt') as handle:
    dictdump = json.loads(handle.read())
    print type(dictdump) == dict

    with open('/home/u180133/PROGECT/data/xallnodes.txt') as nodes:
        content = nodes.readlines()
        content = [x.strip() for x in content]

    for y in content :
        if y in dictdump.keys():
            print y
            
        else :
            print 'XXXXXXXXXXXXXXXX', y
    