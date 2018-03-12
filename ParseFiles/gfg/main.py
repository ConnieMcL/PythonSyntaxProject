import ast

tree = ast.parse(open('/home/u180133/PROGECT/qualitas/astropy/ah_bootstrap.py').read())

print ast.dump(tree, annotate_fields=False, include_attributes=False) 

comp = 0


for node in ast.walk(tree):
    #print(node)
    if isinstance(node, ast.Compare):
       comp= comp + 1


       
 
print "number of comparisons is: " ,comp