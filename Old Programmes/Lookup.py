
import os
import math
import random






files=os.listdir()
for filename in files:
    if (filename[-3:])!='txt':
        files.remove(filename)
#random.shuffle(files)
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



connects=[]
for node in mainnodes:
    f=open(node,'r')
    names=f.readlines()
    connect=[]
    for name in names:
        name=name[0:-1]+'.txt'
        index=files.index(name)
        connect.append(index)

        
    f.close()

    connects.append(connect)
    
#print(connects)

points=[]
for i in range(len(files)):
    peeps=[]
    for connect in connects:
        #print(len(connect))
        for index in connect:
            if index==i:
                peeps.append(files.index(mainnodes[connects.index(connect)]))
    points.append([len(peeps),peeps,files[i]])
    #print(peeps)

#print(points)

sets=[]

for i in range(nosubnodes):
    if files[i] in mainnodes:
        index=mainnodes.index(files[i])
        sett=connects[index][:]
        for pos in points[i][1]:
            if pos not in sett:
                sett.append(pos)

        sets.append(sett)
    else:
        sets.append(points[i][1])

for i in range(nosubnodes):
    sets[i]=[len(sets[i]),files[i],sets[i]]

def search(name,files,sets):
    peeps=[]
    name=name+'.txt'
    index=files.index(name)
    for a in sets[index][2]:
        peeps.append(files[a])
    return peeps

def repsearch(index,files,sets): #does second layer
    peeps=[]
    for a in sets[index][2]:
            per=files[a][0:-4]
            peeps.append(search(per,files,sets))

    return peeps

def removedub(peeps):
    toprint=[]
    for peep in peeps:
        for pee in peep:
            if pee not in toprint:
                toprint.append(pee)

    return toprint

def searchlayer(name,files,sets,gens):
    if gens==1:
        for a in search(name,files,sets):
            print(a)
        return
    else:
        connectedness=[]
        lay1=search(name,files,sets)
        #print('\n===LAYER 1==='+str(len(lay1))+' people===')
        #for a in lay1:
            #print(a[:-4])
        
        name=name+'.txt'
        index=files.index(name)
        connectedness.append(len(lay1))
        lay1.append(name)
        
        #print(sets[index])
        #print('Connected to...')
        peeps=[]
        
        if gens>1:
            peeps=repsearch(index,files,sets)
            peeps=removedub(peeps)
            lay2=[]
            for peep in peeps:
                if peep not in lay1:
                    lay2.append(peep)
            
            print('\n===LAYER 1+2==='+str(len(lay1+lay2))+' people===')
            connectedness.append(len(lay2))
            display=lay1+lay2

            random.shuffle(display)
            
            for a in display:
                print(a[:-4])

            peeps=lay2

            
            if gens>2:
                apeeps=[]
                for peep in peeps:
                    for pee in repsearch(files.index(peep),files,sets):
                        apeeps.append(pee)
                peeps=removedub(apeeps)

                lay3=[]
                for peep in peeps:
                    if peep not in lay1:
                        if peep not in lay2:
                            lay3.append(peep)

                print('\n===LAYER 3==='+str(len(lay3))+' people===')
                connectedness.append(len(lay3))
                for a in lay3:
                    print(a[:-4])

                peeps=lay3

                if gens>3:
                    apeeps=[]
                    for peep in peeps:
                        for pee in repsearch(files.index(peep),files,sets):
                            apeeps.append(pee)
                    peeps=removedub(apeeps)

                    lay4=[]
                    for peep in peeps:
                        if peep not in lay1:
                            if peep not in lay2:
                                if peep not in lay3:
                                    lay4.append(peep)

                    print('\n===LAYER 4==='+str(len(lay4))+' people===')
                    connectedness.append(len(lay4))
                    for a in lay4:
                        print(a[:-4])

                    peeps=lay4

                    if gens>4:
                        apeeps=[]
                        for peep in peeps:
                            for pee in repsearch(files.index(peep),files,sets):
                                apeeps.append(pee)
                        peeps=removedub(apeeps)

                        lay5=[]
                        for peep in peeps:
                            if peep not in lay1:
                                if peep not in lay2:
                                    if peep not in lay3:
                                        if peep not in lay4:
                                            lay5.append(peep)

                        print('\n===LAYER 5==='+str(len(lay5))+' people===')
                        connectedness.append(len(lay5))
                        for a in lay5:
                            print(a[:-4])

                        peeps=lay5

                        if gens>5:
                            apeeps=[]
                            for peep in peeps:
                                for pee in repsearch(files.index(peep),files,sets):
                                    apeeps.append(pee)
                            peeps=removedub(apeeps)

                            lay6=[]
                            for peep in peeps:
                                if peep not in lay1:
                                    if peep not in lay2:
                                        if peep not in lay3:
                                            if peep not in lay4:
                                                if peep not in lay5:
                                                    lay6.append(peep)

                            print('\n===LAYER 6==='+str(len(lay6))+' people===')
                            connectedness.append(len(lay6))
                            for a in lay6:
                                print(a[:-4])

                            peeps=lay6
        
            
    tot=0
    for i in range(len(connectedness)):
        tot=tot+(i+1)*connectedness[i]
    avg=tot/(len(files)-1)

    print('Connectedness Score - - - '+str(round(avg,3)))

    return

while True:
    lookup=str(input("\nName of Person to Lookup:"))
    gens=int(input('How many layers:'))
    searchlayer(lookup,files,sets,gens)
