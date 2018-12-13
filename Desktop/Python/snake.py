import time
import getpass
import curses
import threading
import random
import RPi.GPIO as GPIO
from os import system, name

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

class Snake:
    def __init__ (self, l_snake, h_snake, larg, alt, fru_larg, fru_alt, l_bef, h_bef, score):
        self.Matrix = [[0 for x in range(larg)] for y in range(alt)] 
        self.larg = larg
        self.alt = alt
        self.fora = 0
        for x in range (0, self.larg):
            for y in range (0, self.alt):
                self.Matrix[y][x] = "-"

        self.Matrix[fru_larg][fru_alt] = "U"        
        self.Matrix[l_snake][h_snake] = "O"
        print("#######SNAKE##FODA#######")    
        for j in range (0, score):
            if score != 0:
                self.Matrix[l_bef[j]][h_bef[j]] = "O"
                if l_snake == l_bef[j] and h_snake == h_bef[j]:
                    self.fora = 1           
                  

def prin():
    larg    = 10
    alt     = 15 
    l_snake = 6
    h_snake = 5
    fru_larg = random.randint(0,9)
    fru_alt = random.randint(0,9)
    score = 0
    cont_lista = 0
    l_bef = []
    h_bef = []
    ent2 = "Q"
    ult_ent = "w"
    while True:
        global cont
        global ent      
        global got_fru
        if cont == 1:
            ent2 = "a"
        elif cont == 2:
            ent2 = "w"
        elif cont == 3:
            ent2 = "a"
        elif cont == 4:
            ent2 = "w"
        if ent2 == "s":
            h_snake = h_snake +1
            ult_ent = ent2
        elif ent2 == "w":
            h_snake = h_snake -1
            ult_ent = ent2
        elif ent2 == "a":
            l_snake = l_snake -1
            ult_ent = ent2
        elif ent2 == "d":
            l_snake = l_snake +1
            ult_ent = ent2
        else:
            if ult_ent == "s":
                h_snake = h_snake +1
            if ult_ent == "w":
                h_snake = h_snake -1
            if ult_ent == "a":
                l_snake = l_snake -1
            if ult_ent == "d":
                l_snake = l_snake +1
        l_bef.append(l_snake)
        h_bef.append(h_snake)
        Matrix = Snake(l_snake, h_snake, larg, alt, fru_larg, fru_alt, l_bef, h_bef, score)     
        if Matrix.Matrix[l_snake][h_snake] == Matrix.Matrix[fru_larg][fru_alt]:
            score = score + 1
            fru_larg = random.randint(0,9)
            fru_alt = random.randint(0,9)           
        for x in range (0,Matrix.larg):
            for y in range (0,Matrix.alt):
                print(Matrix.Matrix[y][x], end="")
            print("")
        print("")
        if cont_lista == score:
            l_bef.pop(0)
            h_bef.pop(0)
        elif cont_lista < score:
            cont_lista = cont_lista + 1
            #print("pop")
        if Matrix.fora == 1:
            break
        print("SCORE:",  score)
        time.sleep(0.8)        
        clear()

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 


def inputa():
    while True:
        global ent
        ent = getpass.getpass("")

def callback(channel):
    global cont
    if GPIO.input(channel):
        cont = cont + 1
        print(cont)
    else:
        cont = cont + 1
        print(cont)
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

def sensor():
# infinite loop
    global cont
    while True:
        cont = 0
        time.sleep(3)

clear()
got_fru = 0
ent = "s"
cont = 0
t1 = threading.Thread(target= prin)
t2 = threading.Thread(target=sensor )
t1.start()
t2.start()
t1.join()
t2.join()
