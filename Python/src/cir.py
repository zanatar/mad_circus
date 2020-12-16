import main
import way

def Circus():
    if main.cfg['act2'] == False:
        if main.cfg['circus_check'] == False:
            main.cfg['circus_check'] = True
            main.p = 'circus_act11.txt'
            main.Print()
            main.sel = {1:'Зайти в шатер'}
            main.Refresh()
            main.btn.config(command=Circus12)
        elif main.cfg['circus_check'] == True:
            main.p = 'Мануальный монолог все продолжается. Клоун Чпок не знает устали.'
            main.Phrase()
            main.btn.config(command=Circus12)
            main.sel = {9:'Инвентарь',90:'Уйти'}
            main.Refresh()
            main.btn.config(command=Circus14)
    elif main.cfg['circus_act2_start'] == True and main.cfg['act3'] == False:
        main.p = 'circus_act21.txt'
        main.Print()
        main.sel = {1:'Дождаться начала представления'}
        main.Refresh()
        main.btn.config(command=Circus22)
    elif main.cfg['act3'] == True and main.cfg['circus_end'] == False:
        Circus_el1()
    elif main.cfg['circus_end'] == True:
        Circus31()
    else:
        main.p = 'В шатре пусто, ничего интересного там нет'
        main.Phrase()
        


def Circus12():
    main.p = 'circus_act12.txt'
    main.Print()
    main.sel = {1:'Дождаться начала представления'}
    main.Refresh()
    main.btn.config(command=Circus13)
    
def Circus13():
    main.p = 'circus_act13.txt'
    main.Print()
    main.sel = {9:'Инвентарь',90:'Уйти'}
    main.Refresh()
    main.btn.config(command=Circus14)
def Circus14():
    l = main.choose.get()
    if l == 9:
        main.Inventory()
        main.btn.config(command=Circus15)
    elif l == 90:
        way.West()
def Circus15():
    l = main.choose.get()
    if l == 90:
        main.sel = {9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Circus14)
    elif l == 6:
        main.p = 'circus_end1.txt'
        main.Print()
        del main.inv[6]
        main.cfg['act2'] = True
        way.West()


def Circus22():
    main.p = 'circus_act22.txt'
    main.Print()
    main.sel = {1:'Слушать речь директора'}
    main.Refresh()
    main.btn.config(command=Circus23)
    

def Circus23():
    main.p = 'circus_act23.txt'
    main.Print()
    main.sel = {1:'Ого,слон!'}
    main.Refresh()
    main.btn.config(command=Circus24)
        
def Circus24():
    main.p = 'circus_act24.txt'
    main.Print()
    main.sel = {1:'Воздержаться от апплодисментов'}
    main.Refresh()
    main.btn.config(command=Circus25)
    
def Circus25():
    main.p = 'circus_act25.txt'
    main.Print()
    main.sel = {1:'Выйти из сектора обстрела'}
    main.Refresh()
    main.btn.config(command=Circus26)

def Circus26():
    main.p = 'circus_act26.txt'
    main.Print()
    main.sel = {1:'Нуу... Нуу??? Нуу!!!'}
    main.Refresh()
    main.btn.config(command=Circus27)

def Circus27():
    main.p = 'circus_end21.txt'
    main.Print()
    main.sel = {1:'ВАХ!!!'}
    main.Refresh()
    main.btn.config(command=Circus28)

def Circus28():
    main.p = 'circus_end22.txt'
    main.Print()
    main.sel = {1:"Вперед!"}
    main.Refresh()
    main.cfg['act3'] = True
    main.cfg['pool_check'] = False
    main.cfg['slon_check'] = False
    main.cfg['zver_check'] = False
    way.West()

def Circus_el1():
    
    main.p = "В шатре царит разруха и запустение. Посреди арены все еще лежит труп несчастного Жипки."
    main.Phrase()
    main.sel = {1:'Обследовать труп слона' , 90: 'Уйти'}
    main.Refresh()
    main.btn.config(command=Circus_el2)
    
def Circus_el2():
    l = main.choose.get()
    if l == 1:
        if main.cfg['circus_elef_check'] == False:
            main.p = 'circus_elef.txt'
            main.Print()
            main.cfg['circus_elef_check'] = True
        if main.cfg['stage_end3'] == False and 13 not in main.inv:
            main.inv[13] =  'Глобус Украины'
        main.sel = {9: 'Инвентарь', 90: 'Уйти'}
        main.Refresh()
        main.btn.config(command=Circus_el3)
    elif l == 90:
        way.West()

def Circus_el3():
    l = main.choose.get()
    if l == 9:
        main.Inventory()
        main.btn.config(command=Circus_el4)
    elif l == 90:
        way.West()


def Circus_el4():
    l = main.choose.get()
    if l == 90:
        main.sel = {9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Circus_el3)
    elif l == 16:
        main.p = 'Достав припасенный бочонок, Ян доверху наполнил его слоновьим жиром'
        main.Phrase()
        del main.inv[16]
        main.inv[17] = 'Бочонок слоновьего жира'
        main.sel = {9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Circus_el3)
        
def Circus31():
    main.p = 'circus_act31.txt'
    main.Print()
    main.sel = {1:'Что же нас ждет?'}
    main.Refresh()
    main.btn.config(command=Circus32)
    
def Circus32():
    main.p = 'circus_act32.txt'
    main.Print()
    main.sel = {9:'Инвентарь',90:'Уйти'}
    main.Refresh()
    main.btn.config(command=Circus33)

def Circus33():
    l = main.choose.get()
    if l == 9:
        main.Inventory()
        main.btn.config(command=Circus34)
    elif l == 90:
        main.p = 'Выхода нет!'
        main.Phrase()
        
def Circus34():
    l = main.choose.get()
    if l == 90:
        main.sel = {9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Circus33)
    elif l == 26:
        #del main.inv[26]
        Circus35()
        
def Circus35():
    main.p = 'circus_act33.txt'
    main.Print()
    main.sel = {1:'Наблюдать'}
    main.Refresh()
    main.btn.config(command=Circus36)

def Circus36():
    main.p = 'circus_act34.txt'
    main.Print()
    main.sel = {1:'Это....Великолепно!!!'}
    main.Refresh()
    main.btn.config(command=Circus37)

def Circus36():
    main.p = 'circus_act35.txt'
    main.Print()
    main.sel = {1:'Покинуть шатер'}
    main.Refresh()
    main.btn.config(command=Circus37)

def Circus37():
    main.p = 'circus_burn.txt'
    main.Print()
    main.sel = {1:'НАЧАТЬ'}
    main.Refresh()
    main.btn.config(command=Circus38)

def Circus38():
    if 17 in main.inv and 9 in main.inv and 2 in main.inv:
        main.sel = {9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Burn)
    else:
        main.p = 'circus_fail.txt'
        main.Print()
        main.p = 'Какая жалость. Вы не смогли выполнить миссию и помочь Яну исполнить его Предназначение. Но ничего страшного, всегда можно попробовать еще разок :)'
        main.Phrase()
        main.sel = {1:'Всенепременно! Начну прямо сейчас.' , 2:'NEWERMORE'}
        main.Refresh()
        main.btn.config(command=Restart)

def Restart():
    l = main.choose.get()
    if l == 1:
        main.sel = {1: 'Новая игра' , 2: 'Загрузить игру',  0: 'Выйти'}
        main.Refresh()
        main.btn.config(command=main.Start)
    else:
        main.root.destroy()

def Burn():
    
    l = main.choose.get()
    if l == 9:
        main.Inventory()
        main.btn.config(command=Burn1)
    elif l == 90:
        main.p = 'Выхода нет!'
        main.Phrase()
                    
def Burn1():
    l= main.choose.get()
    if l == 90:
        main.sel = {9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Burn)
    elif l == 17 and main.cfg['circus_bomb'] == 0: 
        del main.inv[17] 
        main.p = 'Ян поставил бочонок со слоновьим жиром у шатра'
        main.Phrase()
        main.cfg['circus_bomb'] = main.cfg['circus_bomb'] +1
        main.sel = {1: 'Поджечь бочонок' , 9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Burn2)
    elif l == 2 and main.cfg['circus_bomb'] == 1:
        main.p = 'Ян добавил в бочонок водки и размешал смесь'
        main.Phrase()
        del main.inv[2]
        main.cfg['circus_bomb'] = main.cfg['circus_bomb'] +1
        main.sel = {1: 'Поджечь бочонок' , 9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Burn2)
    elif l == 9 and main.cfg['circus_bomb'] == 2:
        main.p = 'Ян засунул шашечку динамита в бочонок, оставив фитиль торчать снаружи'
        main.Phrase()
        del main.inv[9]
        main.cfg['circus_bomb'] = main.cfg['circus_bomb'] +1
        main.sel = {1: 'Поджечь бочонок' , 9:'Инвентарь',90:'Уйти'}
        main.Refresh()
        main.btn.config(command=Burn2)
    elif l == 7 and main.cfg['circus_bomb'] == 3:
        main.p = 'circus_win1.txt'
        main.Print()
        main.sel = {1:'гори...Гори!...ГОРИ!!!'}
        main.Refresh()
        main.btn.config(command=Burn3)

def Burn2():
    l= main.choose.get()
    if l == 9:
        main.Inventory()
        main.btn.config(command=Burn1)
    elif l == 90:
        main.p = 'Выхода нет!'
        main.Phrase()
    elif l == 1:
        if main.cfg['circus_bomb'] == 1:
            main.p = 'Жир слишком густой и не загорится'
            main.Phrase()
        elif main.cfg['circus_bomb'] == 2:
            main.p = 'Жир стал горючим, но нужна мощная инициация'
            main.Phrase()
        elif main.cfg['circus_bomb'] == 3:
            main.p = 'circus_win1.txt'
            main.Print()
            main.sel = {1:'гори...Гори!...ГОРИ!!!'}
            main.Refresh()
            main.btn.config(command=Burn3)
            

def Burn3():
    main.p = 'circus_win2.txt'
    main.Print()
    #сделать очистку экрана и мб крупный шрифт
    main.p ='Поздравляю вас! Вы смогли выполнить миссию и исполнить предназначение Яна. Однако, в хорошей игре много разных концовок :) Попробуйте найти остальные.'
    main.Phrase()
    main.sel = {1:'Конечно, попробую!'}
    main.Refresh()
    main.btn.config(command=Burn4)

def Burn4():
    x= main.choose.get()
    if x == 1:
        main.sel = {1: 'Новая игра' , 2: 'Загрузить игру',  0: 'Выйти'}
        main.Refresh()
        main.btn.config(command=main.Start)








