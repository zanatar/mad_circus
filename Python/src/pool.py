pool_d = {1: 'Осмотреться', 0: 'Уйти'}
border_d = {1: 'Искупаться' , 0: 'Уйти'}
fishing_d = {1: 'Рыбачить' , 9: 'Инвентарь' , 0: 'Уйти'}
import way
import main


def Pool_way():
    main.sel = pool_d
    main.Refresh()
    main.btn.config(command=Pool)

def Pool():
    if main.cfg['pool_check'] == False and 2 in pool_d:
        del pool_d[2]
        main.Refresh()
    x = main.choose.get()
    if x == 1:
        main.p = 'Бассейн представлял собой приличный размеров яму, вырытую в земле и заполненную мутноватой водой. '
        main.Phrase()
        if main.cfg['act3'] == False:
            main.p = 'Внутри и около него никого не было, не считая охранника, сонно опершегося на ограждение.'
            main.Phrase()
        elif main.cfg['act3'] == True and main.cfg['pool_clean'] == False:
            main.p = 'Похоже, там началось представление. В воде находились несколько девочек, затянутых в зеленоватые трико с пришитыми плавниками – не слишком удачная попытка изобразить русалок. Они бултыхались по периметру бассейна, пытаясь изобразить некий танец или ритуал. Выглядело все это довольно убого.'
            main.Phrase()
            if main.cfg['ride_end3'] == True:
                main.p = 'Неподалеку от бассейна, застряв в ограде цирка, торчали праздничные сани. Пара служителей и охранник бассейна пытались что-то с ними сделать.'
                main.Phrase()
            else:
                main.p = 'Впрочем, оживившийся охранник смотрел на это мельтешение с большим удовольствием. Его правая рука находилась глубоко в кармане брюк, и шевелилась, словно он там потерял что-то весьма важное и никак не может найти.'
                main.Phrase()
        else:
            main.p = 'После устроенной Яном диверсии бассейн опустел и зрители разошлись.'
            main.Phrase()
            main.p = 'Неподалеку от бассейна, застряв в ограде цирка, торчали праздничные сани. Пара служителей и охранник бассейна пытались что-то с ними сделать.'
            main.Phrase()
        pool_d[2] = 'Подойти к краю бассейна'
        main.cfg['pool_check'] = True
        main.Refresh()
    elif x == 2 and main.cfg['pool_check'] == True:
        Move()
    elif x == 0:
        way.East()

def Move():
    if main.cfg['act3'] == False:
        main.p = 'День был жаркий и Яну захотелось искупаться. Он попытался подойти к бассейну с целью заняться водными процедурами, но охранник, лениво повернувшись к нему, промолвил «-выступлений пока нет, покиньте площадку», отбив у Яна желание продолжать попытки. Больше, пока, тут делать нечего.'
        main.Phrase()
        Pool_way()
    elif main.cfg['act3'] == True and main.cfg['ride_end3'] == False:
        main.p =  'Ян попытался подойти к бассейну поближе, но охранник, заметив движение, резко повернулся к нему и, не вынимая руки из кармана, рявкнул «-не подходить к выступающим!», после чего вернулся к просмотру. Больше, пока, тут делать нечего.'
        main.Phrase()
        Pool_way()
    elif main.cfg['act3'] == True and main.cfg['ride_end3'] == True and main.cfg['pool_fishing'] == False:
        main.p =  'Ян подошел к бассейну. Охранник был так занят работой с санями, что не обратил на это внимание.'
        main.Phrase()
        if main.cfg['pool_swim'] == False:
            main.p = 'Денек был жарким и Яна потянуло искупнуться.'
            main.Phrase()
        Border()
    elif main.cfg['pool_fishing'] == True:
        main.p = 'Охранник наверняка запомнил нарушителя. Думаю, не стоит искушать судьбу.'
        main.Phrase()
        Pool_way()

def Border():
    if main.cfg['pool_swim'] == True and 1 in border_d:
        del border_d[1]
        border_d[2] = 'Порыбачить'
    if main.cfg['pool_swim'] == False:
        border_d[9] = 'Инвентарь'
    main.sel = border_d
    main.Refresh()
    main.btn.config(command=Border1)


def Border1():
    x = main.choose.get()
    if x == 1 and main.cfg['pool_swim'] == False:
        if main.cfg['pool_clean'] == False:
            main.p = 'Яну все еще хотелось искупаться, но «русалки» занимали в бассейне много места и своими перемещениями создавали волнение, что, учитывая весьма слабый навык плавания, отбивало все желание. Нужно бы очистить бассейн.'
            main.Phrase()
            border_d[9] = 'Инвентарь'
            main.cfg['pool_inv'] = True
            main.Refresh()
        elif main.cfg['pool_clean'] == True and main.cfg['pool_calm'] == False:
            main.p = 'По странному капризу стихии, физики отражения и предвзятости судьбы, волны, поднятые «русалками» все не затихали и не затихали.'
            main.Phrase()
        elif main.cfg['pool_calm'] == True:
            main.p = 'pool_swim.txt'
            main.Print()
            main.cfg['pool_swim'] = True
            del border_d[1]
            del border_d[9]
            border_d[2] = 'Порыбачить'
            Border()
    elif x == 2 and main.cfg['pool_swim'] == True:
        main.p = 'Ян решил приступить к рыбалке, используя подручные средства'
        main.Phrase()
        Fishing()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Border2)
    elif x == 0:
        Pool_way()


def Border2():
    i = main.choose.get()
    if i == 90:
        Border()
    elif i == 4:
        main.p = 'pool_clean.txt'
        main.Print()
        main.cfg['pool_clean'] = True
        del main.inv[4]
        Border()
    elif i == 17 and main.cfg['pool_clean'] == True:
        main.p = 'pool_calm.txt'
        main.Print()
        main.cfg['pool_calm'] = True
        del main.inv[17]
        main.inv[16] = 'Пустой бочонок'
        Border()

def Fishing():
    main.sel = fishing_d
    main.Refresh()
    main.btn.config(command=Fishing1)

def Fishing1():
    x = main.choose.get()
    if x == 1:
        if main.cfg['pool_rod'] == 0:
            main.p = 'На что ловить то будем? Руками не вариант'
            main.Phrase()
        elif main.cfg['pool_rod'] == 1:
            main.p = 'Оглушить рыбу палкой не получиться - вода слишком мутная.'
            main.Phrase()
        elif main.cfg['pool_rod'] == 2:
            main.p = 'Такой удочкой можно поймать рыбу, только если долго читать ей произведения Эдгара По. Возможно тогда она захочет свить из веревки петлю и повеситься. Ах, да, у рыб нет гортани.'
            main.Phrase()
        elif main.cfg['pool_rod']== 3:
            main.p = ' Ян закинул удочку в воду и долго сидел у берега выжидая. Но рыба так и не клюнула. Может быть требуется что-то еще?'
            main.Phrase()
        elif main.cfg['pool_rod'] == 4:
            main.p = 'Ян закинул импровизированную удочку в мутные воды и принялся ждать.'
            main.Phrase()
            main.sel = {1: 'Ловить рыбка большая и очень большая!'}
            main.Refresh()
            main.btn.config(command=Fishing2)
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Fishing3)
    elif x == 0:
        main.cfg['pool_rod'] = 0
        Border()

            


def Fishing2():
    x = main.choose.get()
    if x == 1:
        main.p = 'pool_fishing.txt'
        main.Print()
        main.cfg['pool_check'] = False
        main.cfg['pool_fishing'] = True
        del pool_d[2]
        del main.inv[24]
        del main.inv[23]
        del main.inv[22]
        del main.inv[14]
        main.inv[25] = 'Рыба фугу'
        way.East()

def Fishing3():
    i =  main.choose.get()
    if i == 90:
        Fishing()
    elif i == 24 and main.cfg['pool_rod'] == 0:
        main.p = 'Уперев припасенную жердину в ограду, Ян приготовился к сборке удочки. Удилище в наличие, нужно остальное'
        main.Phrase()
        main.cfg['pool_rod'] += 1
        Fishing()
    elif i == 23 and main.cfg['pool_rod'] == 1:
        main.p = 'Ян достал веревку и привязал ее к жердине.'
        main.Phrase()
        main.cfg['pool_rod'] += 1
        Fishing()
    elif i == 22 and main.cfg['pool_rod'] == 2:
        main.p = 'Ян достал крючок от колета пьяницы и привязал его веревке. Что-ж, удочка готова.'
        main.Phrase()
        main.cfg['pool_rod'] += 1
        Fishing()
    elif i == 14 and main.cfg['pool_rod'] == 3:
        main.p = 'Ян достал оторванный член и насадил его на крючок. Хоть на что-то он сгодится. Ну вот, для рыбалки все готово.'
        main.Phrase()
        main.cfg['pool_rod'] += 1
        Fishing()
    elif i == 9:
        main.p = 'Решив использовать браконьерскую технику, Ян поджег шнур у шашечки с динамитом и швырнул ее в бассейн. Однако, вот незадача, при попадании в воду фитиль моментально потух. Обидно!'
        main.Phrase()
        del main.inv[9]
        Fishing()

            




    

    



