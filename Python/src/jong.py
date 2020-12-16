jong_d = {1: 'Осмотреться', 0: 'Уйти'}
lynch_d = {1: 'Выкрикнуть реплику' , 9: 'Инвентарь' , 0: 'Уйти'}
lynch_rep1 = {1: '«-У музыканта был мотив»' , 2: '«- Слава Украине»' ,
              3: 'Сторона обвинения запрашивает проведения дополнительный следственных действий в тч глубинного ректального обыска обвиняемого', 0: 'Уйти' }
lynch_rep2 = {1: 'Сторона обвинения настаивает на привлечении неустановленных лиц к солидарной отвественности' , 2: 'Кровь на руках' , 3:'Кто не скачет – тот москаль', 0: 'Уйти'}
lynch_rep3 = {1: 'Виновен он, виновен, я точно знаю!' , 2: 'Ща не вмерла украина' , 3: 'Прошу признать обвиняемого виновным на основании неприменения им ст. 51 конституции', 0: 'Уйти' }


import way
import main

def Jong_way():
    main.sel = jong_d
    main.Refresh()
    main.btn.config(command=Jong)

def Jong():
    x = main.choose.get()
    if x == 1:
        if main.cfg['jong_end1'] == False and main.cfg['act3'] == False:
            main.p = 'jong_start.txt'
            main.Print()
            jong_d[9] = 'Инвентарь'
            main.Refresh()
        elif main.cfg['act3'] == True and main.cfg['jong_end3'] == False:
            main.p = 'jong_lynch.txt'
            main.Print()
            jong_d[2] = 'Проследовать на заседание'
            main.Refresh()
        else:
            main.p ='Площадка пуста, никого нет, ничего не происходит'
            main.Phrase()
    elif x == 2 and main.cfg['act3'] == True and main.cfg['jong_end3'] == False:
        main.p = 'jong_lynch1.txt'
        main.Print()
        Lynch()
    elif x == 9 and main.cfg['jong_end1'] == False and main.cfg['act3'] == False:
        main.Inventory()
        main.btn.config(command=Jong1)
    elif x == 0:
        way.North()


def Jong1():
    i = main.choose.get()
    if i == 90:
        Jong_way()
    elif i == 18:
        main.p = 'jong_end1.txt'
        main.Print()
        del main.inv[18]
        main.cfg['jong_end1'] = True
        del jong_d[9]
        Jong_way()
        
def Lynch():
    main.sel = lynch_d
    main.Refresh()
    main.btn.config(command=Lynch1)

def Lynch1():
    x = main.choose.get()
    if x == 1:
        if main.cfg['jong_rep'] == 2 :
            main.p = 'Ян прислушался к голосу в своей голове. Из потока сумбура ему удалось вычленить отдельные осмысленные фразы.'
            main.Phrase()
            main.sel = lynch_rep2
            main.Refresh()
            main.btn.config(command=Rep2)
        elif main.cfg['jong_rep'] == 3 :
            main.p = 'Ян прислушался к голосу в своей голове. Из потока сумбура ему удалось вычленить отдельные осмысленные фразы.'
            main.Phrase()
            main.sel = lynch_rep3
            main.Refresh()
            main.btn.config(command=Rep3)
        else:
            main.p = 'Ян прислушался к голосу в своей голове. Из потока сумбура ему удалось вычленить отдельные осмысленные фразы.'
            main.Phrase()
            main.sel = lynch_rep1
            main.Refresh()
            main.btn.config(command=Rep1)
    elif x == 0:
        Jong_way()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Lynch2)

def Lynch2():
    i = main.choose.get()
    if i == 90:
        Lynch()
    elif i == 13 and main.cfg['jong_lynch'] == 2:
        main.p = 'jong_end31.txt'
        main.Print()
        main.cfg['jong_lynch'] = 3
        Verd()
        

def Rep1():
    x = main.choose.get()
    if x == 1:
        main.p = 'jong_rep11.txt'
        main.Print()
        main.cfg['jong_lynch'] = main.cfg['jong_lynch'] + 1
        main.cfg['jong_rep'] = main.cfg['jong_rep'] + 1
        Lynch()
    elif x == 2:
        main.p = 'jong_rep12.txt'
        main.Print()
        main.cfg['jong_lynch'] = main.cfg['jong_lynch'] - 1
        main.cfg['jong_rep'] = main.cfg['jong_rep'] + 1
        Lynch()
    elif x == 3:
        main.p ='Судья и прокурор посмотрели на Яна мутными глазами, не в силах понять произнесенное.'
        main.Phrase()
    elif x == 0:
        Lynch()

def Rep2():
    x = main.choose.get()
    if x == 2:
        main.p = 'jong_rep21.txt'
        main.Print()
        main.cfg['jong_lynch'] = main.cfg['jong_lynch'] + 1
        main.cfg['jong_rep'] = main.cfg['jong_rep'] + 1
        Lynch()
    elif x == 3:
        main.p = 'jong_rep22.txt'
        main.Print()
        main.cfg['jong_lynch'] = main.cfg['jong_lynch'] - 1
        main.cfg['jong_rep'] = main.cfg['jong_rep'] + 1
        Lynch()
    elif x == 1:
        main.p ='Судья и прокурор посмотрели на Яна мутными глазами, не в силах понять произнесенное.'
        main.Phrase()
    elif x == 0:
        Lynch()

def Rep3():
    x = main.choose.get()
    if x == 1:
        main.p = 'Свидетельство Яна не было учтено, ввиду бездоказательности и того, что личность Яна не вызывала доверия'
        main.Phrase()
        Verd()
    elif x == 2:
        main.p = 'jong_fail1.txt'
        main.cfg['jong_lynch'] = main.cfg['jong_lynch'] - 1
        main.Print()
        Verd()
    elif x == 3:
        main.p ='Судья и прокурор посмотрели на Яна мутными глазами, не в силах понять произнесенное.'
        main.Phrase()
    elif x == 0:
        Lynch()
        

def Verd():
    main.sel = {1: 'Каков же будет вердикт?'}
    main.Refresh()
    main.btn.config(command=Verd1)

def Verd1():
    x = main.choose.get()
    if x == 1:
        if main.cfg['jong_lynch'] == 3:
            main.p = 'jong_end32.txt'
            main.Print()
            main.sel = {1: 'Правосудие восторжествовало!'}
            main.Refresh()
            main.btn.config(command=Verd2)
        elif main.cfg['jong_lynch'] == -3 :
            main.p = 'jong_fail2.txt'
            main.Print()
            main.sel = {1: 'Что-то пошло не так...'}
            main.Refresh()
            main.btn.config(command=Fail)
        else:
            main.p = 'Судья не смог определиться с приговором и отправил дело на пересмотр'
            main.Phrase()
            main.cfg['jong_rep'] = main.cfg['jong_rep'] - 2
            main.cfg['jong_lynch'] = 0
            Jong_way()

def Verd2():
    x = main.choose.get()
    if x == 1:
        main.p = 'Удовлетворенная толпа стала расходится, служители вынули тело из петли и споро потащили в сторону зверинца и лишь довольный исходом Ян остался до самого конца, когда сцена опустела и он смог спокойно отвязать и забрать себе длинную веревку. «-Веревка повешенного – на удачу», довольно размышлял Ян.'
        main.Phrase()
        del main.inv[13]
        main.inv[23] ='Веревка'
        main.cfg['jong_end3'] = True
        del jong_d[2]
        Jong_way()


def Fail():
    x = main.choose.get()
    if x == 1:
        main.p = 'jong_endgame.txt'
        main.Print()
        main.sel = {1: 'Новая игра' , 2: 'Загрузить игру',  0: 'Выйти'}
        main.Refresh()
        main.btn.config(command=main.Start)
       







        
