from tkinter import *
import c

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

inv = [("Выйти" , 90)]

sel = [("Цирк" , 1)]
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
for txt, val in sel:
    Radiobutton(ansFrame, text=txt, value=val, variable=choose, padx=15, pady=10, )\
        .grid(row=row, sticky=W)
    row += 1



def Refresh():
    for widget in ansFrame.winfo_children():
        widget.destroy()
        row = 2
    for txt, val in sel:
        Radiobutton(ansFrame, text=txt, value=val, variable=sel, padx=15, pady=10, )\
            .grid(row=row, sticky=W)
        row += 1    
def Print():
    textbox.insert(END,"\n ")
    textbox.insert(END, open(p, 'rt').read())
    textbox.yview(END)

def Start():
    c.Circus()

btn = Button(root, text="Нажать", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=Start())
btn.place(relx=1, rely=1, anchor="se", height=30, width=130, bordermode=INSIDE)



 
root.mainloop()
