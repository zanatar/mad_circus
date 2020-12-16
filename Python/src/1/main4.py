from tkinter import *
import cir
import zak
import toi
import way
import slon
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
       'ride_pony_drunk': '0',
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

inv = {90: "Выйти",  

       12: 'Шматок сала' , 13: 'Глобус Украины' ,
       1: 'Сколопендра',15 : 'Стальное яйцо' 
        
       }

sel = {1: 'Цирк'}
p = 'start.txt'

root = Tk()
root.title("Итицкий цирк")


textFrame = Frame(root, height = 340, width = 600)
textFrame.pack(side = 'top', fill = 'both', expand = 1)

ansFrame = Frame(root, height = 60, )
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
    textbox.insert(END,"\n ")
    textbox.insert(END, open(p, 'rt').read())
    textbox.yview(END)

def Phrase():
    textbox.insert(END,"\n ")
    textbox.insert(END, p)
    textbox.yview(END)

def Start():
    way.West()

    

#selection = Label(textvariable=choose, padx=15, pady=10)
#selection.pack(side = 'right', fill = 'x')



btn = Button(root, text="Нажать", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=Start)
btn.place(relx=1, rely=1, anchor="se", height=30, width=130, bordermode=INSIDE)

def Circus():
    global sel
    global p
    global cfg
    if cfg['act2'] == False:
        if cfg['circus_check'] == False:
            cfg['circus_check'] = True
            p = 'circus_act11.txt'
            Print()
            sel = [('Зайти в шатер' , 1)]
            Refresh()
            btn.config(command=Circus1)


#def Circus1():
#    global sel
#    global p
#    p = 'circus_act12.txt'
#    Print()
#    sel = [('Дождаться начала представления' , 1)]
#    Refresh()
#    btn.config(command=Circus2)

def Circus2():
    global sel
    global p
    p = 'circus_act21.txt'
    Print()
    sel = [('11' , 1)]
    Refresh()
    btn.config(command=Circus2)
Print()

root.mainloop()

##inv = {1: 'Сколопендра', 2: 'Бутылка водки',3: 'Морковка', 4: 'Дохлая мышь' ,
##      5: 'Ржавая ножовка' , 6: 'Обломок трембиты' , 0: 'Выйти', 8: 'Пустая бутылка' ,
##       9: 'Шашечка динамита' , 7: 'Зажигалка' , 10: 'Бутылка с пургеном',
##       11: 'Шприц с адреналином' , 
##       12: 'Шматок сала' , 13: 'Глобус Украины' , 14: 'Отрезанный член'
##            15 : 'Стальное яйцо' , 16: 'Пустой бочонок', 17: 'Бочонок слоновьего жира' ,
##   18:'Гиря' , 
## 22: 'Крючок' , 23: 'Веревка' , 24: 'Жердина' , 25: 'Рыба фугу', 
##      26: 'Перстень дожа' }
