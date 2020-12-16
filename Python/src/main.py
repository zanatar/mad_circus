from tkinter import *
import cir
import zak
import toi
import way
import slon
import shutil
import way
import sys
import pickle
import os
cfg = {'zak_prod' : True ,
       'zak_drunk':True ,
       'drunk_event':False ,
       'drunk_fail':False ,
       'toi_tab':False ,
       'toi_sw':False ,
       'toi_brake':False ,
       'slon_check':False ,#
       'slon_talk':False ,
       'slon_ass_lube':False ,
       'slon_din_arm':False ,
       'act2':False ,
       'act3':False ,
       'zak_check':False,
       'zak_mouse': False,
       'zak_desk_check':False ,
       'tir_win':False ,
       'tir_dyn':False ,
       'shoot_check':False ,
       'shoot_drunk':False ,
       'zver_check':False ,
       'zver_pig_check':False ,
       'zver_pig_armed':False ,
       'zver_pig_kaboom':False ,
       'pool_check':False ,
       'pool_inv':False ,
       'pool_clean':False ,
       'pool_calm':False ,
       'pool_swim':False ,
       'pool_fishing':False ,
       'pool_rod': 0 ,
       'stage_end1':False ,
       'stage_listen':False ,
       'stage_end3':False ,
       'stage_request':False ,
       'stage_rom_new': False,
       'stage_rom_vodka':False ,
       'ride_check1':False ,
       'ride_skol':False ,
       'ride_end1':False ,
       'ride_end3':False ,
       'ride_check3':False,
       'ride_carrots':0 ,
       'ride_pony_check':False ,
       'ride_pony_drunk': 0 ,
       'ride_deer_check':False ,
       'deer_rush':False ,
       'jong_end1':False ,
       'jong_end3':False ,
       'jong_lynch':0 ,
       'jong_rep':1,
       'trailer_amput':False ,
       'trailer_kill':False ,
       'trailer_check':False ,
       'circus_check': False, 
       'circus_act2_start':False ,
       'circus_elef_check':False ,
       'circus_end':False ,
       'circus_bomb':0
         }

inv = {90: "Выйти",       }
saves = {  0: 'Выйти',}
saves_all = {1: 'Запись 1', 2: 'Запись 2', 3: 'Запись 3', 4: 'Запись 4', 5: 'Запись 5',
             6: 'Запись 6', 7: 'Запись 7', 8: 'Запись 8', 0: 'Выйти'}
exit_check = {1: 'Да' , 2: 'Нет'}
sel = {1: 'Новая игра' , 2: 'Загрузить игру',  0: 'Выйти'}
p = 'start.txt'

root = Tk()
root.title("Итицкий цирк")



textFrame = Frame(root, height = 340, width = 600)
textFrame.pack(side = 'top', fill = 'both', expand = 1)

ansFrame = Frame(root, height = 120, width = 600)
ansFrame.pack(side = 'bottom', fill = 'x')

textbox = Text(textFrame, font='Arial 14', wrap=WORD)
textbox.pack(expand = True, fill=BOTH)
scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

choose = IntVar()


row = 2
for val, txt in sel.items():
    Radiobutton(ansFrame, text=txt, value=val, variable=choose, padx=15, pady=10, )\
        .grid(row=row, sticky=W)
    row += 1



def Refresh():
    for widget in ansFrame.winfo_children():
        widget.destroy()
    row = 2
    column = 2
    for val, txt in sel.items():
        Radiobutton(ansFrame, text=txt, value=val, variable=choose, padx=15, pady=10, )\
            .grid(row=row,column=column, sticky=W)
        row += 1
        if row == 6:
            row = 2
            column +=1

def Inventory():
    for widget in ansFrame.winfo_children():
        widget.destroy()
    row = 2
    column = 2
    for val, txt in inv.items():
        Radiobutton(ansFrame, text=txt, value=val, variable=choose, padx=15, pady=10, )\
            .grid(row=row,column=column, sticky=W)
        row += 1
        if row == 6:
            row = 2
            column +=1

def Print():
    textbox.insert(END,"\n \n \n ")
    textbox.insert(END, open(p, 'rt').read())
    textbox.yview(END)

def Phrase():
    textbox.insert(END,"\n \n \n  ")
    textbox.insert(END, p)
    textbox.yview(END)

def Start():
    global p
    global sel
    x = choose.get()
    if x == 1:
        p = 'intro1.txt'
        Print()
        sel = {1: 'Продолжить'}
        Refresh()
        btn.config(command=Intro)
    elif x == 2:
        Load()
    elif x == 0:
        p = 'До скорой встречи!'
        Phrase()
        root.destroy()

def Load():
    Saves()
    btn.config(command=Load1)


def Saves():
    global p
    global sel
    if os.path.isfile('save1.txt') == True:
        saves[1] = 'Запись 1'
    if os.path.isfile('save2.txt') == True:
        saves[2] = 'Запись 2'
    if os.path.isfile('save3.txt') == True:
        saves[3] = 'Запись 3'
    if os.path.isfile('save4.txt') == True:
        saves[4] = 'Запись 4'
    if os.path.isfile('save5.txt') == True:
        saves[5] = 'Запись 5'
    if os.path.isfile('save6.txt') == True:
        saves[6] = 'Запись 6'
    if os.path.isfile('save7.txt') == True:
        saves[7] = 'Запись 7'
    if os.path.isfile('save8.txt') == True:
        saves[8] = 'Запись 8'
    sel = saves
    Refresh()
    

def Load1():
    global inv
    global cfg
    global p
    global sel
    x = choose.get()
    if x == 1:
        with open('save1.txt','rb') as save:
            cfg = pickle.load(save)
        with open('save1_inv.txt', 'rb') as save1:
            inv = pickle.load(save1)
        p = 'И снова стоит Ян у входа в цирк, но деяния его не забыты и достижения наличествуют'
        Phrase()
        way.West()
    elif x == 2:
        with open('save2.txt','rb') as save:
            cfg = pickle.load(save)
        with open('save2_inv.txt', 'rb') as save1:
            inv = pickle.load(save1)
        p = 'И снова стоит Ян у входа в цирк, но деяния его не забыты и достижения наличествуют'
        Phrase()
        way.West()
    elif x == 3:
        with open('save3.txt','rb') as save:
            cfg = pickle.load(save)
        with open('save3_inv.txt', 'rb') as save1:
            inv = pickle.load(save1)
        p = 'И снова стоит Ян у входа в цирк, но деяния его не забыты и достижения наличествуют'
        Phrase()
        way.West()
    elif x == 4:
        with open('save4.txt','rb') as save:
            cfg = pickle.load(save)
        with open('save4_inv.txt', 'rb') as save1:
            inv = pickle.load(save1)
        p = 'И снова стоит Ян у входа в цирк, но деяния его не забыты и достижения наличествуют'
        Phrase()
        way.West()
    elif x == 5:
        with open('save5.txt','rb') as save:
            cfg = pickle.load(save)
        with open('save5_inv.txt', 'rb') as save1:
            inv = pickle.load(save1)
        p = 'И снова стоит Ян у входа в цирк, но деяния его не забыты и достижения наличествуют'
        Phrase()
        way.West()
    elif x == 6:
        with open('save6.txt','rb') as save:
            cfg = pickle.load(save)
        with open('save6_inv.txt', 'rb') as save1:
            inv = pickle.load(save1)
        p = 'И снова стоит Ян у входа в цирк, но деяния его не забыты и достижения наличествуют'
        Phrase()
        way.West()
    elif x == 7:
        with open('save7.txt','rb') as save:
            cfg = pickle.load(save)
        with open('save7_inv.txt', 'rb') as save1:
            inv = pickle.load(save1)
        p = 'И снова стоит Ян у входа в цирк, но деяния его не забыты и достижения наличествуют'
        Phrase()
        way.West()
    elif x == 8:
        with open('save8.txt','rb') as save:
            cfg = pickle.load(save)
        with open('save8_inv.txt', 'rb') as save1:
            inv = pickle.load(save1)
        p = 'И снова стоит Ян у входа в цирк, но деяния его не забыты и достижения наличествуют'
        Phrase()
        way.West()
    elif x == 0:
        sel = {1: 'Новая игра' , 2: 'Загрузить игру',  0: 'Выйти'}
        Refresh()
        btn.config(command=Start)
        

def Intro():
    global p
    global sel
    x = choose.get()
    if x == 1:
        p = 'intro2.txt'
        Print()
        sel = {1: 'Продолжить'}
        Refresh()
        btn.config(command=Intro1)
def Intro1():
    global p
    global sel
    x = choose.get()
    if x == 1:
        p = 'intro3.txt'
        Print()
        sel = {1: 'И...???'}
        Refresh()
        btn.config(command=Intro2)
        
def Intro2():
    global p
    global sel
    x = choose.get()
    if x == 1:
        p = 'intro4.txt'
        Print()
        sel = {1: '"Помочь" Яну'}
        Refresh()
        btn.config(command=Intro3)

def Intro3():
    x = choose.get()
    if x == 1:
        way.West()

def Exit():
    global p
    global sel
    p = 'Уверены, что хотите покинуть игру?'
    Phrase()
    sel = exit_check
    Refresh()
    btn.config(command=Exit1)

def Exit1():
    global p
    global sel
    x = choose.get()
    if x == 1:
        p = 'Сохранить достигнутое?'
        Phrase()
        btn.config(command=Exit2)
    elif x == 2:
        way.West()



def Exit2():
    global sel
    x = choose.get()
    if x == 1:
        sel = saves_all
        Refresh()
        btn.config(command=Exit3)
    elif x == 2:
        root.destroy()
    



def Exit3():
    global sel
    global p
    x = choose.get()
    if x == 1:
        if os.path.isfile('save1.txt') == True:
            p = 'Запись  существует. Удалить?'
            Phrase()
            sel = exit_check
            Refresh()
            btn.config(command=Conf1)
        elif os.path.isfile('save1.txt') == False:
            with open('save1.txt','wb') as save:
                pickle.dump(cfg,save)
            with open('save1_inv.txt','wb') as save1:
                pickle.dump(inv,save1)
            root.destroy()
    elif x == 2:
        if os.path.isfile('save2.txt') == True:
            p = 'Запись  существует. Удалить?'
            Phrase()
            sel = exit_check
            Refresh()
            btn.config(command=Conf2)
        elif os.path.isfile('save2.txt') == False:
            with open('save2.txt','wb') as save:
                pickle.dump(cfg,save)
            with open('save2_inv.txt','wb') as save1:
                pickle.dump(inv,save1)
            root.destroy()
    elif x == 3:
        if os.path.isfile('save3.txt') == True:            
            p = 'Запись  существует. Удалить?'
            Phrase()
            sel = exit_check
            Refresh()
            btn.config(command=Conf3)
        elif os.path.isfile('save3.txt') == False:
             
            with open('save3.txt','wb') as save:
                pickle.dump(cfg,save)
            with open('save3_inv.txt','wb') as save1:
                pickle.dump(inv,save1)
            root.destroy()
    elif x == 4:
        if os.path.isfile('save4.txt') == True:
            p = 'Запись  существует. Удалить?'
            Phrase()
            sel = exit_check
            Refresh()
            btn.config(command=Conf4)
        elif os.path.isfile('save4.txt') == False:
            with open('save4.txt','wb') as save:
                pickle.dump(cfg,save)
            with open('save4_inv.txt','wb') as save1:
                pickle.dump(inv,save1)
            root.destroy()
    elif x == 5:
        if os.path.isfile('save5.txt') == True:
            p = 'Запись  существует. Удалить?'
            Phrase()
            sel = exit_check
            Refresh()
            btn.config(command=Conf5)
        elif os.path.isfile('save51.txt') == False:
            with open('save5.txt','wb') as save:
                pickle.dump(cfg,save)
            with open('save5_inv.txt','wb') as save1:
                pickle.dump(inv,save1)
            root.destroy()
    elif x == 6:       
        if os.path.isfile('save6.txt') == True:
            p = 'Запись  существует. Удалить?'
            Phrase()
            sel = exit_check
            Refresh()
            btn.config(command=Conf6)
        elif os.path.isfile('save6.txt') == False:
            with open('save6.txt','wb') as save:
                pickle.dump(cfg,save)
            with open('save6_inv.txt','wb') as save1:
                pickle.dump(inv,save1)
            root.destroy()
    elif x == 7:
        if os.path.isfile('save7.txt') == True:
            p = 'Запись  существует. Удалить?'
            Phrase()
            sel = exit_check
            Refresh()
            btn.config(command=Conf7)
        elif os.path.isfile('save7.txt') == False:
            with open('save7.txt','wb') as save:
                pickle.dump(cfg,save)
            with open('save7_inv.txt','wb') as save1:
                pickle.dump(inv,save1)
            root.destroy()
    elif x == 8:
        if os.path.isfile('save8.txt') == True:
            p = 'Запись  существует. Удалить?'
            Phrase()
            sel = exit_check
            Refresh()
            btn.config(command=Conf8)
        elif os.path.isfile('save7.txt') == False:
            with open('save8.txt','wb') as save:
                pickle.dump(cfg,save)
            with open('save8_inv.txt','wb') as save1:
                pickle.dump(inv,save1)
            root.destroy()
    elif x == 0:
        way.West()

def Conf1():
    global inv
    global cfg
    x = choose.get()
    if x == 1:
        with open('save1.txt','wb') as save:
            pickle.dump(cfg,save)
        with open('save1_inv.txt','wb') as save1:
            pickle.dump(inv,save1)
        root.destroy()
    elif x == 2:
        Exit()

def Conf2():
    global inv
    global cfg
    x = choose.get()
    if x == 1:
        with open('save2.txt','wb') as save:
            pickle.dump(cfg,save)
        with open('save2_inv.txt','wb') as save1:
            pickle.dump(inv,save1)
        root.destroy()
    elif x == 2:
        Exit()
    
def Conf3():
    global inv
    global cfg
    x = choose.get()
    if x == 1:
        with open('save3.txt','wb') as save:
            pickle.dump(cfg,save)
        with open('save3_inv.txt','wb') as save1:
            pickle.dump(inv,save1)
        root.destroy()
    elif x == 2:
        Exit()
def Conf4():
    global inv
    global cfg
    x = choose.get()
    if x == 1:
        with open('save4.txt','wb') as save:
            pickle.dump(cfg,save)
        with open('save4_inv.txt','wb') as save1:
            pickle.dump(inv,save1)
        root.destroy()
    elif x == 2:
        Exit()
def Conf5():
    global inv
    global cfg
    x = choose.get()
    if x == 1:
        with open('save5.txt','wb') as save:
            pickle.dump(cfg,save)
        with open('save5_inv.txt','wb') as save1:
            pickle.dump(inv,save1)
        root.destroy()
    elif x == 2:
        Exit()

def Conf6():
    global inv
    global cfg
    x = choose.get()
    if x == 1:
        with open('save6.txt','wb') as save:
            pickle.dump(cfg,save)
        with open('save6_inv.txt','wb') as save1:
            pickle.dump(inv,save1)
        root.destroy()
    elif x == 2:
        Exit()

def Conf7():
    global inv
    global cfg
    x = choose.get()
    if x == 1:
        with open('save7.txt','wb') as save:
            pickle.dump(cfg,save)
        with open('save7_inv.txt','wb') as save1:
            pickle.dump(inv,save1)
        root.destroy()
    elif x == 2:
        Exit()
def Conf8():
    global inv
    global cfg
    x = choose.get()
    if x == 1:
        with open('save8.txt','wb') as save:
            pickle.dump(cfg,save)
        with open('save8_inv.txt','wb') as save1:
            pickle.dump(inv,save1)
        root.destroy()
    elif x == 2:
        Exit()



btn = Button(root, text="OK", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=Start)
btn.place(relx=1, rely=1, anchor="se", height=30, width=130, bordermode=INSIDE)


Print()
root.protocol('WM_DELETE_WINDOW', Exit)
root.mainloop()

