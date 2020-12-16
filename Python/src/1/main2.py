from tkinter import *
chooses = [("act1" , 90), ("act2", 2), ("act3", 99), ]

root = Tk()
root.title("Итицкий цирк")


textFrame = Frame(root, height = 340, width = 600)
textFrame.pack(side = 'top', fill = 'both', expand = 1)

ansFrame = Frame(root, height = 60, )
ansFrame.pack(side = 'bottom', fill = 'x')

def click_button():
    global chooses
    l = choose.get()
    if l == 90:
        textbox.insert(END,"\n ")
        textbox.insert(END, open('circus_act11.txt', 'rt').read())
        row = 2
        for txt, val in chooses:
            Radiobutton(ansFrame, text=txt, value=val, variable=choose, padx=15, pady=10, )\
        .grid(row=row, sticky=W)
        row += 1
    elif l == 2:
        textbox.insert(END,"\n ")
        textbox.insert(END, open('circus_act12.txt', 'rt').read())
        row = 2
        for txt, val in chooses:
            Radiobutton(ansFrame, text=txt, value=val, variable=choose, padx=15, pady=10, )\
        .grid(row=row, sticky=W)
        row += 1

choose = IntVar()

row = 2
for txt, val in chooses:
    Radiobutton(ansFrame, text=txt, value=val, variable=choose, padx=15, pady=10, )\
        .grid(row=row, sticky=W)
    row += 1
textbox = Text(textFrame, font='Arial 14', wrap=WORD)
textbox.pack(expand = True, fill=BOTH)
scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

btn = Button(root, text="Нажать", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.place(relx=1, rely=1, anchor="se", height=30, width=130, bordermode=INSIDE)

 
root.mainloop()
