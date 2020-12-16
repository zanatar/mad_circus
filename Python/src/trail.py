import way
import main

trailer_d = {1: 'Осмотреться', 0: 'Уйти'}
trailer_doc = {1: 'Подать ценный совет' , 9: 'Инвентарь' , 0: 'Уйти'}
trailer_advice = {1: 'Конем, ходи, конем - век воли не видать!' ,
                 2: 'Цапу надо крутить' , 3: 'Семь раз отмерь, один раз отрежь.' ,
                 4: 'Кантуй по малу' , 5: 'Господа, позвольте я пробью с ноги!',
                  0: 'Прекратить подавать ценные советы' }

trailer_react = {1: 'Доктор всем своим видом дал понять, куда бы он ввел ферзя любителю шахмат' ,
                 2: 'Доктор с раздражением взглянул на поцака без цака' , 
                 3: 'Доктор с энтузиазмом воспринял данное предложение. Жаль, скальпель для данной операции не подойдет' ,
                 4: 'Доктор не проявил интереса к потенциальному грузчику' ,
                 5: 'Господа, возможно, позволили бы. Но доктор верен клятве Гиппократа!'}


def Trailer_way():
    main.sel = trailer_d
    main.Refresh()
    main.btn.config(command=Trailer)

def Trailer():
    x = main.choose.get()
    if x == 1:
        main.p = 'trailer_start.txt'
        main.Print()
        if main.cfg['jong_end1'] == False and 18 not in main.inv:
            main.p = 'Дверь фургона, покрашенного в красный цвет, была непредусмотрительно открыта.'
            main.Phrase()
            trailer_d[2] = 'Подойти к красному фургону'
        if main.cfg['jong_end1'] == True and main.cfg['trailer_amput'] == False:
            main.p = 'Около фургона, покрашенного в красный цвет, собралась толпа народу. Люди с интересом заглядывали внутрь через окна и двери.'
            main.Phrase()
            trailer_d[2] = 'Подойти к красному фургону'
        if main.cfg['stage_end1'] == True and main.cfg['act2'] == True and main.cfg['trailer_kill'] == False:
            main.p = 'Из фургона, покрашенного в голубой цвет, доносились шум и ругань.'
            main.Phrase()
            trailer_d[3] = 'Подойти к голубому фургону'
        main.Refresh()
    elif x == 2:
        if main.cfg['jong_end1'] == False and 18 not in main.inv:
            main.p = 'trailer_iron.txt'
            main.Print()
            main.inv[18] = 'Гиря'
            del trailer_d[2]
            main.Refresh()
        elif main.cfg['jong_end1'] == True and main.cfg['trailer_amput'] == False:
            main.p = 'trailer_doctor.txt'
            main.Print()
            Doc()
    elif x == 3 and main.cfg['stage_end1'] == True and main.cfg['trailer_kill'] == False:
        Ukr()
    elif x == 0:
        way.South()


def Ukr():   
    main.p = 'trailer_ukr1.txt'
    main.Print()
    main.sel = {1: 'Слушать диалог'}
    main.Refresh()
    main.btn.config(command=Ukr1)

def Ukr1():   
    main.p = 'trailer_ukr2.txt'
    main.Print()
    main.sel = {1: 'Что же будет дальше?'}
    main.Refresh()
    main.btn.config(command=Ukr2)

def Ukr2():   
    main.p = 'trailer_ukr3.txt'
    main.Print()
    main.sel = {1: 'Вот это поворот!'}
    main.Refresh()
    main.btn.config(command=Ukr3)

def Ukr3():
     main.p = 'Поняв, что больше тут ничего интересного не будет, а оказываться рядом с местом преступления не стоит, Ян ретировался, прихватив с собой глобус Украины на память.'
     main.Phrase()
     main.inv[13] = 'Глобус Украины'
     del trailer_d[3]
     main.cfg['trailer_kill'] = True
     Trailer_way()
     

    
        

            
    
def Doc():
    main.sel = trailer_doc
    main.Refresh()
    main.btn.config(command=Doc1)


def Doc1():
    x = main.choose.get()
    if x == 1:
        main.sel = trailer_advice
        main.Refresh()
        main.btn.config(command=Advice)
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Doc2)
    elif x == 0:
        Trailer_way()
        
        
    
def Doc2():
    i = main.choose.get()
    if i == 5:
        main.p = 'trailer_amput.txt'
        main.Print()
        del main.inv[5]
        main.sel = {1: 'Отойти подальше'}
        main.Refresh()
        main.btn.config(command=Doc3)
    elif i == 90:
        Doc()


def Doc3():
    x = main.choose.get()
    if x == 1:
        main.p = 'Отойдя подальше, Ян осмотрел свою находку. Ей оказался шприц с длинной иглой и надписью «Адреналин» на приклеенной бирке. Штука определенно полезная.'
        main.Phrase()
        main.inv[11] = 'Шприц с адреналином'
        main.cfg['trailer_amput'] = True
        del trailer_d[2]
        Trailer_way()

        
        


def Advice():
    x = main.choose.get()
    if x == 0:
        Doc()
    else:
        main.p = trailer_react[x]
        main.Phrase()
        
        
        
    
            

            
