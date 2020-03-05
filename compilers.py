#!/usr/bin/python
# -*- coding: utf-8 -*-
# Compilers
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Compilers

import io, os, sys, time, random, marshal
from time import sleep

info = """
Nama        : Compilers
Versi       : 2.1 (Update: 15 Oktober 2020, 4:00 PM)
Tanggal     : 05 April 2019
Author      : Nedi Senja
Tujuan      : Untuk mengcompile Python
              python3.7 dan python.2.7
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[106;90;1m[          Compilers, My Github: @stepbystepexe          ]\033[0m"""

logo = """
 \033[0;91m█▀▀▀▀ █▀▀▀█ █▀█▀█ █▀▀▀█ ▀▀█▀▀ █     █▀▀▀▀   \033[0;37m█▀▀▀█ █   █
 \033[0;91m█     █   █ █ ▀ █ █▀▀▀▀   █   █     █▀▀▀    \033[0;37m█▀▀▀▀ ▀▀█▀▀
 \033[0;91m▀▀▀▀▀ ▀▀▀▀▀ ▀   ▀ ▀     ▀▀▀▀▀ ▀▀▀▀▀ ▀▀▀▀▀ \033[0;90m▀ \033[0;37m▀       ▀
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    o = [
     '.   ','..  ','... ']
    for i in o:
        print '\r\033[0m[\033[0;33m●\033[0m] Sedang mengcompile ' +i,
        sys.stdout.flush()
        time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def home():
    os.system('clear')
    os.system('reset')
    sleep(1)
    print
    print(logo)
    print(example)
    print
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mFile harus berada dalam satu folder yang sama")
    write("         Jikalau tidak ya otomatis gx bisa dicompile lah\033[0m\n")

def python3():
        try:
                home()
                sch = input("\n\033[0m[\033[41;77;1m File \033[0m] ")
                exe = open(sch).read()
                bom = compile(exe,'','exec')
                cif = marshal.dumps(bom)
                die = open("save."+sch,'w')
                die.write('import marshal\n')
                die.write('exec(marshal.loads('+repr(cif)+'))')
                die.close()
                print
                loads()
                sleep(1)
                print("\n\033[0m[\033[94;1m#\033[0m] \033[77;1mBerhasil dicompile: \033[0msave."+sch+"\n")
                o = raw_input("\033[0m[\033[96;1m?\033[0m] Buka file [Y/n]: ")
                if o.strip() in 'Y y'.split():
                    print
                    os.system('nano save.'+sch)
                    print
                    sys.exit(1)
                elif o.strip() in 'N n'.split():
                    restart()
                else:
                    restart()
        except IOError:
                print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mGagal mengcompile\033[0m\n")
                sys.exit(1)
def python2():
        try:
                home()
                sch = raw_input("\n\033[0m[\033[41;77;1m File \033[0m] ")
                exe = open(sch).read()
                bom = compile(exe,'','exec')
                cif = marshal.dumps(bom)
                die = open("save."+sch,'w')
                die.write('import marshal\n')
                die.write('exec(marshal.loads('+repr(cif)+'))')
                die.close()
                print
                loads()
                sleep(1)
                print("\n\033[0m[\033[94;1m#\033[0m] \033[77;1mBerhasil dicompile: \033[0msave."+sch+"\n")
                o = raw_input("\033[0m[\033[96;1m?\033[0m] Buka file [Y/n]: ")
                if o.strip() in 'Y y'.split():
                    print
                    os.system('nano save.'+sch)
                    print
                    sys.exit(1)
                elif o.strip() in 'N n'.split():
                    restart()
                else:
                    restart()
        except IOError:
                print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mGagal mengcompile\033[0m")
                sys.exit(1)

os.system('clear')
os.system('reset')
sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[96;2;1m1\033[0m] \033[77;1mPython3.7")
print("\033[0m[\033[96;2;1m2\033[0m] \033[77;1mPython2.7")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m[\033[95;1m/\033[0m] \033[77;1mMasukan opsi: \033[0m")
if option.strip() in '1 python3'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    python3()
elif option.strip() in '2 python2'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    python2()
elif option.strip() in '& 3 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 4 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Marshal')
    print(info)
    sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 5 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 0 keluar'.split():
    print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mKeluar dari program!\n")
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]\n")
    sleep(1)
    restart()
