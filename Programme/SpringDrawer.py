import turtle
import os
import math
import random
files=os.listdir()
newfiles=[]
for filename in files:
    
    if (filename[-4:])=='.txt':
        print(filename)
        newfiles.append(filename)
random.shuffle(newfiles)
files=newfiles
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


radius=200
minirad=5
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

freqa=[]
for i in range(nosubnodes):
    
    close=sets[i][0]
    #print(close)
    freqa.append(close)
    
    #print(close)




freq=[0,0,0,0,0,0,0,0,0,0,0,0,0]

for re in freqa:
    #print(re)
    freq[re]=freq[re]+1
countvar=0
for fre in freq:
    print(str(fre)+' people with '+str(countvar)+' unique connections')
    countvar=countvar+1
#print(freq)



for i in range(nosubnodes):
    pen.penup()

    close=int(1.8**(freqa[i]))
    
    if files[i] in mainnodes:
        pen.color('blue')
        x=math.sin(angle*i)*(radius-close)
        y=math.cos(angle*i)*(radius-close)
    else:
        pen.color('orange')
        x=math.sin(angle*i)*(radius-close)
        y=math.cos(angle*i)*(radius-close)
    if files[i]=='Will Dennis.txt':
        pen.color('red')
    if files[i] in ['Pat Nichols.txt','Seb Merricks.txt','Lara Freeman.txt','Oscar Cowen.txt','Adam Robarts.txt','Ollie Rennison.txt','Reuben Heaton.txt']:
        pen.color('green')
    
    
    #x=random.randint(-radius,radius)
    #y=random.randint(-radius,radius)
    
    coords.append([x,y])
    pen.setpos(x,y-minirad)
    pen.pendown()
    
    
    
    
    pen.circle(minirad)

def oldbuffer(coords,minirad):
    for i in range(len(coords)):

        pos=coords[i]
        x1=pos[0]
        y1=pos[1]
        #print(2*minirad)
        for j in range(len(coords)):

            if i!=j:

                coord=coords[j]
                x2=coord[0]
                y2=coord[1]
                
                if math.sqrt((x2-x1)**2+(y2-y1)**2)<(3*minirad):
                    while x2-x1==0:
                        x1=x1+random.randint(0,1)*2-1
                    while y2-y1==0:
                        y1=y1+random.randint(0,1)*2-1
                    grad=(y2-y1)/(x2-x1)
                    ang=math.atan(grad)

                    rad=random.randint(0,1)*2-1
                    
                    while math.sqrt((x2-x1)**2+(y2-y1)**2)<(3*minirad):
                        print(files[i])
                        print(files[j])
                        cx=(math.cos(ang))
                        cy=math.sin(ang)
                        if grad>0:
                            if x1>0:
                                cx=-cx
                                cy=-cy

                        if grad<0:
                            if x1>0:
                                cx=-cx
                            if y1<0:
                                cy=-cy
                        x1=x1+cx
                        y1=y1+cy
                    print('====')
        coords[i][0]=x1
        coords[i][1]=y1

    return coords

def buffer(coords,minirad):
    for i in range(len(coords)):
        pos=coords[i]
        x1=pos[0]
        y1=pos[1]

        
        rot=1
        for j in range(len(coords)):
            if i!=j:
                coord=coords[j]
                x2=coord[0]
                y2=coord[1]
                grad=(y2-y1)/(x2-x1)
                
                while math.sqrt((x2-x1)**2+(y2-y1)**2)<(2*minirad):
                    remx=0+x1
                    remy=0+y1
                    print('o')
                    if y2==remy:
                        if x2>remx:
                            x1=x1-0.1
                        else:
                            x1=x1+0.1
                    elif remx==x2:
                        if y2>remy:
                            y1=y1-0.1
                        else:
                            y1=y1+0.1
                    else:
                        if grad>0:
                            if x2-remx<0:
                                x1=x1+0.1
                                y1=y1+0.1
                            else:
                                x1=x1-0.1
                                y1=y1-0.1
                        else:
                            if x2-remx<0:
                                x1=x1-0.1
                                y1=y1+0.1
                            else:
                                x1=x1+0.1
                                y1=y1-0.1

                        print(math.sqrt((x2-x1)**2+(y2-y1)**2))

                    
                


        coords[i][0]=x1
        coords[i][1]=y1

    return coords
                    
                    

def drawcircles(minirad,files,mainnodes,coords):

    for i in range(len(files)):
        pen.penup()
        pos=coords[i]
        if files[i] in mainnodes:
            pen.color('blue')
        else:
            pen.color('orange')

        if files[i]=='Will Dennis.txt':
            pen.color('red')
        if files[i] in ['Pat Nichols.txt','Seb Merricks.txt','Lara Freeman.txt','Oscar Cowen.txt','Adam Robarts.txt','Ollie Rennison.txt','Reuben Heaton.txt']:
            pen.color('green')

        x=pos[0]
        y=pos[1]
        pen.setpos(x,y-minirad)
        pen.pendown()
        pen.circle(minirad)
    

def drawlines(mainnodes,files,coords):

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



def shiftcoord(cordy,files,sets):

    coords=cordy[:]

    tension=0.001
    springsize=40
    new=[]
    for i in range(len(files)):
        pos1=coords[i]
        x1=pos1[0]
        y1=pos1[1]
        peeps=sets[i][2]

        vectors=[]
        for peep in peeps:
            #if files[i]=='Will Dennis.txt':
                #print(files[peep])
            pos2=coords[peep]
            x2=pos2[0]
            y2=pos2[1]
            distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
            while x2-x1==0:
                x1=x1+random.randint(0,1)*2-1
            grad=(y2-y1)/(x2-x1)
            ang=math.atan(grad)
            #print(math.atan(grad))
            if grad>0:
                if x1<0:
            
                    vector=[math.cos(ang)*tension*distance,
                            math.sin(ang)*tension*distance]
                else:
                    vector=[-math.cos(ang)*tension*distance,
                            -math.sin(ang)*tension*distance]
            if grad<0:
                vecx=math.cos(ang)*tension*distance
                vecy=math.sin(ang)*tension*distance
                if x1>0:
                    vecx=-vecx
                if y1<0:
                    vecy=-vecy
                vector=[vecx,vecy]
            vectors.append(vector)

        '''
        inv=True
        while x1==0:
            x1=x1+random.randint(0,1)*2-1
        
        grad=y1/(x1)
        ang=math.atan(grad)
        distance=math.sqrt(x1**2+y1**2)
        if grad>0:
            if x1<0:
            
                vector=[math.cos(ang)*tension*distance,
                        math.sin(ang)*tension*distance]
            else:
                vector=[-math.cos(ang)*tension*distance,
                        -math.sin(ang)*tension*distance]
        else:
            vecx=math.cos(ang)*tension*distance
            vecy=math.sin(ang)*tension*distance
            if x1>0:
                vecx=-vecx
            if y1<0:
                vecy=-vecy

            if inv==True:
                vector=[-vecx,-vecy]
            else:
            
                vector=[vecx,vecy]

            
        vectors.append(vector)
        '''
        xx=x1
        yy=y1      
        for vector in vectors:
            xx=xx+vector[0]
            yy=yy+vector[1]

        #print(yy)
        
        while xx>350:
            xx=xx-1
        while xx<-350:
            xx=xx+1
        while yy>350:
            yy=yy-1
        while yy<-350:
            yy=yy+1


        #print([xx,yy])
        #print(y1)

        
        new.append([xx,yy])

    return new
               
#drawlines(mainnodes,files,coords)
pen.clear()
for i in range(100):
    print(i)
    #pen.clear()
    #drawcircles(minirad,files,mainnodes,coords)
    coords=shiftcoord(coords,files,sets)
    #pen.clear()
    #drawcircles(minirad,files,mainnodes,coords)
    #coords=buffer(coords,minirad)
    
    if (i+1)%50==0:
        True
        '''
        pen.clear()
        drawcircles(minirad,files,mainnodes,coords)
        sav=(turtle.getscreen())
        sav.getcanvas().postscript(file=str(i+1)+".eps")
        sav.clear()
        '''

drawcircles(minirad,files,mainnodes,coords)


coords=buffer(coords,minirad)

pen.clear()
drawcircles(minirad,files,mainnodes,coords)

coords=buffer(coords,minirad)

a=input(':')
drawlines(mainnodes,files,coords)
