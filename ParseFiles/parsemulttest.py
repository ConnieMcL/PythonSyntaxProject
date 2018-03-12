
import ast
import os

#########LITERALS

num=0
string=0
##formval=0 ver 3.6
##joindstr=0 ver 3.6
bytez=0
lists=0
tuples=0
sets=0
dictionarrs=0
ellips=0

#####VARIABLES
names=0
loads=0
stores=0
delet=0
stared=0

#######EXPRESSIONS

expres=0
unaryop=0
uadd=0
usub=0
knot=0
invrt=0
binop=0
add=0
sub=0
mult=0
div=0
floordiv=0
mod=0
poww=0
lshift=0
rshift=0
bitor=0
bitxor=0
bitand=0
#matmult ver 3.5
boolop=0
ands=0
ors=0
comp=0



for subdir, dirs, files in os.walk('/home/u180133/PROGECT/qualitas/'):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".py"):
            print filepath +'\n'
            
            
           
            try:
                tree = ast.parse(open(filepath).read())
            except SyntaxError:
                print 'Syntax Error Keep Her Lit'
                pass
            for node in ast.walk(tree):
            
                if isinstance(node, ast.Compare):
                    comp= comp + 1
#here is where the rest of the if instances would go 

        
print "number of comparisons is: " ,comp