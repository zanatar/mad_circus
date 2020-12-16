import main
import way

zak_d = {1: 'Осмотреться', 0: 'Уйти'}
drunk_d = {1: 'Осмотреться', 2: 'Поговорить с пьяницей', 9: 'Инвентарь' , 0:'Уйти'}  
mouse = {1:'Ян подошел к прилавку и покопался в судках, мисках и тарелках, расставленных на нем. Единственное, что его заинтересовало, было, увы, дохлой мышью, которую он и прихватил с собой с неясными целями.' , 
         2:'Ян подошел к прилавку. При более тщательном осмотре его содержимое не стало для него ни привлекательнее, ни интереснее.'
         }
desk_d = {1: 'Осмотреться' , 0: 'Уйти'}


zak_crate = { 1: 'Ян подошел к ящику с водкой. Дождавшись, пока фокус зрения продавщицы сместится от него в противоположную сторону, он попытался украдкой стащить бутылку. Взгляд продавщицы моментально сфокусировался на Яне.  «Руки убрал», взрыкнула продавщица, выхватив  откуда-то из глубин драной юбки грязный половник и выразительно стукнула им по прилавку так, что зазвенела посуда. Ян решил не рисковать.' ,
              2: 'Ян подошел к ящику с водкой. Теперь между ним и алкоголем не было никаких препятствий и он ловко выхватил бутылку из ящика. Однако внимательное изучение ее содержимого подтвердила его худшие опасения – самому пить такое было категорически невозможно. Возможно водке все-же найдется применение.',
              3: 'Бесплатная водка - это конечно здорово, но, полагаю, одной бутылки пока достаточно'}
def Zak_way():
    if main.cfg['zak_drunk'] == True and main.cfg['zak_check'] == True:
        zak_d[4] = 'Подойти к пьянице'
    main.sel = zak_d
    main.Refresh()
    main.btn.config(command=Zak)

def Zak():
    x = main.choose.get()
    if x == 1:
        main.p = 'zak_start.txt'
        main.Print()
        if main.cfg['zak_prod'] == True:           
            main.p = 'За прилавком находится продавщица'
            main.Phrase()
        if main.cfg['zak_drunk'] == True:
            main.p = 'За одним из столиков сидит пьяница'
            zak_d[4] = 'Подойти к пьянице'
            main.Phrase()
        zak_d[2] = 'Подойти к прилавку'
        zak_d[3] = 'Подойти к ящику с водкой'
        main.cfg['zak_check'] = True
        main.sel = zak_d
        main.Refresh()
    elif x == 2 and main.cfg['zak_prod'] == False and main.cfg['zak_mouse'] == False :
        main.p = mouse[1]
        main.Phrase()
        main.inv[4] = 'Дохлая мышь'
        main.cfg['zak_mouse'] = True
    elif x == 2 and main.cfg['zak_mouse'] == True:
        main.p = mouse[2]
        main.Phrase()
    elif x == 2 and main.cfg['zak_prod'] == True:
        Desk()
    elif x == 3:
        if main.cfg['zak_prod'] == True:
            main.p = zak_crate[1]
            main.Phrase()
        elif main.cfg['zak_prod'] == False and 2 not in main.inv:
            main.p = zak_crate[2]
            main.Phrase()
            main.inv[2] = 'Бутылка водки'
        elif main.cfg['zak_prod'] == False and 2 in main.inv:
            main.p = zak_crate[3]
            main.Phrase()
    elif x == 4 and main.cfg['zak_drunk'] == True:
        Drunk()
    elif x == 0:
        way.West()
def Desk():
    main.sel = desk_d
    main.Refresh()
    main.btn.config(command=Desk1)
def Desk1():
    x = main.choose.get()
    if x == 1:
        main.p = 'desk_start.txt'
        main.Print()
        desk_d[9] = 'Инвентарь'
        desk_d[2] = 'Поговорить с продавщицей'
        main.sel = desk_d
        main.Refresh()
    elif x == 2:
        main.p = 'Продавщица скосила на Яна глаза, моментально оценила платежеспособность клиента, недовольно хмыкнула и продолжила пялиться в пустоту.'
        main.Phrase()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Desk2)
    elif x ==0:
        Zak_way()

def Desk2():
    i = main.choose.get()
    if i == 90:
        main.sel = desk_d
        main.Refresh()
        main.btn.config(command=Desk1)
    elif i == 1:
        main.p = 'desk_prod.txt'
        main.Print()
        main.cfg['zak_prod'] = False
        del main.inv[1]
        main.inv[5] = 'Ржавая ножовка'
        Zak_way()

def Drunk():
    main.sel = drunk_d
    main.Refresh()
    main.btn.config(command=Drunk1)

def Drunk1():
    x = main.choose.get()
    if x == 2:
        main.p = 'Повернувшись к вам, пьяница попытался выдавить из себя что-нибудь членораздельное, но не смог'
        main.Phrase()
    elif x == 0:
        Zak_way()
    elif x == 1:
        main.p = 'drunk_start.txt'
        main.Print()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Drunk2)

def Drunk2():
    i = main.choose.get()
    if i == 90:
        main.sel = drunk_d
        main.Refresh()
        main.btn.config(command=Drunk)
    elif i == 2:
        main.p = 'drunk_vodka.txt'
        main.Print()
        del main.inv[2]
        Drunk()
    elif i == 10:
        main.p = 'drunk_purgen.txt'
        main.Print()
        del main.inv[10]
        del zak_d[4]
        main.cfg['zak_drunk'] = False
        main.cfg['drunk_event'] = True
        Zak_way()
        
        
    
        

    







   
