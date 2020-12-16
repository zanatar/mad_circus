import zak
import toi
import cir
import main
import slon
import tir
import trail
import stage
import jong
import ride
import pool
import zver
west_d = {1: 'Зайти в большой шатер' , 2:'Подойти к закусочной' , 3: ' К туалетам' ,
          4: 'Пойти на север' , 5: 'Пойти на восток' , 6: 'Пойти на юг' , 0:'Уйти из цирка'}
north_d = {1: 'Заглянуть в зверинец' , 2: 'Подойти к площадке жонглеров' ,
           3: 'Пойти на запад' , 4: 'Пойти на восток' , 5: 'Пойти на юг' }
east_d = {1:'Подойти к слонярне' , 2:'Подойти к бассейну' , 3:'Подойти к манежу' ,
          4: 'Пойти на север' , 5: 'Пойти на запад' , 6: 'Пойти на юг'}

south_d = {1:' Подойти к площадке музыкантов' , 2:'Подойти к тиру' , 3:'Идти к трейлерам персонала' ,
          4: 'Пойти на север' , 5: 'Пойти на запад' , 6: 'Пойти на восток'}


def West():
    main.p = 'way_west.txt'
    main.Print()
    main.sel = west_d
    main.Refresh()
    main.btn.config(command=West1)

def West1():
    x = main.choose.get()
    if x == 1:
        cir.Circus()
    elif x == 2:
        zak.Zak_way()
    elif x == 3:
        toi.Toi_way()
    elif x == 4:
        North()
    elif x == 5:
        East()
    elif x == 6:
        South()
    elif x == 0:
        main.Exit()

def East():
    main.p = 'way_east.txt'
    main.Print()
    main.sel = east_d
    main.Refresh()
    main.btn.config(command=East1)

def East1():
    x = main.choose.get()
    if x == 1:
        slon.Slon_way()
    elif x == 2:
        pool.Pool_way()
    elif x == 3:
        ride.Ride_way()
    elif x == 4:
        North()
    elif x == 5:
        West()
    elif x == 6:
        South()
def South():
    main.p = 'way_south.txt'
    main.Print()
    main.sel = south_d
    main.Refresh()
    main.btn.config(command=South1)

def South1():
    x = main.choose.get()
    if x == 2:
        tir.Tir_way()
    elif x == 1:
        stage.Stage_way()
    elif x == 3:
        trail.Trailer_way()
    elif x == 4:
        North()
    elif x == 6:
        East()
    elif x == 5:
        West()
def North():
    main.p = 'way_north.txt'
    main.Print()
    main.sel = north_d
    main.Refresh()
    main.btn.config(command=North1)

def North1():
    x = main.choose.get()
    if x == 1:
        zver.Zver_way()
    elif x == 2:
        jong.Jong_way()
    elif x == 3:
        West()
    elif x == 4:
        East()
    elif x == 5:
        South()
    

    
