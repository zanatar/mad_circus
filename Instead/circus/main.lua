instead_version "2.0.0"
require "theme"
require "format"
format.para = true
require "dlg"
--require "dbg"
require "toilets"
require "zakus"
require "rider"
require "slon"
require "shoot"
require "music"
require "zver"
require "circus"
require "direct"
require "pool"
require "jong"
require "trailers"

myxml = io.open('xxx.xml'):read('*all')
--game.forcedsc = true;


game.act = 'Не получается.';
game.inv = "Гм.. Не то..";
game.use = 'Не сработает...';

global {
	act2 = false;
	act3 = false;
	skol_taken = false;
	drunk_event = false;
	tablets_switch = false;
	toilet_check = false;
	toilet_destroy = false;
	pony_feed = false;
	pony_drink = 1;
	deer_carrot = 0;
	deer_boost = false;
	deer_rush =false;
	slon_armed =false;
	slon_lubed = false;
	tir_win = false;
	clown_drunk = false;
	stage1_end = false;
	stage3_end = false;
	stage_listen = false;
	romeo_listen =false;
	pig_caboom = false;
	pig_armed = false;
	doctor_check = false;
	pool_clean = false;
	waves_calm = false;
	fishing_rod = 0;
	jong_end2 = false;
	jong_end3 = false;
	circus_final = false;
	circus_act1_check = false;
	circus_act1_end = false;
	pool3_end = false;
	gam_end = loose
}

main = room {
	nam = 'Приветствие',
	enter = function()
		set_music('start.ogg');
		theme.gfx.bg('start.png');
		theme.win.color('white', 'red', 'blue');
	end,
	dsc = function() pn (string.match(myxml, "<welcome>(.-)</welcome>"))	end,
	obj = {
		'agree';
		'decline';
		'credits';
	};
};

agree = obj{
	nam = 'согласие',
	dsc = [[{Мне есть 18 лет. Я согласен с Условиями и предупрежден о возможном вреде здоровью, психике и тд и тп блаблабла...}]],
	act = function() walk(intro) end,
};

decline = obj{
	nam = 'отказ',
	dsc = [[{^^Нее, пойду-ка я лучше в Sims!}]],
	act = function()
		pn'До свидания.';
		stead.menu_toggle('quit');
	end,
};


credits = obj{
	nam = 'cred',
	dsc = [[{^^Cоздатели}]],
	act = function()
		set_music('credits.ogg');
		pn (string.match(myxml, "<credits>(.-)</credits>"));
			if here() ~= main then
				pn '^^Уважаемые господа, представление закончено! Всем спасибо и до скорой встречи!';
			end;
		end,
};

intro = room{
	nam = 'Вступление',
	enter = function()
		set_music('start.ogg');
		theme.gfx.bg('intro.png');
		theme.win.color('black', 'red', 'green');
	end,
	dsc = function() pn (string.match(myxml, "<intro1>(.-)</intro1>"))	end,
	obj = {
		'intro2';
		'intro3:disable()';
		'intro4:disable()';
		'go:disable()'
		},
};

intro2 = obj{
	nam ='intro2',
	dsc = [[{Голос?}]],
	act = function(s)
		pn (string.match(myxml, "<intro2>(.-)</intro2>"));
		s:disable();
		enable('intro3');
	end,
};

intro3 = obj{
	nam ='intro3',
	dsc = [[{Как все непросто...}]],
	act = function(s)
		pn (string.match(myxml, "<intro3>(.-)</intro3>"));
		s:disable();
		enable('intro4');
	end,
};


intro4 = obj{
	nam ='intro4',
	dsc = [[{И???}]],
	act = function(s)
		pn (string.match(myxml, "<intro4>(.-)</intro4>"));
		s:disable();
		enable('go');
	end,
};


go = obj{
	nam = 'start',
	dsc = [[{"Помочь" Яну}]],
	act = function() walk(index) end,
};

