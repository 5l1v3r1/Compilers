#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
# Compilers
# Coded by Senja
# Github: https://github.com/stepbystepexe/Compilers
from __opt__ import *
import os, sys, time, marshal
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
def py3():
        try:
                print
                a=input("\033[0m[\033[92;1m+\033[0m] \033[77;1mEnter the file name: \033[0m")
                x=open(a).read()
                b=compile(x,'','exec')
                c=marshal.dumps(b)
                d=open("theresults_"+a,'w')
                d.write('import marshal\n')
                d.write('exec(marshal.loads('+repr(c)+'))')
                d.close()
                time.sleep(1.5)
                print
                print("\033[0m[\033[94;1m@\033[0m] \033[77;1mFile Compiled Successfully: \033[0mtheresults_"+a)
                print
        except KeyboardInterrupt:
                print
                print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mERROR: MAKE SURE THE FILES WANT TO BE IN THE COMPILE ARE IN THE SAME FOLDERS AND MAKE SURE YOU ENTER THE FILE CORRECTLY")
                print
                exit(1)
def py2():
        try:
                print
                a=raw_input("\033[0m[\033[92;1m+\033[0m] \033[77;1mEnter the file name: \033[0m")
                x=open(a).read()
                b=compile(x,'','exec')
                c=marshal.dumps(b)
                d=open("theresults_"+a,'w')
                d.write('import marshal\n')
                d.write('exec(marshal.loads('+repr(c)+'))')
                d.close()
                time.sleep(1.5)
                print
                print("\033[0m[\033[94;1m@\033[0m] \033[77;1mFile Compiled Successfully: \033[0mtheresults_"+a)
                print
        except KeyboardInterrupt:
                print
                print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mERROR: MAKE SURE THE FILES WANT TO BE IN THE COMPILE ARE IN THE SAME FOLDERS AND MAKE SURE YOU ENTER THE FILE CORRECTLY")
                print
                exit(1)
def py1():
        try:
                print
                a=raw_input("\033[0m[\033[92;1m+\033[0m] \033[77;1mEnter the file name: \033[0m")
                x=open(a).read()
                b=compile(x,'','exec')
                c=marshal.dumps(b)
                d=open("theresults_"+a,'w')
                d.write('import marshal\n')
                d.write('exec(marshal.loads('+repr(c)+'))')
                d.close()
                time.sleep(1.5)
                print
                print("\033[0m[\033[94;1m@\033[0m] \033[77;1mFile Compiled Successfully: \033[0mtheresults_"+a)
                print
        except KeyboardInterrupt:
                print
                print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mERROR: MAKE SURE THE FILES WANT TO BE IN THE COMPILE ARE IN THE SAME FOLDERS AND MAKE SURE YOU ENTER THE FILE CORECTLY")
                print
                exit(1)
os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print("\033[106;90;1m[       Python Compilers v1.0, Coded by @stepbystep      ]\033[0m")
time.sleep(1)
print
print("\033[0m[\033[94;1m1\033[0m] \033[77;1mPython3.7")
print("\033[0m[\033[93;1m2\033[0m] \033[77;1mPython2.7")
print("\033[0m[\033[96;1m3\033[0m] \033[77;1mPython")
print("\033[0m[\033[91;1m0\033[0m] \033[77;1mExit")
print
option = raw_input("\n\033[0m[\033[95;1m/\033[0m] \033[77;1mSelect an option: \033[0m")
if option == '1' or option == '01':
    py3()
elif option == '2' or option == '02':
    py2()
elif option == '3' or option == '03':
    py1()
elif option == '0' or option == '00':
    print
    print("\033[0m[\033[91;1m!\033[0m] \033[77;1mExit the program!")
    print
    exit(1)

else:
        print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mInvalid option!")
        print
        time.sleep(1)
        restart_program()
