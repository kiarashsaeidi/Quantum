import pandas as pd 
import numpy as np 
import matplotlib.pyplot



def make_quantum(i):
    if (Doreh == 1):
        quantum = ')1S' + str(i)
        return (quantum)
    elif(Doreh == 2):
        if (i <= 4):
            quantum = ')1S2'  +'  '+ ')2S'+ str(i - 2)
        else : 
            quantum = ')1S2' + '  '+')2S2' +'  '+ ')2P' + str(i-4)
        return (quantum)
    
    elif(Doreh == 3):
        if (i <= 12):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+')3S' + str(i - 10)
        elif(i <= 18) : 
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P' + str(i - 12)
        return (quantum)

    elif(Doreh == 4):
        if(i <= 20):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S' + str(i - 18)
        elif(i <= 30):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d' + str(i - 20)
        elif(i <= 36):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P' +str(i - 30)
        return(quantum)

    elif(Doreh == 5):
        if(i <= 38):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S'+str(i - 36)
        elif(i <= 48):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +'4P6' +'  '+')5S2'+'  '+'4d'+str(i - 38)
        elif(i <= 54):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P'+str(i - 48)
        return(quantum)

    elif(Doreh == 6):
        if(i <= 56):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S'+str(i - 54)
        elif(i <= 70):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f'+str(i - 56)
        elif(i <= 80):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d'+str(i - 70)
        elif(i <= 86):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P'+str(i - 80)
        return (quantum)



    elif(Doreh == 7):   

        if(i <= 88):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P6'+'  '+')7S'+str(i - 86)
        elif(i <= 102):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P6'+'  '+')7S2'+'  '+')5f'+str(i - 88)
        elif(i <= 112):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P6'+'  '+')7S2'+'  '+')5f14'+'  '+')6d'+str(i - 102)
        elif(i <= 118):
            quantum = ')1S2'  +'  '+ ')2S2'+ '  '+')2P6'+'  '+ ')3S2' + '  ' + ')3P6' +'  '+')4S2' + '  ' + ')3d10'+ '  ' +')4P6' +'  '+')5S2'+'  '+')4d10'+'  '+')5P6'+'  '+')6S2'+'  '+')4f14'+'  '+')5d10'+'  '+')6P6'+'  '+')7S2'+'  '+')5f14'+'  '+')6d10'+'  '+')7P'+str(i - 112)
        return(quantum)






data = [['Symbol'],
 ['H'],
 ['He'],
 ['Li'],
 ['Be'],
 ['B'],
 ['C'],
 ['N'],
 ['O'],
 ['F'],
 ['Ne'],
 ['Na'],
 ['Mg'],
 ['Al'],
 ['Si'],
 ['P'],
 ['S'],
 ['Cl'],
 ['Ar'],
 ['K'],
 ['Ca'],
 ['Sc'],
 ['Ti'],
 ['V'],
 ['Cr'],
 ['Mn'],
 ['Fe'],
 ['Co'],
 ['Ni'],
 ['Cu'],
 ['Zn'],
 ['Ga'],
 ['Ge'],
 ['As'],
 ['Se'],
 ['Br'],
 ['Kr'],
 ['Rb'],
 ['Sr'],
 ['Y'],
 ['Zr'],
 ['Nb'],
 ['Mo'],
 ['Tc'],
 ['Ru'],
 ['Rh'],
 ['Pd'],
 ['Ag'],
 ['Cd'],
 ['In'],
 ['Sn'],
 ['Sb'],
 ['Te'],
 ['I'],
 ['Xe'],
 ['Cs'],
 ['Ba'],
 ['La'],
 ['Ce'],
 ['Pr'],
 ['Nd'],
 ['Pm'],
 ['Sm'],
 ['Eu'],
 ['Gd'],
 ['Tb'],
 ['Dy'],
 ['Ho'],
 ['Er'],
 ['Tm'],
 ['Yb'],
 ['Lu'],
 ['Hf'],
 ['Ta'],
 ['W'],
 ['Re'],
 ['Os'],
 ['Ir'],
 ['Pt'],
 ['Au'],
 ['Hg'],
 ['Tl'],
 ['Pb'],
 ['Bi'],
 ['Po'],
 ['At'],
 ['Rn'],
 ['Fr'],
 ['Ra'],
 ['Ac'],
 ['Th'],
 ['Pa'],
 ['U'],
 ['Np'],
 ['Pu'],
 ['Am'],
 ['Cm'],
 ['Bk'],
 ['Cf'],
 ['Es'],
 ['Fm'],
 ['Md'],
 ['No'],
 ['Lr'],
 ['Rf'],
 ['Db'],
 ['Sg'],
 ['Bh'],
 ['Hs'],
 ['Mt'],
 ['Ds'],
 ['Rg'],
 ['Cn'],
 ['Nh'],
 ['Fl'],
 ['Mc'],
 ['Lv'],
 ['Ts'],
 ['Og']]


atom = pd.DataFrame(data)


#atom = pd.read_csv('/home/kiarash/Electron/atooms.csv')


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

for i in range(0 , 119):

    if (atom.iloc[i][0] == inat):        
        
        if (i <= He):
            Doreh = 1
        elif(i <=Ne ):
            Doreh = 2
        elif(i <=Ar):
            Doreh = 3
        elif(i <=Kr):
            Doreh = 4
        elif(i <=Xe):
            Doreh = 5
        elif(i <=Rn):
            Doreh = 6
        elif(i <=Og):
            Doreh = 7



        quantum = make_quantum(i)
        print(i+1  , inat , Doreh , '.........'  , quantum)











