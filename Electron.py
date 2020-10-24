import pandas as pd 
import numpy as np 
import matplotlib.pyplot



def make_quantum(i):
    if (Doreh == 1):
        quantum = ')1S' + str(i+1)
        return (quantum)
    elif(Doreh == 2):
        if (i+1 <= 4):
            quantum = ')1S2'  +'  '+ ')2S'+ str(i - 1)
        else : 
            quantum = ')1S2' + '  '+')2S2' +'  '+ ')2P' + str(i-3)
        return (quantum)
    
    elif(Doreh == 3):
        if (i+1 <= 12):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+')3S' + str(i - 9)
        elif(i+1 <= 18) : 
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P' + str(i - 11)
        return (quantum)

    elif(Doreh == 4):
        if(i+1 <= 20):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S' + str(i - 17)
        elif(i+1 <= 30):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d' + str(i - 19)
        elif(i+1 <= 36):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P' +str(i - 29)
        return(quantum)

    elif(Doreh == 5):
        if(i+1 <= 38):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S'+str(i - 35)
        elif(i+1 <= 48):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +'4P6' +'  '+')5S2'+'  '+'4d'+str(i - 37)
        elif(i+1 <= 54):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P'+str(i - 47)
        return(quantum)

    elif(Doreh == 6):
        if(i+1 <= 56):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S'+str(i - 53)
        elif(i+1 <= 70):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f'+str(i - 55)
        elif(i+1 <= 80):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d'+str(i - 69)
        elif(i+1 <= 86):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P'+str(i - 79)
        return (quantum)



    elif(Doreh == 7):   

        if(i+1 <= 88):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P6'+'  '+')7S'+str(i - 85)
        elif(i+1 <= 102):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P6'+'  '+')7S2'+'  '+')5f'+str(i - 87)
        elif(i+1 <= 112):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P6'+'  '+')7S2'+'  '+')5f14'+'  '+')6d'+str(i - 101)
        elif(i+1 <= 118):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P6'+'  '+')7S2'+'  '+')5f14'+'  '+')6d10'+'  '+')7P'+str(i - 111)
        return(quantum)









atom = pd.read_csv('/home/kiarash/Electron/atooms.csv')


inat = input('input atom : ')
inat = inat.capitalize()

num = 0
cul = []
cul2 = []

He = 2
Ne = 10
Ar = 18
Kr = 36
Xe = 54
Rn = 86
Og = 118


afba = ['1s' , '2s' , '2p' , '3s' , '3p' , '4s' , '3d' , '4p' , '5s',  '4d' , '5p' , '6s' , '4f' , '5d' , '6p' , '7s' , '5f' , '6d' , '7p']

for i in range(0 , 118):

    if (atom.iloc[i]['Symbol'] == inat):

        if (i+1 <= He):
            Doreh = 1
        elif(i+1 <=Ne ):
            Doreh = 2
        elif(i+1 <=Ar):
            Doreh = 3
        elif(i+1 <=Kr):
            Doreh = 4
        elif(i+1 <=Xe):
            Doreh = 5
        elif(i+1 <=Rn):
            Doreh = 6
        elif(i+1 <=Og):
            Doreh = 7



        quantum = make_quantum(i)
        print(i+1  , inat , Doreh , '.........'  , quantum)











