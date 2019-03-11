name=input('Name of person whos names need filling:')
f=open(name+'.txt','r')
names=f.readlines()
#print(names)
for i in range(5):
    names[i]=names[i][0:-1]
#print(names)
f.close()
for name in names:
    g=open(name+'.txt','a')
    g.close()

