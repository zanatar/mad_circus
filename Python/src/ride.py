ride_d = {1: 'Осмотреться', 0: 'Уйти'}
pony_d = {1: 'Погладить пони' , 2: 'Понаблюдать за катанием' , 0: 'Уйти'}
pony_ride = {1: '«Пони» явно был не в форме. Устало передвигая ногами, он медленно провез посаженного на него ребенка по кругу. Тот казался недовольным и пытался ускорить движение дергая за уздечку и пиная ножками по бокам животного, но тщетно.' ,
             2: 'После недавнего угощения «пони» явно стал бодрее. Кавалерийским шагом провез он очередного седока вокруг манежа. Ребенок был доволен и всячески выделывался в процессе, изображая не то вождя краснокожих, не то страдая от геморроя.' ,
             3: 'После недавнего угощения «пони» стал еще бодрее. Лихим галопом протащил он седока аж 2 круга, правда периодически покачиваясь и запинаясь. Ребенок, явно не ожидавший такой прыти, с испугом держался за его гриву, пытаясь не расплакаться.'
             }
pony_drunk = {1: 'Ян подошел к «пони» и показал ему бутылку  водки. Тот, увидя гостинец, сильно оживился, радостно ржа и подмигивая. Ян открутил пробку и, прикрыв своим телом морду «пони», влил ее содержимое по назначению. Приняв угощение, «пони» благодарно поглядел на Яна, дав, впрочем, мимикой и ржанием, понять, что он вовсе не против добавки.' ,
              2: 'Ян подошел к «пони» и показал ему бутылку  с пургеном. Тот, увидя гостинец, сильно оживился, радостно ржа и подмигивая. Ян открутил пробку и, прикрыв своим телом морду «пони», попытался влить ее по назначению но зверь учуял незнакомый запах и отказался это пить, расплескав все содержимое.' ,
              3: 'Оставшуюся после угощения пустую бутылку Ян прибрал себе – пригодится.' ,
              4: 'Оставшуюся после угощения пустую бутылку Ян выбросил : бутылка у него уже была, зачем ему две – он придумать не мог.' ,
              5: 'Ян подошел к «пони» и протянул ему морковку. Тот скосил на нее глаза и изобразил мордой несоответствие  подношения желаемому. Принюхавшись, Ян уловил тонкий шлейф перегара в запахе лошадки. '
              }

deer_d = {1:'Наблюдать за катанием' , 0: 'Уйти'}

import way
import main


def Ride_way():
    if main.cfg['ride_skol'] == True and 3 in ride_d:
        del ride_d[3]
    main.sel = ride_d
    main.Refresh()
    main.btn.config(command=Ride)

def Ride():
    x = main.choose.get()
    if x == 1 and main.cfg['act3'] == False and main.cfg['ride_end1'] == False:
        main.p = 'ride_act1.txt'
        main.Print()
        if main.cfg['ride_skol'] == False:
            main.p = 'В стороне от манежа находилась большая лужа. Мутная вода изредка колыхалась, словно что-то двигалось в глубине.'
            main.Phrase()
            ride_d[3] = 'Засунуть руку в лужу'
        ride_d[2] = 'Подойти к ограде'
        main.Refresh()
    elif x == 1 and main.cfg['act3'] == False and main.cfg['ride_end1'] == True:
        main.p = 'Манеж пуст, никого нет, ничего не происходит.'
        main.Phrase()
    elif x == 1 and main.cfg['ride_end3'] == True:
        main.p = 'Манеж пуст, никого нет, ничего не происходит.'
        main.Phrase()
    elif x == 1 and main.cfg['act3'] == True and main.cfg['ride_end3'] == False:
        main.p = 'ride_act3.txt'
        main.Print()
        ride_d[2] = 'Подойти к ограде'
        main.Refresh()
    elif x == 2  and main.cfg['act3'] == False and main.cfg['ride_end1'] == False:
        Pony()
    elif x == 2 and main.cfg['act3'] == True and main.cfg['ride_end3'] == False:
        main.p = 'Ян остановился у ограды, решив понаблюдать за катанием.'
        main.Phrase()
        Deer()
    elif x == 3 and main.cfg['act3'] == False and main.cfg['ride_skol'] == False:
        main.p = 'ride_skol.txt'
        main.Print()
        main.cfg['ride_skol'] = True
        main.inv[1] = 'Сколопендра'
        main.Refresh()
    elif x == 3 and main.cfg['act3'] == False and main.cfg['ride_skol'] == True and main.cfg['ride_check1'] == True:
        main.p = 'Сколько ни копался ян в луже, больше ничего ценного найти ему так и не удалось'
        main.Phrase()
    elif x == 0:
        way.East()

def Pony():
    main.sel = pony_d
    main.Refresh()
    main.btn.config(command=Pony1)

def Pony1():
    x = main.choose.get()
    if x == 1:
        main.p ='ride_pony.txt'
        main.Print()
        pony_d[9] = 'Инвентарь'
        main.Refresh()
    elif x == 2 and main.cfg['ride_pony_drunk'] == 0:
        main.p = pony_ride[1]
        main.Phrase()
    elif x == 2 and main.cfg['ride_pony_drunk'] == 1:
        main.p = pony_ride[2]
        main.Phrase()
    elif x == 2 and main.cfg['ride_pony_drunk'] == 2:
        main.p = pony_ride[3]
        main.Phrase()
    elif x == 2 and main.cfg['ride_pony_drunk'] == 3:
        main.p = 'ride_end1.txt'
        main.Print()
        main.cfg['ride_end1'] = True
        main.inv[7] = 'Зажигалка'
        del ride_d[2]
        main.Refresh()
        Ride_way()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Pony2)
    elif x == 0:
        Ride_way()

def Pony2():
    i = main.choose.get()
    if i == 90:
        Pony()
    elif i == 2:
        main.p = pony_drunk[1]
        main.Phrase()
        del main.inv[2]
        if 8 not in main.inv:
            main.inv[8] = 'Пустая бутылка'
            main.p = pony_drunk[3]
            main.Phrase()
        else:
            main.p = pony_drunk[4]
            main.Phrase()
        main.cfg['ride_pony_drunk'] +=1
        Pony()
    elif i == 3:
        main.p = pony_drunk[5]
        main.Phrase()
    elif i == 10:
        main.p = pony_drunk[2]
        main.Phrase()
        del main.inv[10]
        if 8 not in main.inv:
            main.inv[8] = 'Пустая бутылка'
            main.p = pony_drunk[3]
            main.Phrase()
        else:
            main.p = pony_drunk[4]
            main.Phrase()
        Pony()



def Deer():
    main.sel = deer_d
    main.Refresh()
    main.btn.config(command=Deer1)

def Deer1():
    x = main.choose.get()
    if x == 1 and main.cfg['deer_rush'] == False:
        main.p = 'ride_deer.txt'
        main.Print()
        deer_d[9] = 'Инвентарь'
        main.cfg['ride_deer_check'] = True
        main.Refresh()
    elif x == 1 and main.cfg['deer_rush'] == True:
        main.p = 'ride_end3.txt'
        main.Print()
        main.inv[24] = 'Жердина'
        main.cfg['ride_end3'] = True
        main.cfg['pool_check'] = False
        del ride_d[2]
        Ride_way()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Deer2)
    elif x == 0:
        Ride_way()

def Deer2():
    i = main.choose.get()
    if i == 90:
        Deer()
    elif i == 11:
        main.p = 'Ян подошел к Оленю и вколол ему весь шприц с адреналином. Олень преобразился, его ноги перестали трястись, он часто задышал и его глаза бешено завращались.'
        main.Phrase()
        main.cfg['deer_rush'] = True
        del main.inv[11]
        Deer()
    elif i == 3:
        main.p = 'ride_carrot.txt'
        main.Print()
        del main.inv[3]
        main.cfg['ride_carrots'] +=1
        if main.cfg['ride_carrots'] == 42:
            main.p = 'ride_carrot.txt'
            main.Print()
            main.p = 'Мои поздравления! Вы открыли секретную концовку! Однако, у хороших игр есть много концовок. Не желаете ли найти их все?'
            main.sel = {1: 'Всенепременно!'}
            main.Refresh()
            main.btn.config(command=Start)

            

        
    


        















