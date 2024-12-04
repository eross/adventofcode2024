c1=[]
c2=[]
with open('data.txt','r') as file:
    for line in file:
        a1,a2 = line.strip().split()
        c1.append(int(a1))
        c2.append(int(a2))

c1.sort()
c2.sort()

diffs=0

for i in range(len(c1)):
    diffs = diffs + abs(c1[i]-c2[i])
    
print(diffs)



