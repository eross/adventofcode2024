

def findnumcount(n, c):
    found = 0
    for x in c:
        if (n==x):
            found = found + 1
    return found



c1=[]
c2=[]
with open('data.txt','r') as file:
    for line in file:
        a1,a2 = line.strip().split()
        c1.append(int(a1))
        c2.append(int(a2))

c1.sort()
c2.sort()

sim=0

for i in c1:
    sim = sim + findnumcount(i,c2)*i

print(sim)    




