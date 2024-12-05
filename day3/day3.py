import re

def getfuncs(s):
    return re.match("(do\(\)|don't\(\)).+",s)

def getmuls(s):
    return re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",s)

def getpairs(spair):

    s=re.findall("[0-9]{1,3}",spair)
    d=[]
    if len(s) != 2:
        raise IndexError("must be two values")
    for i in s:
        d.append(int(i))
    return d

with open('data.txt','r') as file:
    s = file.read()
    d = getmuls(s)
    print(len(d))
    result = 0
    for i in d:
        p = getpairs(i)
        result = result + p[0]*p[1]
    print(result)


  
    




