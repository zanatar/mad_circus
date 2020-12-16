slon_d = {1: 'Осмотреться' , 0: 'Уйти'}
slon_t = {1: 'Поговорить с конюхом' , 9: 'Инвентарь' , 0: 'Уйти'}
ass_d = {1: 'Потыкать задницу пальцем' , 2: 'Отшлепать ее как следует', 3: 'Погрузиться в задницу и исследовать ее изнутри',
         9: 'Инвентарь' , 0: 'Уйти'}
ass_in = {1: 'Морковка с легкостью проникла в слоновью задницу и словно затерялась там, судя по всему не доставив слону никакого дискомфорта.',
          2: 'Бутылка водки с легкостью проникла в слоновью задницу и словно затерялась там, судя по всему не доставив слону никакого дискомфорта.' ,
          3: 'Бутылка с пургеном с легкостью проникла в слоновью задницу и словно затерялась там, судя по всему не доставив слону никакого дискомфорта.' ,
          4: 'Пустая бутылка с легкостью проникла в слоновью задницу и словно затерялась там, судя по всему не доставив слону никакого дискомфорта.' ,
          5: 'Шашечка динамита с легкостью проникла в слоновью задницу и словно затерялась там, судя по всему не доставив слону никакого дискомфорта.' ,
          6: 'Ян достал зажигалку, поджег бикфордов шнур от шашечки и, на всякий случай, отбежал к углу вольера. Шнур догорел, раздался приглушенный хлопок внутри слона. Жипка отвлекшись от пожирания овощей, потерся задом о загородку и вернулся к прерванному занятию. Очевидно, мощность взрыва была недостаточна.' ,
          7: 'Шматок свиного жира с легкостью проник в слоновью задницу, параллельно от души ее смазав.' ,
          8: 'Ян достал глобус Украины и попытался засунуть его в задницу слону. Массивный глобус шел очень туго и не пролезал. Слон начал беспокоиться  и Ян счел благоразумным прекратить попытки. Однако желание засунуть глобус все не угасало.' ,
          9: 'Ян достал глобус украины и попытался засунуть его в задницу слону. В этот раз глобус проскочил в задницу без особых проблем. При этом явно ощущалось, что больше туда не влезет ничего. Внутренний голос подсказал Яну, что он все сделал правильно.' ,
          10: 'Внезапно, со стороны большого шатра, зазвучала какая-то какофония звуков. Услышав ее, конюх  занервничал и начал двигаться втрое быстрее. «-Хаспадин хороший», обратился конюх к Яну, «-шел бы ты  отсель ужо. Представленье скоро будет, слона готовить надо, а ты мешаешься». Заинтересованный Ян решил не тратить время зря и направился к шатру.' ,
           }
purg_s = {1: 'Ян подошел к бочке с пургеном. Данная субстанция вполне может пригодится, но в чем ее переносить? Не в горстях же.' ,
          2: 'Ян подошел к бочке с пургеном. Стараясь не запачкать руку он наполнил пустую бутылку содержимым бочки и завинтил крышку. «Водка особая» готова к употреблению.' ,
          3: 'Можно было бы использовать бочонок, он недостаточно герметичен для жидкостей'
          }
kon_d = {1: 'Звать тебя как?', 2: 'А это что за чудо?', 3: 'А почему это у слона такая большая... жопа?',
         4: 'И чего он тут делает?', 5: 'Чем поражать?', 6: 'А пурген зачем?'}



import main
import way
import cir

def Slon_way():
    main.sel = slon_d
    main.Refresh()
    main.btn.config(command=Slon)

def Slon():
    x = main.choose.get()
    if x == 1:
        if main.cfg['act3'] == False:
            main.p = 'slon_start.txt'
            main.Print()
            slon_d[2] = 'Подойти к слону'
        else:
            main.p ='После трагического завершения представления слонярня опустела.  Лишь бочка с пургеном и ящик с морковкой сиротливо стояли на своих местах.'
            main.Phrase()
        slon_d[3] = 'Cтащить морковку из ящика'
        slon_d[4] = 'Подойти к бочке с пургеном'
        main.Refresh()
    elif x == 2:
         main.p = 'Ян подошел к слону поближе. Конюх, похоже, не прочь поболтать, в отличие от слона'
         main.Phrase()
         slon_d[5] = 'Осмотреть слоновью задницу'
         main.sel = slon_t
         main.Refresh()
         main.btn.config(command=Kon)
    elif x == 3:
        if 3 in main.inv:
            main.p = 'Тут и с одной то морковкой непонятно, что делать. Куда уж с двумя.'
            main.Phrase()
        else:
            main.inv[3] = 'Морковка'
            main.p ='Ян подошел к ящику с морковкой и стащил оттуда одну.'
            main.Phrase()
            if main.cfg['act3'] == False:
                 main.p = 'Увлеченный кормлением слона конюх ничего не заметил.'
                 main.Phrase()
    elif x == 4:
        if 8 in main.inv:
            main.p = purg_s[2]
            main.Phrase()
            del main.inv[8]
            main.inv[10] = 'Бутылка с пургеном'
        elif 16 in main.inv:
            main.p = purg_s[1]
            main.Phrase()
            main.p = purg_s[3]
            main.Phrase()
        else:
            main.p = purg_s[1]
            main.Phrase()
    elif x == 5:
        main.p = 'Ян подошел к заднице слона. Впечатляюще огромная, она нависала над ним, словно отвесный утес, суровая и  непоколебимая. Внутри Яна все сильнее нарастало желание сделать с ней  что-нибудь эдакое.'
        main.Phrase()
        main.sel = ass_d
        main.Refresh()
        main.btn.config(command=Ass)
    elif x == 0:
        way.East()

                    
            
def Ass():
    x = main.choose.get()
    if x == 1:
        main.p = 'Weapon has no effect'
        main.Phrase()
    elif x == 2:
        main.p ='Да, да, получай плохой слоник!'
        main.Phrase()
    elif x == 3:
        main.p = 'Серьезно?'
        main.Phrase()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Ass1)
    elif x == 0:
        Slon_way()

def Ass1():
    i = main.choose.get()
    if i == 3:
        main.p = ass_in[1]
        main.Phrase()
        del main.inv[3]
        main.Inventory()
    elif i == 2:
        main.p = ass_in[2]
        main.Phrase()
        del main.inv[2]
        main.Inventory()
    elif i == 10:
        main.p = ass_in[3]
        main.Phrase()
        del main.inv[10]
        main.Inventory()
    elif i == 8:
        main.p = ass_in[4]
        main.Phrase()
        del main.inv[8]
        main.Inventory()
    elif i == 9:
        main.p = ass_in[5]
        main.Phrase()
        del main.inv[9]
        main.cfg['slon_din_arm'] = True
        main.Inventory()
    elif i == 7 and main.cfg['slon_din_arm'] == True:
        main.p = ass_in[6]
        main.Phrase()
        main.cfg['slon_din_arm'] = False
        main.Inventory()
    elif i == 12:
        main.p = ass_in[7]
        main.Phrase()
        del main.inv[12]
        main.cfg['slon_ass_lube'] = True
        main.Inventory()
    elif i == 13 :
        if main.cfg['slon_ass_lube'] == False:
            main.p = ass_in[8]
            main.Phrase()
        elif main.cfg['slon_ass_lube'] == True:
            if main.cfg['jong_end1'] == False:
                main.p ='Вы, безусловно, на правильном пути. Но перед тем, как сделать сие, увы, необратимое действие, рекомендую закончить дела в других местах'
                main.Phrase()
            elif main.cfg['jong_end1'] == True:
                main.p = ass_in[9]
                main.Phrase()
                del main.inv[13]
                del slon_d[2]
                del slon_d[5]
                main.cfg['act2'] = True
                main.cfg['circus_act2_start'] = True
                main.p = ass_in[10]
                main.Phrase()
                main.sel = {1: 'Переместиться в большой шатер' }
                main.Refresh()
                main.btn.config(command=Ass2)
    elif i == 90:
        Slon_way()
        
                
                
                
def Ass2():
    x = main.choose.get()
    if x == 1:
        cir.Circus()

         
         

        
def Kon():
    x = main.choose.get()
    if x == 1:
        main.p = 'slon_talk.txt'
        main.Print()
    elif x == 0:
        Slon_way()
    elif x == 9:
        main.Inventory()
        main.btn.config(command=Kon1)

def Kon1():
    i = main.choose.get()
    if i == 90:
        main_sel = slon_t
        main.Refresh()
        main.btn.config(command=Kon)
    elif i == 3:
        main.p ='Увидав протянутую морковку слон на секунду отвлекся от перемалывания брюквы ловким движением хобота выхватил ее у Яна и закинул в пасть.'
        main.Phrase()
        del main.inv[3]
        main_sel = slon_t
        main.Refresh()
        main.btn.config(command=Kon)

   
