from time import sleep
Sidetilside = 0
Svingbanetur = 0

def Rød():
    global Sidetilside
    global svingbanetur
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    sleep(1)
    if Svingbanetur == 2:
        return SvingbaneRødGul()
    if Sidetilside == 0:
        return RødGulNS()
    elif Sidetilside == 1:
        return RødGulVØ()
#Svingbane
def SvingbaneRødGul():
    print ('\x1b[6;30;43m' + "RødGul! pil" + '\x1b[0m''   \x1b[6;30;43m' + "RødGul! pil" + '\x1b[0m')
    sleep(2)
    return SvingbaneGrøn()
def SvingbaneGrøn():
    global Svingbanetur
    print ('\x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m''   \x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m')
    sleep(4)
    Svingbanetur = 0
    return SvingbaneGul()
def SvingbaneGul():
    global Svingbanetur
    print ('\x1b[6;30;43m' + " Gul! pil  " + '\x1b[0m''   \x1b[6;30;43m' + " Gul! pil  " + '\x1b[0m')
    sleep(1)
    return Rød()
#NS
def GrønNS():
    print ('\x1b[7;32;40m' + " Grøn! Kør " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    sleep(1)
    print ('\x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m')
    sleep(4)
    return GulNS()

def RødGulNS():
    print ('\x1b[6;30;43m' + "RødGul! Kør" + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    sleep(2)
    return GrønNS()

def GulNS():
    global Sidetilside
    global Svingbanetur
    print ('\x1b[6;30;43m' + " Gul! stop " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    sleep(1)
    Sidetilside = 1
    Svingbanetur += 1
    return Rød()

#VØ
def GrønVØ():
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[7;32;40m' + " Grøn! Kør " + '\x1b[0m')
    sleep(1)
    print ('              \x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m')
    sleep(4)
    return GulVØ()

def RødGulVØ():
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;43m' + "RødGul! Kør" + '\x1b[0m')
    sleep(2)
    return GrønVØ()

def GulVØ():
    global Sidetilside
    global Svingbanetur
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;43m' + " Gul! stop " + '\x1b[0m')
    sleep(1)
    Sidetilside = 0
    Svingbanetur += 1
    return Rød()

state=Rød()
while state: state=Rød()  # starter statemachine
print ("Done with states")
