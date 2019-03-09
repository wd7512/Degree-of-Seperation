import turtle
import os
import math
import random
files=os.listdir()
for filename in files:
    if (filename[-4:])!='.txt':
        #print(filename)
        files.remove(filename)
random.shuffle(files)
#print(files)
mainnodes=[]
for filename in files:
    f=open(filename,'r')
    contents=f.readlines()
    if contents!=[]:
        mainnodes.append(filename)
    f.close()

nosubnodes=len(files)
nomainnodes=len(mainnodes)


radius=380
pen=turtle.Turtle()
pen.speed(10000000)
pen.ht()
#pen.penup()
#pen.setpos(0,-radius)
#pen.pendown()
#pen.circle(radius)
angle=2*math.pi/nosubnodes




connects=[]
for node in mainnodes:
    f=open(node,'r')
    names=f.readlines()
    connect=[]
    for name in names:
        #print(name)
        name=name[0:-1]+'.txt'
        index=files.index(name)
        connect.append(index)

        
    f.close()

    connects.append(connect)
    
#print(connects)

points=[]
for i in range(len(files)):
    count=[]
    for connect in connects:
        for index in connect:
            if index==i:
                count.append(files.index(mainnodes[connects.index(connect)]))
    points.append([len(count),count,files[i]])

#print(points)

sets=[]

for i in range(nosubnodes):
    if files[i] in mainnodes:
        index=mainnodes.index(files[i])
        sett=connects[index]
        
        for pos in points[i][1]:
            if pos not in sett:
                sett.append(pos)

        sets.append(sett)
        
    else:
        sets.append(points[i][1])

for i in range(nosubnodes):
    sets[i]=[len(sets[i]),files[i],sets[i]]
#for a in sets:
    #print(a)

print(str(nosubnodes)+' people')
print(str(nomainnodes)+' participants')




coords=[]
minirad=10
freqa=[]
for i in range(nosubnodes):
    pen.penup()



    close=sets[i][0]
    #print(close)
    freqa.append(close)

    


    
    close=int(1.92**(close))
    #print(close)

    if files[i] in mainnodes:
        pen.color('blue')
        x=math.sin(angle*i)*(radius-close)
        y=math.cos(angle*i)*(radius-close)
    else:
        pen.color('orange')
        x=math.sin(angle*i)*(radius-close)
        y=math.cos(angle*i)*(radius-close)
    
    
    #x=random.randint(-radius,radius)
    #y=random.randint(-radius,radius)
    
    coords.append([x,y])
    pen.setpos(x,y-minirad)
    pen.pendown()
    
    
    
    
    pen.circle(minirad)

freq=[0,0,0,0,0,0,0,0,0,0,0,0,0]

for re in freqa:
    #print(re)
    freq[re]=freq[re]+1
countvar=0
for fre in freq:
    print(str(fre)+' people with '+str(countvar)+' unique connections')
    countvar=countvar+1
#print(freq)


pen.color('Black')
for node in mainnodes:
    pos=coords[files.index(node)]
    
    f=open(node,'r')
    names=f.readlines()
    for name in names:
        name=name[0:-1]+'.txt'
        index=files.index(name)
        moveto=coords[index]


        pen.penup()
        pen.setpos(pos[0],pos[1])
        pen.pendown()
        pen.setpos(moveto[0],moveto[1])


        
    f.close()
    

