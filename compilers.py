#!/usr/bin/python
# -*- coding: utf-8 -*-
# Compilers
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Compilers

from __opt__ import *
import os, sys, time, marshal

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

example = """\033[106;90;1m[       Python Compilers, My Github: @stepbystepexe      ]\033[0m"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def python3():
        try:
                print
                a=input("\033[0m[\033[92;1m+\033[0m] \033[77;1mMasukan nama berkas: \033[0m")
                x=open(a).read()
                b=compile(x,'','exec')
                c=marshal.dumps(b)
                d=open("theresults_"+a,'w')
                d.write('import marshal\n')
                d.write('exec(marshal.loads('+repr(c)+'))')
                d.close()
                time.sleep(1.5)
                print
                print("\033[0m[\033[94;1m@\033[0m] \033[77;1mBerkas berhasil dicompile: \033[0mcompile_"+a)
                print
        except KeyboardInterrupt:
                print
                print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mGagal. [ INFO ] berkas harus berada dalam satu folder")
                print
                sys.exit(1)
def python2():
        try:
                print
                a=raw_input("\033[0m[\033[92;1m+\033[0m] \033[77;1mMasukan nama berkas: \033[0m")
                x=open(a).read()
                b=compile(x,'','exec')
                c=marshal.dumps(b)
                d=open("theresults_"+a,'w')
                d.write('import marshal\n')
                d.write('exec(marshal.loads('+repr(c)+'))')
                d.close()
                time.sleep(1.5)
                print
                print("\033[0m[\033[94;1m@\033[0m] \033[77;1mBerkas berhasil dicompile: \033[0mcompile_"+a)
                print
        except KeyboardInterrupt:
                print
                print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mGagal. [ INFO ] berkas harus berada dalam satu folder")
                print
                sys.exit(1)
def python():
        try:
                print
                a=raw_input("\033[0m[\033[92;1m+\033[0m] \033[77;1mMasukan nama berkas: \033[0m")
                x=open(a).read()
                b=compile(x,'','exec')
                c=marshal.dumps(b)
                d=open("theresults_"+a,'w')
                d.write('import marshal\n')
                d.write('exec(marshal.loads('+repr(c)+'))')
                d.close()
                time.sleep(1.5)
                print
                print("\033[0m[\033[94;1m@\033[0m] \033[77;1mBerkas berhasil dicompile: \033[0mcompile_"+a)
                print
        except KeyboardInterrupt:
                print
                print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mGagal. [ INFO ] berkas harus berada dalam satu folder")
                print
                sys.exit(1)

os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[96;2;1m1\033[0m] \033[77;1mPython3.7")
print("\033[0m[\033[96;2;1m2\033[0m] \033[77;1mPython2.7")
print("\033[0m[\033[96;2;1m3\033[0m] \033[77;1mPython")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\n\033[0m[\033[95;1m/\033[0m] \033[77;1mMasukan opsi: \033[0m")
if option == '1' or option == '01':
    python3()
elif option == '2' or option == '02':
    python2()
elif option == '3' or option == '03':
    python()
elif option.strip() in '& 4 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 5 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Marshal')
    print(info)
    time.sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 6 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 7 keluar'.split():
    print
    print("\033[0m[\033[91;1m!\033[0m] \033[77;1mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    time.sleep(1)
    restart()
