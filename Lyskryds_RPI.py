#Statemachine til beskrivelse af livets gang
from gpiozero import LED, Button
from time import sleep

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
NSsidegul=LED(4)
NSsidegrøn=LED(5)

VØred=LED(21)
VØgul=LED(20)
VØgreen=LED(16)
VØsidegul=LED(24)
VØsidegrøn=LED(23)

NSknap = Button(17)#blå
VØknap = Button(6)#grøn

Sidetilside = 0
Svingbanetur = 0

def biloverNS():
    sleep(0.5)
    if NSknap.is_pressed:
        print("Bil køre over rød NS")
    sleep(0.5)
    if NSknap.is_pressed:
        print("Bil køre over for maget rødNS")
        
def biloverVØ():
    sleep(0.5)
    if VØknap.is_pressed:
        print("Bil køre over rød EV")
    sleep(0.5)
    if VØknap.is_pressed:
        print("Bil køre over for maget rødEV")

def Rød():
    global Sidetilside
    global svingbanetur
    VØsidegul.off()
    NSsidegul.off()
    NSgul.off()
    VØgul.off()
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    NSred.on()
    VØred.on()
    biloverVØ()
    biloverNS()
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
    VØsidegul.on()
    NSsidegul.on()
    sleep(2)
    return SvingbaneGrøn()
def SvingbaneGrøn():
    global Svingbanetur
    VØsidegul.off()
    NSsidegul.off()
    print ('\x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m''   \x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m')
    NSsidegrøn.on()
    VØsidegrøn.on()
    sleep(4)
    Svingbanetur = 0
    return SvingbaneGul()
def SvingbaneGul():
    global Svingbanetur
    NSsidegrøn.off()
    VØsidegrøn.off()    
    print ('\x1b[6;30;43m' + " Gul! pil  " + '\x1b[0m''   \x1b[6;30;43m' + " Gul! pil  " + '\x1b[0m')
    VØsidegul.on()
    NSsidegul.on()
    sleep(1)
    return Rød()
#NS
def GrønNS():
    NSred.off()
    NSgul.off()
    print ('\x1b[7;32;40m' + " Grøn! Kør " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    NSgreen.on()
    sleep(1)
    biloverVØ()
    sleep(1)
    biloverVØ()
    sleep(1)
    biloverVØ()
    sleep(1)
    biloverVØ()
    sleep(1)
    biloverVØ()
    return GulNS()

def RødGulNS():
    print ('\x1b[6;30;43m' + "RødGul! Kør" + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    NSgul.on()
    biloverVØ()
    sleep(1)
    biloverVØ()
    Sleep(1)
    return GrønNS()

def GulNS():
    global Sidetilside
    global Svingbanetur
    NSgreen.off()
    print ('\x1b[6;30;43m' + " Gul! stop " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    NSgul.on()
    biloverNS()
    biloverVØ()
    sleep(1)
    Sidetilside = 1
    Svingbanetur += 1
    return Rød()

#VØ
def GrønVØ():
    VØgul.off()
    VØred.off()
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[7;32;40m' + " Grøn! Kør " + '\x1b[0m')
    VØgreen.on()
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    return GulVØ()

def RødGulVØ():
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;43m' + "RødGul! Kør" + '\x1b[0m')
    VØgul.on()
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    return GrønVØ()

def GulVØ():
    global Sidetilside
    global Svingbanetur
    VØgreen.off()
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;43m' + " Gul! stop " + '\x1b[0m')
    EVgul.on()
    biloverVØ()
    biloverNS()
    sleep(1)
    Sidetilside = 0
    Svingbanetur += 1
    return Rød()

state=Rød()
while True:
    while state: state=Rød()  # starter statemachine
    print ("Done with states")

