import imageio
import os
name=str(input('Name of Gif:'))
dirfiles=os.listdir()
files=[]
for file in dirfiles:
    if file[-4:]=='.png':
        files.append(file)

ref=files[:]
for i in range(len(ref)):
    #print(ref[i])
    ref[i]=int((ref[i].split(','))[0])
    #print(ref[i])

images=[]

ref=sorted(ref)
for num in ref:
    num=str(num)
    #print(num)
    for file in files:
        
        count=0
        while file[count]!=',':
            count=count+1
            i=0
            for char in num:
                if char==file[i]:
                    
                    i=i+1
                if i==len(num):
                    print(file)
                    images.append(imageio.imread(file))


imageio.mimsave(name+'fast.gif', images,duration=0.05)
#imageio.mimsave(name+'normal.gif', images,duration=0.1)
#imageio.mimsave(name+'slow.gif', images,duration=0.2)
