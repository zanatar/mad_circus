import main
import way
toi_d = {1: 'Осмотреться',0: 'Уйти'}

toi_base = {1: 'Ян зашел в кабинку с табличкой «МЭ». Запершись, спустив штаны и кое-как пристроившись на очке, он попытался облегчиться. Но процесс все никак не начинался, а жуткая вонь отбивала желание продолжать попытки, Так что Ян спешно покинул заведение.' ,
            2: 'Ян зашел в кабинку с табличкой «ЖО». Запершись, спустив штаны и кое-как пристроившись на очке, он попытался облегчиться. Но процесс все никак не начинался, а жуткая вонь отбивала желание продолжать попытки, Так что Ян спешно покинул заведение.'
            }
def Toi_way():
    main.sel = toi_d
    main.Refresh()
    main.btn.config(command=Toi)

def Toi():
    x = main.choose.get()
    if x == 1:
        main.p = 'toi_start.txt'
        main.Print()
        toi_d[2] = 'Зайти в кабинку с табличкой "МЭ"'
        toi_d[3] = 'Зайти в кабинку с табличкой "ЖО"'
        if main.cfg['drunk_fail'] == True:
            if main.cfg['toi_tab'] == False:
                main.p ='Ян осмотрел туалет еще раз. Внезапно в его голове зародилась годная идея.'
                main.Phrase()
                toi_d[4] = 'Поменять местами таблички "МЭ" и "ЖО"'
                main.Refresh()
                main.cfg['drunk_fail'] = False
        main.Refresh()
    elif x == 2:
        if main.cfg['toi_tab'] == False and main.cfg['drunk_event'] == False:
            main.p = toi_base[1]
            main.Phrase()
        elif main.cfg['toi_tab'] == False and main.cfg['drunk_event'] == True:
            main.p = 'toi_fail.txt'
            main.Print()
            main.cfg['drunk_fail'] = True
            main.cfg['zak_drunk'] = True
            main.cfg['drunk_event'] = False
        elif main.cfg['toi_tab'] == True and main.cfg['toi_brake'] == False:
            main.p = 'toi_fem1.txt'
            main.Print()
        elif main.cfg['toi_tab'] == True and main.cfg['toi_brake'] == True:
            main.p = 'Туалет с табличкой "МЭ" сильно поврежден. Воспользоваться им по назначению не выйдет'
            main.Phrase()
    elif x == 3:
        if main.cfg['toi_tab'] == False:
            main.p = 'toi_fem.txt'
            main.Print()
        elif main.cfg['toi_tab'] == True and main.cfg['drunk_event'] == True:
            main.p = 'toi_win.txt'
            main.Print()
            toi_base[1] = 'Туалет с табличкой "МЭ" сильно поврежден. Воспользоваться им по назначению не выйдет'
            main.inv[14] = 'Отрезанный член'
            main.inv[15] = 'Стальное яйцо'
            main.cfg['drunk_event'] = False
            main.cfg['toi_brake'] = True
        elif main.cfg['toi_tab'] == True and main.cfg['drunk_event'] == False:
            main.p = toi_base[2]
            main.Phrase()
    elif x == 4:
        main.p = 'Ян ловко поменял местами таблички "МЭ" и "ЖО"'
        del toi_d[4]
        main.cfg['toi_tab'] = True
        main.Refresh()
    elif x == 0:
        way.West()
            

                
