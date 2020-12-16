import way
import main
from pygame import mixer

stage_d = {1: 'Осмотреться', 0: 'Уйти'}
string1 = {1: 'Эээ, песня про зайцев!' , 2: 'Маэстро, урежте марш!' ,
           3: 'Non più compagni: andate' , 4: 'Спой, светик, не стыдись!' ,
           5: 'Я требую продолжения банкета!'}
           
string2 = {1: 'Хоп хоп, мусорок, не шей мне срок!' , 2: 'Розовые розы Светке Соколовой' ,
           3: 'Das ist der Pariser Tango Monsieur' , 4: 'Solo restar desio, meco non bramo' ,
           5: 'Союз нерушимый республик свободных'}
string3 = {1: 'Потерял я Эвридику' , 2:  'Che il mio dolor crudel: mi dà conforto' , 
           3: 'Из за острова на стрежень' , 4: 'Куда, куда, куда вы удалились?' ,
           5: 'Der Hölle Rache kocht in meinem Herzen'}
string4 = {1: 'Solo il barbaro affanno:' , 2: 'Casta diva' , 3: ' Être ou ne pas être' ,
           4: 'vive la Résistance' , 5: 'Aut Caesar, aut nihil.' }
string5 = {1: 'Lascia ch`io pianga' , 2: 'Ogni altro oggetto a me divien tiranno' ,
           3: 'Ridi, Pagliaccio, sul tuo amore infranto!' , 4: 'Dove andrò senza il mio ben?' ,
           5: 'La donna è mobile'}
romeo_d = {1: 'Перестать слушать музыку' }

def Stage_way():
    main.sel = stage_d
    main.Refresh()
    main.btn.config(command=Stage)

def Stage():
    x = main.choose.get()
    if x == 1:
        if main.cfg['act3'] == False and  main.cfg['stage_end1'] == False:
            main.p = 'stage_act1.txt'
            main.Print() 
            stage_d[9] = 'Инвентарь'
            main.Refresh()
        elif main.cfg['act3'] == False and  main.cfg['stage_end1'] == True:
            main.p = 'Музыкальная сцена опустела и лишь ветер гоняет по ней пыль и обрывки бумаги. Делать там пока определенно нечего.'
            main.Phrase()
        elif main.cfg['act3'] == True and  main.cfg['stage_end3'] == True:
            main.p = 'На сцене пусто и уныло. Только шарманщик, ссутулился в углу и, время от времени, скучающе покручивал ручку шарманки, извлекая из нее то Баха, то Rammstein, то песни группы «Руки вверх».'
            main.Phrase()
        elif main.cfg['act3'] == True and  main.cfg['stage_end3'] == False:
            main.p = 'stage_act3.txt'
            main.Print()
            stage_d[2] = 'Послушать выступление'
            main.Refresh()
        elif main.cfg['stage_listen'] == True:
            stage_d[3] = 'Привлечь внимание артиста'
            stage_d[9] = 'Инвентарь'
            main.Refresh()
            
    elif x == 2 and main.cfg['act3'] == True and  main.cfg['stage_end3'] == False:
        Euridica()
    elif x == 3 and  main.cfg['stage_end3'] == False:
        if  main.cfg['stage_request'] == False:
            Request()
        elif main.cfg['stage_request'] == True:
            main.p ='Ян привлек внимание пьяницы и попросил исполнить арию Цингарелли на бис. Тот с радостью согласился.'
            main.Phrase()
            main.sel = {1: 'Наслаждаться музыкой '}
            main.Refresh()
            main.btn.config(command=Romeo)
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Stage1)
    elif x == 0:
        way.South()
        
            
def Stage1():
    i = main.choose.get()
    if i == 3 and main.cfg['stage_end1'] == False:
        main.p = 'Выждав, пока музыкант, утомившись дуть в рог, взял паузу и отложил рог в сторону, Ян незаметно засунул в нее морковку.'
        main.Phrase()
        main.sel = {1: 'Подождем и поглядим, что произойдет'}
        main.Refresh()
        main.btn.config(command=Stage2)
    elif i == 2 and main.cfg['stage_end1'] == True and main.cfg['stage_end3'] == False and  main.cfg['stage_listen'] == True:
        main.p ='Ян подошел к сцене и протянул пьянице бутылку водки. Тот принял ее, внимательно осмотрел, открыл, понюхал содержимое. Затем, брезгливым движением, он вылил ее содержимое на землю, замотал головой, словно отрицая свое алкогольное прошлое, и вернул обескураженному Яну пустую бутылку.'
        main.Phrase()
        del  main.inv[2]
        main.inv[8] = 'Пустая бутылка'
        main.Inventory()
    elif i == 10 and main.cfg['stage_end1'] == True and main.cfg['stage_end3'] == False and  main.cfg['stage_listen'] == True:
        main.p = 'Ян подошел к сцене и протянул пьянице бутылку с пургеном. Тот принял ее, внимательно осмотрел, открыл, понюхал содержимое. Затем, брезгливым движением, он вылил ее содержимое на землю, замотал головой, словно отрицая свое алкогольное прошлое, и вернул обескураженному Яну пустую бутылку.'
        main.Phrase()
        del  main.inv[10]
        main.inv[8] = 'Пустая бутылка'
        main.Inventory()
    elif i == 90:
        Stage_way()




def Stage2():
    x = main.choose.get()
    if x == 1:
        main.p = 'stage_end1.txt'
        main.Print()
        del  main.inv[3]
        main.inv[6] = 'Сломаный альпийский рог'
        del stage_d[9]
        main.cfg['stage_end1'] = True
        Stage_way()
    
def Euridica():
    main.p = 'stage_eu_start.txt'
    main.Print()
    main.sel = {1: 'Наслаждаться музыкой '}
    main.Refresh()
    main.btn.config(command=Euridica1)

def Euridica1():
    x = main.choose.get()
    if x == 1:
        main.p = 'stage_euredica.txt'
        main.Print()
        mixer.init()
        mixer.music.load('e.ogg')
        mixer.music.play()
        main.sel = {1: 'Перестать слушать музыку '}
        main.Refresh()
        main.btn.config(command=Euridica2)

def Euridica2():
    x = main.choose.get()
    if x == 1:
        mixer.music.stop()
        main.cfg['stage_listen'] = True
        stage_d[3] = 'Привлечь внимание артиста'
        stage_d[9] = 'Инвентарь'
        Stage_way()


def Request():
    main.p = 'Пьяница с интересом взглянул на Яна, ожидая, видимо, заказа песни. Ян обратил мысленный взор внутрь себя, ожидая инструкций, но в ответ на него вылился поток  непонятных, не связанных меж собою фраз…'
    main.Phrase()
    main.sel = string1
    main.Refresh()
    main.btn.config(command=Request1)
    
def Request1():
    x = main.choose.get()
    if x == 3:
        main.p ='Пьяница оживился, услышав что-то отдаленно знакомое. Нужно продолжать'
        main.Phrase()
        main.sel = string2
        main.Refresh()
        main.btn.config(command=Request2)
    else:
        main.p =  'Пьяница разочарованно поморщился, не сумев уловить знакомые слова'
        main.Phrase()
        Stage_way()


def Request2():
    x = main.choose.get()
    if x == 4:
        main.p ='Интерес усилился. Нужно продолжать'
        main.Phrase()
        main.sel = string3
        main.Refresh()
        main.btn.config(command=Request3)
    else:
        main.p =  'Пьяница разочарованно поморщился, не сумев уловить знакомые слова'
        main.Phrase()
        Stage_way()

def Request3():
    x = main.choose.get()
    if x == 2:
        main.p ='Да, эта вещь определенно ему знакома. Но нужна конкретика.'
        main.Phrase()
        main.sel = string4
        main.Refresh()
        main.btn.config(command=Request4)
    else:
        main.p =  'Пьяница разочарованно поморщился, не сумев уловить знакомые слова'
        main.Phrase()
        Stage_way()

def Request4():
    x = main.choose.get()
    if x == 1:
        main.p ='Пьяница почти уловил мелодию и буквально умоляет взором о последней строке'
        main.Phrase()
        main.sel = string5
        main.Refresh()
        main.btn.config(command=Request5)
    else:
        main.p =  'Пьяница разочарованно поморщился, не сумев уловить знакомые слова'
        main.Phrase()
        Stage_way()

def Request5():
    x = main.choose.get()
    if x == 2:
        main.p ='stage_rom_start.txt'
        main.Print()
        main.cfg['stage_request'] = True
        main.sel = {1: 'Наслаждаться музыкой '}
        main.Refresh()
        main.btn.config(command=Romeo)
    else:
        main.p =  'Пьяница разочарованно поморщился, не сумев уловить знакомые слова'
        main.Phrase()
        Stage_way()


def Romeo():
    x = main.choose.get()
    if x == 1:
        mixer.init()
        mixer.music.load('r.mp3')
        mixer.music.play()
        main.p ='stage_romeo.txt'
        main.Print()
        if main.cfg['stage_rom_new'] == False:
            main.p ='stage_rom_new.txt'
            main.Print()
            main.cfg['stage_rom_new'] = True
        romeo_d[9] = 'Инвентарь'
        main.sel = romeo_d
        main.Refresh()
        main.btn.config(command=Romeo1)

def Romeo1():
    x = main.choose.get()
    if x == 1:
        mixer.music.stop()
        Stage_way()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Romeo2)

def Romeo2():
    i = main.choose.get()
    if i == 90:
        mixer.music.stop()
        Stage_way()
    elif i == 2:
        main.p ='stage_rom_vodka.txt'
        main.Print()
        del main.inv[2]
        main.cfg['stage_rom_vodka'] = True
        mixer.music.stop()
        Stage_way()
    elif i == 10 and main.cfg['stage_rom_vodka'] == True:
        main.p ='stage_rom_purg.txt'
        main.Print()
        del main.inv[10]
        del stage_d[2]
        del stage_d[3]
        del stage_d[9]
        main.inv[22] = 'Крючок'
        main.cfg['stage_end3'] = True
        mixer.music.stop()
        Stage_way()
    










