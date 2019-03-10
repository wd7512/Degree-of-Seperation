import turtle
import os
import math
import random
import canvasvg
import numpy as np

def shiftcoord(cordy,files,sets,tension,spread):

    coords=cordy[:] #get coordinates list without editing it


    centre=[0,0]
    for cord in coords: 
        centre[0]=centre[0]+cord[0]
        centre[1]=centre[1]+cord[1]

    centre[0]=centre[0]/len(coords)
    centre[1]=centre[1]/len(coords)#get the mean location of all dots

    #print(centre)
    
    new=[] #for new coordinates
    
    for i in range(len(files)): #for each person
        pos1=coords[i]
        x1=pos1[0]
        y1=pos1[1] #get coords
        
        peeps=sets[i][2] #get people they are connected to


        vectors=[] #for all vectors
        
        for peep in peeps: #for people connected to
            
            pos2=coords[peep]
            x2=pos2[0] #get coords
            y2=pos2[1]

            vect=[(x2-x1)*tension,(y2-y1)*tension] #make a vector that is the person to peep multiplied by tension

            vectors.append(vect)

        if x1>0: #get x vector to push away from mean
            vecx=700+x1-centre[0]
        else:
            vecx=-700+x1-centre[0]
        if y1>0: #get y vector to push away from mean
            vecy=350+y1-centre[1]
        else:
            vecy=-350+y1-centre[0]


        vector=[spread*tension*vecx*len(peeps),spread*tension*vecy*len(peeps)]
        vectors.append(vector) #adds vector that pushes them away from the mean

        xx=x1
        yy=y1
        for vector in vectors: #adds up all their x and y vectors to original coordinates
            xx=xx+vector[0]
            yy=yy+vector[1]

        

        while xx>700:#makes sure they dont go further than border
            xx=xx-1
        while xx<-700:
            xx=xx+1
        while yy>350:
            yy=yy-1
        while yy<-350:
            yy=yy+1



        new.append([xx,yy]) #append new coords

    return new

def drawcircles(minirad,files,mainnodes,coords,pen):

    for i in range(len(files)): #for each person
        pen.penup()
        pos=coords[i] #get their coordinates
        if files[i] in mainnodes: #colour appropirately
            pen.color('blue')
        else:
            pen.color('orange')

        if files[i]=='Will Dennis.txt':
            pen.color('red')
        if files[i] in ['Pat Nichols.txt','Seb Merricks.txt','Lara Freeman.txt','Oscar Cowen.txt','Adam Robarts.txt','Ollie Rennison.txt','Reuben Heaton.txt']:
            pen.color('green')

        x=pos[0]
        y=pos[1]
        pen.setpos(x,y-minirad) #draw
        pen.pendown()
        pen.circle(minirad)


def drawlines(mainnodes,files,coords,connects,pen):

    pen.color('Black')
    for node in mainnodes: #for all mainnodes
        pos=coords[files.index(node)] #get coords
        
        
        
        names=connects[mainnodes.index(node)] #get people named
        
        #print(names)
        for name in names: #for each person named
            
            moveto=coords[name] #get coords of name


            pen.penup()
            pen.setpos(pos[0],pos[1]) #draw
            pen.pendown()
            pen.setpos(moveto[0],moveto[1])


def oldbuffer(coords,minirad,dist):
    for i in range(len(coords)): #for each person

        pos=coords[i] #get their coordinates
        x1=pos[0]
        y1=pos[1]
        
        for j in range(len(coords)): #for each person

            if i!=j: #if different people

                coord=coords[j]
                x2=coord[0] #get their coordinates
                y2=coord[1]

                while math.sqrt((x2-x1)**2+(y2-y1)**2)<(dist*minirad): #if they are too close


                    x1=x1-(x2-x1)*0.1 #shift orginal person away
                    y1=y1-(y2-y1)*0.1
                
        coords[i][0]=x1
        coords[i][1]=y1 #update coords

    return coords

def crosscount(coords,connects,mainnodes): #to count how many crosses there are yet, ignore for now as it doesnt work
    lines=[] #[distance,gradient,coordinate]
    for i in range(len(mainnodes)):
        pos1=coords[i]
        x1=pos1[0]
        y1=pos1[1]
        
        for peep in connects[i]:

            pos2=coords[peep]
            x2=pos2[0]
            y2=pos2[1]

            if x2==x1:
                grad='inf'
            elif y2==y1:
                grad=0
            else:
                grad=(y2-y1)/(x2-x1)
            line=[math.sqrt((y2-y1)**2+(x2-x1)**2),grad,[x1,y1]]
            #print(line)
            lines.append(line)
    '''
    dupe=[]
    for i in range(len(lines)):
        for k in range(len(lines)): # to compare all lines
            if i!=k: #if different
                if lines[i]==lines[k]: #if directly the same
                    dupe.append(lines[k])
                elif lines[i][0]==lines[k][0]: # if of same magnitude
                    print(lines[i])
                    print(lines[k])
                            
                    dupe.append(lines[k])

                        
    #print(sorted(lines))
    
    for du in dupe:
        print(du)
    '''

    lines=sorted(lines)
    dupe=[]
    for i in range(len(lines)-1):
        if lines[i]==lines[i+1]:
            dupe.append(lines[i+1])
        if lines[i][0]==lines[i+1][0]:
            if type(lines[i][1])==float and type(lines[i+1][1])==float and abs(1+lines[i][1]*lines[i+1][1])<0.001:
                dupe.append(lines[i+1])

    for line in dupe:
        lines.remove(line)

    count=0
    for i in range(len(lines)):
        line=lines[i]

        if type(line[1])==float:
            tocomp=lines[:]
            
            tocomp.remove(line)
            

            #-mx+y=-mx1+y1 [-mx,y]

            pos1=line[2]
            
            
            

            xmin=pos1[0]
            xmax=math.cos(math.atan(line[1]))*line[0]

            diff=xmax-xmin
            for comp in tocomp:
                if type(comp[1])==float:

                    left=[[-line[1],1]]
                    right=[-line[1]*pos1[0]+pos1[1]]
                    
                    pos2=comp[2]
                    left.append([-comp[1],1])
                    right.append(-comp[1]*pos2[0]+pos2[1])

                    if left[0][0]-left[1][0]!=0:

                        res=np.linalg.solve(left, right)[0]
                        #print(res)
                        
                        if diff<0:
                            if res<xmin and res>xmax:
                                #print(str(xmin)+','+str(res)+','+str(xmax))
                                count=count+1
                        else:
                            if res>xmin and res<xmax:
                                #print(str(xmin)+','+str(res)+','+str(xmax))
                                count=count+1
    print(len(lines))
    print(count)

def program(runsPar,tensionPar,spreadPar):
    files=os.listdir() #gets list of all files
    newfiles=[]
    
    for filename in files:
        if (filename[-4:])=='.txt':
            newfiles.append(filename) #get text files - people
    
    random.shuffle(newfiles)
    files=newfiles #shuffled list of people


    mainnodes=[] #list of people who have answered
    for filename in files: 
        f=open(filename,'r')
        contents=f.readlines()
        if contents!=[]:
            mainnodes.append(filename)
        f.close()

    nosubnodes=len(files) #number of people
    nomainnodes=len(mainnodes) #number of people answered


    radius=200 #radius of initial circle drawing
    minirad=5 #radius of each node
    angle=2*math.pi/nosubnodes #the angle of each node
    
    pen=turtle.Turtle() #creates pen to draw with
    pen.speed(10000000)
    pen.ht() 
    




    connects=[] #a list corresponding to main nodes which contains the indexs of each person named
    for node in mainnodes: #for each person who has answered
        
        f=open(node,'r')
        names=f.readlines()
        connect=[]
        
        for name in names: #for each person they have named
            name=name[0:-1]+'.txt'
            index=files.index(name) #get their index in the files list
            connect.append(index) #append that index


        f.close()

        connects.append(connect)

    
    points=[] #a list in the format [number of people who named them,the indexes of people who named them,their name file]
    for i in range(len(files)): 
        count=[]
        for connect in connects: #for each mainnode
            for index in connect: 
                if index==i: #if mainnode mentioned them
                    count.append(files.index(mainnodes[connects.index(connect)])) #append the index of the mainnode in files list
        points.append([len(count),count,files[i]])

    

    sets=[]

    for i in range(nosubnodes): #for each peson
        
        if files[i] in mainnodes: #if they are a mainnode
            
            index=mainnodes.index(files[i]) #get their index in mainnode list
            
            sett=connects[index] #get the people they have mentioned

            for pos in points[i][1]: #for each person get the people that mentioned them
                
                if pos not in sett: #if a person who they didnt mention mentioned them
                    
                    sett.append(pos) #add to list

            sets.append(sett) #append the index of all their unique connections

        else: #if not a mainnode
            
            sets.append(points[i][1]) #just append people that mentioned them

    for i in range(nosubnodes):
        sets[i]=[len(sets[i]),files[i],sets[i]]

    

    print(str(nosubnodes)+' people')
    print(str(nomainnodes)+' participants')




    coords=[] #list for everyones coordinates

    freqa=[] #list corresponding to files which will contain the number of unique connections
    for i in range(nosubnodes):

        close=sets[i][0] #get number of unique connections
        freqa.append(close) #append number unique connections





    freq=[0,0,0,0,0,0,0,0,0,0,0,0,0] #list to contain frequencies of unique connections

    for re in freqa:
        freq[re]=freq[re]+1 #count up how many of each frequency

        
    countvar=0
    for fre in freq: #displays number of unique connections
        
        print(str(fre)+' people with '+str(countvar)+' unique connections')
        countvar=countvar+1
    



    for i in range(nosubnodes): #for each person
        pen.penup()

        close=int(1.8**(freqa[i])) #how far in each person is from the centre 

        if files[i] in mainnodes: #make mainnodes blue
            pen.color('blue')
            x=math.sin(angle*i)*(radius-close)
            y=math.cos(angle*i)*(radius-close)
        else:                     #make nodes organse
            pen.color('orange')
            x=math.sin(angle*i)*(radius-close)
            y=math.cos(angle*i)*(radius-close)
        if files[i]=='Will Dennis.txt':
            pen.color('red')
        if files[i] in ['Pat Nichols.txt','Seb Merricks.txt','Lara Freeman.txt','Oscar Cowen.txt','Adam Robarts.txt','Ollie Rennison.txt','Reuben Heaton.txt']:
            pen.color('green')

        '''
        x=random.randint(-radius,radius)
        y=random.randint(-radius,radius)
        #for random starting coords
        '''

        
        coords.append([x,y]) #append coordinates
        pen.setpos(x,y-minirad)
        pen.pendown()




        pen.circle(minirad)

    a=input(':')
    drawlines(mainnodes,files,coords,connects,pen)

    pen.clear() #clear canvas of original circle

    crosscount(coords,connects,mainnodes)

    runs=runsPar #assigns variables
    tension=tensionPar 
    spread=spreadPar

    for i in range(runs): 
        #print(i)
        if i<runs-100:

            coords=shiftcoord(coords,files,sets,tension,spread) #update coordinates


            if (i+1)%100==0: #every 100th do big buffering
                coords=oldbuffer(coords,minirad,10)
                coords=oldbuffer(coords,minirad,5)
                coords=oldbuffer(coords,minirad,3)
                '''
                pen.clear()
                drawcircles(minirad,files,mainnodes,coords)
                sav=(turtle.getscreen())
                sav.getcanvas().postscript(file=str(i+1)+".eps")
                sav.clear()
                '''
        else: #last 100 runs buffers more
            coords=oldbuffer(coords,minirad,4)
            coords=shiftcoord(coords,files,sets,tension,spread)


    pen.clear()
    drawcircles(minirad,files,mainnodes,coords,pen) #draw circles

    crosscount(coords,connects,mainnodes)

    a=input(':')
    drawlines(mainnodes,files,coords,connects,pen)
    #canvasvg.saveall("{},{},{} .svg".format(runs,tension,spread),turtle.getcanvas())
    #pen.clear()
    

            
program(10000,0.001,0.001)
