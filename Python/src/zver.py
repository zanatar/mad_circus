zver_d = {1: 'Осмотреться', 0: 'Уйти'}
seal_d = {9: 'Инвентарь', 0: 'Уйти'}
deer_d = {9: 'Инвентарь', 0: 'Уйти'}
pig_d = {1: 'Осмотреться', 0: 'Уйти'}


import way
import main
import cir

def Zver_way():
    if main.cfg['act3'] == True and 4 in zver_d:
        del zver_d[4]
    main.sel = zver_d
    main.Refresh()
    main.btn.config(command=Zver)

def Zver():
    
    x = main.choose.get()
    if x == 1:
        main.p = 'zver_start.txt'
        main.Print()
        zver_d[2] = 'Подойти к клетке с тюленем'
        zver_d[3] = 'Подойти к загону'
        if main.cfg['act3'] == False:
            main.p = 'В крайней правой клетке внимание привлекал чудовищно тощий олень с красным носом, прижимающийся к стенке клетки чтобы не свалиться.'
            main.Phrase()
            zver_d[4] = 'Подойти к клетке с оленем'
        main.cfg['zver_check'] = True
        main.Refresh()
    elif x == 2:
        main.p = 'Ян подошел к клетке с тюленем. Тюлень не реагирует'
        main.Phrase()
        Seal()
    elif x == 3:
        Pig()
    elif x == 4 and main.cfg['act3'] == False:
        main.p = 'Ян подошел к клетке о оленем'
        main.Phrase()
        Dir()
    elif x == 0:
        way.North()

def Seal():
    main.sel = seal_d
    main.Refresh()
    main.btn.config(command=Seal1)

def Seal1():
    x = main.choose.get()
    if x == 9:
        main.Inventory()
        main.btn.config(command=Seal2)
    elif x == 0:
        Zver_way()

def Seal2():
    i = main.choose.get()
    if i == 90:
        Seal()
    elif i == 3:
        main.p = 'Ян кинул морковку тюленю. Тюлень никак на нее не прореагировал. Очевидно, тюлени морковку не едят'
        main.Phrase()
        del main.inv[3]
        Seal()
    elif i == 25:
        main.p = 'zver_ring.txt'
        main.Print()
        main.cfg['circus_end'] = True
        del main.inv[25]
        main.inv[26] = 'Перстень дожа'
        main.sel = {1: 'Переместиться в большой шатер'}
        main.Refresh()
        main.btn.config(command=Seal3)


def Seal3():
    x = main.choose.get()
    if x == 1:
        cir.Circus()

def Pig():
    main.sel = pig_d
    main.Refresh()
    main.btn.config(command=Pig1)

def Pig1():
    x = main.choose.get()
    if x == 1:
        if main.cfg['zver_pig_kaboom'] == False:
            main.p = 'zver_pig.txt'
            main.Print()
            pig_d[9] = 'Инвентарь'
            main.Refresh()
        elif main.cfg['zver_pig_kaboom'] == True:
            main.p =  'Загон пуст и лишь пятна крови и жира тут и там напоминают о случившейся трагедии.'
            main.Phrase()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Pig2)
    elif x == 0:
        Zver_way()


def Pig2():
    i = main.choose.get()
    if i == 90:
        Seal()
    elif i == 3:
        main.p = 'Ян кинул морковку в открытую пасть свиньи. Пасть захлопнулась.'
        main.Phrase()
        del main.inv[3]
        Pig()
    elif i == 9:
        main.p = 'Ян кинул шашечку динамита в открытую пасть свиньи. Пасть захлопнулась.'
        main.Phrase()
        main.cfg['zver_pig_armed'] = True
        del main.inv[9]
        Pig()
    elif i == 7 and main.cfg['zver_pig_armed'] == True:
        main.p = 'zver_armed.txt'
        main.Print()
        main.sel = {1: 'Катарсис, очищение, да, да, да!!!'}
        main.Refresh()
        main.btn.config(command=Pig3)

def Pig3():
    x = main.choose.get()
    if x == 1:
        main.p = 'zver_kaboom.txt'
        main.Print()
        main.cfg['zver_pig_kaboom'] = True
        main.inv[12] = 'Шматок сала'
        del pig_d[9]
        Zver_way()
    
    

def Dir():
    main.sel = deer_d
    main.Refresh()
    main.btn.config(command=Dir1)

def Dir1():
    x = main.choose.get()
    if x == 9:
        main.Inventory()
        main.btn.config(command=Dir2)
    elif x == 0:
        Zver_way()

def Dir2():
    i = main.choose.get()
    if i == 90:
        Seal()
    elif i == 3:
        main.p = 'Ян кинул  морковку оленю. Тот попытался нагнуться и ухватить ее, но подгибающиеся ноги чуть было не подвели его и он не рискнул. В глазах его застыла вселенская тоска.'
        main.Phrase()
        del main.inv[3]
        Dir()





    
