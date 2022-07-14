#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
import tkinter as tk
import tkinter.font as font

root=tk.Tk()
root.title('Penyandian Pesan Autokey Cipher Menggunakan Pertukaran Kunci Diffie Hellman')
canvas1=tk.Canvas(root, width=800, height=500,bg='LemonCHiffon')
canvas1.pack()
label01=tk.Label(root, text='1903685 Shellya Nur Atqiya',bg='LemonCHiffon',font=('Courier',8)).place(x=60,y=427)
label02=tk.Label(root, text='1903809 Razka Divaniza Mukti',bg='LemonCHiffon',font=('Courier',8)).place(x=300,y=427)
label03=tk.Label(root, text='1908977 Erina Nur Susilowati',bg='LemonCHiffon',font=('Courier',8)).place(x=550,y=427)

#ALICE       

def PUalice():
        def FPB(m,n):
            if m<n:
                o=m
                m=n
                n=o
            s=m%n
            while s!=0:
                m=n
                n=s
                s=m%n
            return n
    
        def cekprima(j):
            tes=0
            i=2
            while i <j:
                if FPB(j,i) == 1:
                    tes=tes+0
                elif FPB(j,i)!=1:
                    tes=tes+1
                i+=1
            return tes
        global na_entry, ga_entry, a_entry
        top1=Toplevel(root,width=800, height=400,bg='LemonChiffon')  
        top1.title('Diffie Hellman Alice')
        labelA1=tk.Label(top1, text = 'Masukkan bilangan prima n dan g yang telah disepakati bersama Bob',bg='LemonChiffon').place(x=230, y=50)
        na_label=tk.Label(top1, text = 'Nilai n : ',bg='LemonChiffon').place(x=230, y=80)
        na_entry=tk.Entry(top1)
        na_entry.place(x=471,y=80)
        ga_label=tk.Label(top1, text = 'Nilai g (g < n) : ',bg='LemonChiffon').place(x=230, y=110)
        ga_entry=tk.Entry(top1)
        ga_entry.place(x=471, y=110)
        labelA2=tk.Label(top1, text = 'Masukkan kunci privat x',bg='LemonChiffon').place(x=230, y=200)
        a_label=tk.Label(top1, text = 'Nilai x : ',bg='LemonChiffon').place(x=230, y=220)
        a_entry=tk.Entry(top1)
        a_entry.place(x=471,y=220)
        label3=tk.Label(top1, text = 'Masukkan kunci publik dari Bob, Y',bg='LemonChiffon').place(x=230, y=260)
        Y_label=tk.Label(top1, text = 'Nilai Y : ',bg='LemonChiffon').place(x=230, y=280)
        Y_entry=tk.Entry(top1)
        Y_entry.place(x=471,y=280)
        def PrimaA():
            na = na_entry.get()
            na = int(na)
            ga = ga_entry.get()
            ga = int(ga)
            if cekprima(na)>1:
                     hasilna = 'n bukan bilangan prima, ganti angka'
            elif cekprima(na)==0:
                     hasilna = 'n bilangan prima'
            if cekprima(ga)>1:
                     hasilga = 'g bukan bilangan prima, ganti angka'
            elif cekprima(ga)==0:
                     hasilga = 'g bilangan prima'
            label_prima =  tk.Label(top1, text = hasilna+ '\n' + hasilga, bg='LemonChiffon').place(x=375, y=160)
        def NilaiX():
            na = na_entry.get()
            na = int(na)
            ga = ga_entry.get()
            ga = int(ga)
            a = a_entry.get()
            a = int(a)
            X = (ga**a)%na
            X_label1 = tk.Label(top1, text = 'Berikut nilai kunci publik Alice,\n X = '+str(X),bg='LemonChiffon').place(x=230, y=340)
            return X
        def NilaiK():
            na = na_entry.get()
            na = int(na)
            a = a_entry.get()
            a = int(a)
            Y = Y_entry.get()
            Y = int(Y)
            K = (Y**a)%na
            K_label1 = tk.Label(top1, text = 'Berikut nilai kunci enkripsi, \n K = '+str(K),bg='LemonChiffon').place(x=450, y=340)
            return K
        def HelpA():
            top1a=Toplevel(root,width=800, height=400,bg='LemonChiffon') 
            top1a.title('Diffie Hellman Alice')
            def closehelp():
                top1a.destroy()
            H_label1=tk.Label(top1a, text = 'Langkah-langkah penggunaan program:\n\t \n> Kunci Publik Alice:\n\t 1. Alice dan Bob menyepakati dua bilangan prima yang besar, yaitu n dan g dengan g < n, input n dan g ke dalam program \n\t 2. Alice menginput suatu bilangan x yang akan menjadi kunci privat milik Alice, kunci x tidak boleh diketahui siapapun termasuk Bob \n\t 3. Tekan button "Kunci Publik X" \n\t 4. Maka kunci Alice adalah (n, g, x, X) dengan x merupakan kunci privat, kirimkan kunci publik X ke Bob \n\t \n > Kunci Enkripsi K: \n\t 1. Alice menginput dua bilangan prima yang besar n dan g yang telah disepakati dengan Bob \n\t 2. Alice menerima kunci publik Y milik Bob, input Y dan kunci privat x ke dalam program \n\t 3. Tekan button "Kunci Enkripsi K"\n\t  4. Alice mendapatkan kunci K yang dapat digunakan untuk mengenkripsi pesan',bg='LemonChiffon',justify=LEFT).pack()
            btnH=tk.Button(top1a,text='Close',bg='tomato',bd='5',command=closehelp).pack()
            
        def closeA():
            top1.destroy()
            
        btnA0=tk.Button(top1,text='Cek Prima',bg='PeachPuff',bd='5',command=PrimaA).place(x=380,y=130)    
        btnA1=tk.Button(top1,text='Kunci Publik X',bg='PeachPuff',bd='5',command=NilaiX).place(x=250,y=310)
        btnA2=tk.Button(top1,text='Kunci Enkripsi K',bg='PeachPuff',bd='5',command=NilaiK).place(x=480,y=310)
        btnA3=tk.Button(top1,text='Help',bg='PeachPuff',bd='5',command=HelpA).place(x=700,y=60)
        btnA4=tk.Button(top1,text='Close',bg='tomato',bd='5',command=closeA).place(x=700,y=100)

        
def PUbob():
        def FPB(m,n):
            if m<n:
                o=m
                m=n
                n=o
            s=m%n
            while s!=0:
                m=n
                n=s
                s=m%n
            return n
    
        def cekprima(j):
            tes=0
            i=2
            while i <j:
                if FPB(j,i) == 1:
                    tes=tes+0
                elif FPB(j,i)!=1:
                    tes=tes+1
                i+=1
            return tes
        global nb_entry, gb_entry, b_entry
        top2=Toplevel(root,width=800, height=400,bg='LemonChiffon')  
        top2.title('Diffie Hellman Bob')
        labelB1=tk.Label(top2, text = 'Masukkan bilangan prima n dan g yang telah disepakati bersama Alice',bg='LemonChiffon').place(x=230, y=50)
        nb_label=tk.Label(top2, text = 'Nilai n : ',bg='LemonChiffon').place(x=230, y=80)
        nb_entry=tk.Entry(top2)
        nb_entry.place(x=471,y=80)
        gb_label=tk.Label(top2, text = 'Nilai g (g < n) : ',bg='LemonChiffon').place(x=230, y=110)
        gb_entry=tk.Entry(top2)
        gb_entry.place(x=471, y=110)
        labelB2=tk.Label(top2, text = 'Masukkan kunci privat y',bg='LemonChiffon').place(x=230, y=200)
        b_label=tk.Label(top2, text = 'Nilai y : ',bg='LemonChiffon').place(x=230, y=220)
        b_entry=tk.Entry(top2)
        b_entry.place(x=471,y=220)
        label3=tk.Label(top2, text = 'Masukkan kunci publik dari Alice, X',bg='LemonChiffon').place(x=230, y=260)
        X_label=tk.Label(top2, text = 'Nilai X : ',bg='LemonChiffon').place(x=230, y=280)
        X_entry=tk.Entry(top2)
        X_entry.place(x=471,y=280)
        def PrimaB():
            nb = nb_entry.get()
            nb = int(nb)
            gb = gb_entry.get()
            gb = int(gb)
            if cekprima(nb)>1:
                     hasilnb = 'n bukan bilangan prima, ganti angka'
            elif cekprima(nb)==0:
                     hasilnb = 'n bilangan prima'
            if cekprima(gb)>1:
                     hasilgb = 'g bukan bilangan prima, ganti angka'
            elif cekprima(gb)==0:
                     hasilgb = 'g bilangan prima'
            label_prima =  tk.Label(top2, text = hasilnb+ '\n' + hasilgb, bg='LemonChiffon').place(x=375, y=160)
        def NilaiY():
            nb = nb_entry.get()
            nb = int(nb)
            gb = gb_entry.get()
            gb = int(gb)
            b = b_entry.get()
            b = int(b)
            Y = (gb**b)%nb
            Y_label1 = tk.Label(top2, text = 'Berikut nilai kunci publik Bob,\n Y= '+str(Y),bg='LemonChiffon').place(x=230, y=340)
            return Y
        def NilaiK():
            nb = nb_entry.get()
            nb = int(nb)
            b = b_entry.get()
            b = int(b)
            X = X_entry.get()
            X = int(X)
            K = (X**b)%nb
            K_label1 = tk.Label(top2, text = 'Berikut nilai kunci dekripsi, \n K = '+str(K),bg='LemonChiffon').place(x=450, y=340)
            return K
        def HelpB():
            top2a=Toplevel(root,width=800, height=400,bg='LemonChiffon')
            top2a.title('Diffie Hellman Bob')
            def closehelp():
                top2a.destroy()
            H_label1=tk.Label(top2a, text = 'Langkah-langkah penggunaan program:\n\t \n> Kunci Publik Bob :\n\t 1. Alice dan Bob menyepakati dua bilangan prima yang besar, yaitu n dan g dengan g < n, input n dan g ke dalam program \n\t 2. Bob menginput suatu bilangan y yang akan menjadi kunci privat milik Bob, kunci y tidak boleh diketahui siapapun termasuk Alice \n\t 3. Tekan button "Kunci Publik Y" \n\t 4. Maka kunci Bob adalah (n, g, y, Y) dengan y merupakan kunci privat, kirimkan kunci publik Y ke Alice \n\t \n > Kunci Dekripsi K: \n\t 1. Bob menginput dua bilangan prima yang besar n dan g yang telah disepakati dengan Alice \n\t 2. Bob menerima kunci publik X milik Alice, input X dan kunci privat y ke dalam program \n\t 3. Tekan button "Kunci Dekripsi K"\n\t  4. Bob mendapatkan kunci K yang dapat digunakan untuk mendekripsi pesan',bg='LemonChiffon',justify=LEFT).pack()
            btnH=tk.Button(top2a,text='Close',bg='tomato',bd='5',command=closehelp).pack()
            
        def closeB():
            top2.destroy()
            
        btnB0=tk.Button(top2,text='Cek Prima',bg='PeachPuff',bd='5',command=PrimaB).place(x=380,y=130)    
        btnB1=tk.Button(top2,text='Kunci Publik Y',bg='PeachPuff',bd='5',command=NilaiY).place(x=250,y=310)
        btnB2=tk.Button(top2,text='Kunci Dekripsi K',bg='PeachPuff',bd='5',command=NilaiK).place(x=480,y=310)
        btnB3=tk.Button(top2,text='Help',bg='PeachPuff',bd='5',command=HelpB).place(x=700,y=60)
        btnB4=tk.Button(top2,text='Close',bg='tomato',bd='5',command=closeB).place(x=700,y=100)


def Autokey():
        global key
        top3=Toplevel(root,width=800, height=300,bg='LemonChiffon')  
        top3.title('Autokey Cipher')
        labelAK1=tk.Label(top3, text = 'Masukkan Plainteks/Cipherteks (non-kapital):',bg='LemonChiffon').place(x=230, y=50)
        teks_label=tk.Label(top3, text = 'Teks : ',bg='LemonChiffon').place(x=230, y=80)
        teks_entry=tk.Entry(top3)
        teks_entry.place(x=471,y=80)
        labelAK2=tk.Label(top3, text = 'Masukkan Kunci yang didapat dari pertukaran Diffie Hellman:',bg='LemonChiffon').place(x=230, y=110)
        key_label=tk.Label(top3, text = 'Kunci (Angka) : ',bg='LemonChiffon').place(x=230, y=130)
        key_entry=tk.Entry(top3)
        key_entry.place(x=471,y=130)
        def kunci(pesan,k):
            a=len(pesan)
            for i in range(a-1):
                k=k+pesan[i]
            return k
        def enkrip():
            teks = teks_entry.get()
            key = key_entry.get()
            key = (int(key)%26)+97
            key = (chr(key))
            key = kunci(teks,key)
            a = len(teks)
            cipher =''
            for i in range(a):
                cipher=cipher+chr(((ord(teks[i])-97+ord(key[i])-97))%26+97)
            cipher_label = tk.Label(top3, text = 'Cipherteks : \n '+ cipher,bg='LemonChiffon').place(x=280, y=220)
        def dekrip():
            teks = teks_entry.get()
            key = key_entry.get()
            key = (int(key)%26)+97
            key = (chr(key))
            a = len(teks)
            plain =''
            for i in range(a):
                b=chr((ord(teks[i])-ord(key[i]))%26+97)
                plain=plain+b
                key=key+b
            plain_label = tk.Label(top3, text = 'Plainteks : \n '+ plain,bg='LemonChiffon').place(x=480, y=220)
        def closeC():
            top3.destroy()
        btnEnkrip = tk.Button(top3,text='Enkripsi',bg='PeachPuff',bd='5',command=enkrip).place(x=280,y=180)
        btnDekrip = tk.Button(top3,text='Dekripsi',bg='PeachPuff',bd='5',command=dekrip).place(x=480,y=180)
        btnClose=tk.Button(top3,text='Close',bg='tomato',bd='5',command=closeC).place(x=380,y=260)
        
def closeall():
    root.destroy()

        
#PROGRAM UTAMA
label1=tk.Label(root,text='Program Pertukaran Kunci Diffie Hellman',bg='LemonChiffon',font=('Arial Bold',15)).place(x=200,y=50)
label2=tk.Label(root,text='Pilih Karakter',bg='LemonCHiffon',font=('Arial Bold',15)).place(x=340,y=80)
btn1=tk.Button(text='Alice',bg='PeachPuff',bd='5',command=PUalice)
myFont = font.Font(family='Helvetica', size=20, weight='bold')
btn1['font'] = myFont
btn1.place(x=350,y=130)
btn2=tk.Button(text='Bob',bg='PeachPuff',bd='5',command=PUbob)
myFont = font.Font(family='Helvetica', size=20, weight='bold')
btn2['font'] = myFont
btn2.place(x=355,y=220)
label3=tk.Label(root,text='Program Penyandian Pesan Autokey Cipher',bg='LemonCHiffon',font=('Arial Bold',15)).place(x=200,y=300)
btn3=tk.Button(text='Penyandian Pesan',bg='PeachPuff',bd='5',command=Autokey)
btn3['font'] = myFont
btn3.place(x=260,y=340)
btn4=tk.Button(root,text='Close',bg='tomato',fg='black',bd='5',command=closeall).place(x=690,y=450)

root.mainloop()

