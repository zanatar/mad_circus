tent = room{
	nam = 'Большой шатер',
	way = {'index'},
	enter = function()
		if act2 == true and act3== false then walk('tent2');
		elseif act3 == true and circus_final == false then walk('tent_middle');
		elseif circus_final == true then walk('tent3');
		elseif circus_act1_end == false and circus_act1_check == true then walk('tent11');
		elseif circus_act1_end == false and circus_act1_check == false then walk('tent1');
		else pn 'В шатре пусто. Никого нет. Делать тут больше нечего.' end;
	end,
}

tent1 = room{
	nam = 'Большой шатер: Мануальный монолог',
	enter = function(s)
		set_music('vbare.ogg');
		theme.gfx.bg('circus1.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	dsc = function() p (string.match(myxml, "<act1_1>(.-)</act1_1>"))	end;
	way = {'index'},
	obj = {
		'act1_2';
		'act1_3:disable()';
		'chpok:disable()';
		},
};
act1_2 = obj{
	nam ='act12',
	dsc = [[{^^Зайти внутрь}]],
	act = function(s)
		pn (string.match(myxml, "<act1_2>(.-)</act1_2>"));
		disable(s);
		enable('act1_3');
	end,
};
act1_3 = obj{
	nam = 'act13',
	dsc = [[{Дождаться начала представления}]],
	act = function(s)
		pn (string.match(myxml, "<act1_3>(.-)</act1_3>"));
		disable(s);
		circus_act1_check = true;
		enable('chpok');
	end,
};
chpok = obj{
	nam = 'Чпок',
	dsc = function()
		if here() == tent11 then
			pn '{Клоун} Чпок не знает устали.'
		else pn 'На удивленные возгласы, смешки и шум пересаживающихся в поиске более интересного ракурса зрителей {клоун} внимания не обращал - видимо старик был глуховат.'
		end;
	end,
	act = [[^^ ^^ ^^ ^^ ^^ ^^Чпок чертовски увлечен своим занятием и не реагирует]],
	used = function(s,w)
		if w == horn then
			pn (string.match(myxml, "<act1_end>(.-)</act1_end>"));
			circus_act1_end = true;
			inv():del(w);
			disable(s);
		end;
	end,
};
tent11 = room{
	way = {'index'},
	nam = 'Большой шатер: Мануальный монолог',
	enter = function(s)
		set_music('vbare.ogg');
		theme.gfx.bg('circus1.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	dsc = [[Мануальный монолог продолжается.]],
	obj = {'chpok'},
};
tent2 = room{
	nam = 'Большой шатер: Слоновий рекорд',
	enter = function(s)
		set_music('marsh.ogg');
		theme.gfx.bg('circus2.png');
		theme.win.color('white', 'cyan', 'blue');
		disable('leave');
	end,
	dsc = function() pn (string.match(myxml, "<act2_1>(.-)</act2_1>"))	end;
	obj = {
		'act2_2';
		'act2_3:disable()';
		'act2_4:disable()';
		'act2_5:disable()';
		'act2_6:disable()';
		'act2_end1:disable()';
		'act2_end2:disable()';
		'leave:disable()';
	},
};
act2_2 = obj{
	nam = 'act22',
	dsc = [[{Дождаться начала представления}]],
	act = function(s)
		pn (string.match(myxml, "<act2_2>(.-)</act2_2>"));
		disable(s);
		enable('act2_3');
	end,
};
act2_3 = obj{
	nam = 'act23',
	dsc = [[{Слушать речь директора}]],
	act = function(s)
		pn (string.match(myxml, "<act2_3>(.-)</act2_3>"));
		disable(s);
		enable('act2_4');
	end,
};
act2_4 = obj{
	nam = 'act24',
	dsc = [[{Ого, слон!}]],
	act = function(s)
		pn (string.match(myxml, "<act2_4>(.-)</act2_4>"));
		disable(s);
		enable('act2_5');
	end,
};
act2_5 = obj{
	nam = 'act25',
	dsc = [[{Воздержаться от апплодисментов}]],
	act = function(s)
		pn (string.match(myxml, "<act2_5>(.-)</act2_5>"));
		disable(s);
		enable('act2_6');
	end,
};
act2_6 = obj{
	nam = 'act26',
	dsc = [[{Выйти из сектора обстрела}]],
	act = function(s)
		pn (string.match(myxml, "<act2_6>(.-)</act2_6>"));
		disable(s);
		enable('act2_end1');
	end,
};
act2_end1 = obj{
	nam = 'act2end1',
	dsc = [[{Нуу... Нуу??? Нуу!!!}]],
	act = function(s)
		theme.gfx.bg('circus21.png');
		pn (string.match(myxml, "<act2_end1>(.-)</act2_end1>"));
		disable(s);
		enable('act2_end2');
	end,
};
act2_end2 = obj{
	nam = 'act2end2',
	dsc = [[{ВАХ!!!}]],
	act = function(s)
		pn (string.match(myxml, "<act2_end2>(.-)</act2_end2>"));
		act3 = true;
		disable(s);
		enable('leave');
	end,
};

tent_middle = room{
	nam = 'Большой шатер',
	enter = function(s)
		set_music('kozl.ogg');
		theme.gfx.bg('circus_mid.png');
		theme.win.color('white', 'yellow', 'red');
	end,
	way = {'index'},
	dsc = [[В шатре царит разруха и запустение.]],
	obj = {'slon_corpse'},
};
slon_corpse = obj{
	nam ='Труп Жипки',
	dsc = [[Посреди арены все еще лежат {останки} несчастного Жипки.]],
	act = function() pn (string.match(myxml, "<middle_check>(.-)</middle_check>"))	end;
	used = function(s,w)
		if w == barrel then
			pn (string.match(myxml, "<middle_use>(.-)</middle_use>"));
			inv():del(w);
			take ('barrel_full');
		end;
	end,
};
barrel_full = obj{
	nam = 'Бочонок слоновьего жира',
};

tent3 = room{
	forcedsc = false,
	nam = 'Большой шатер: Из пушки на луну.',
	enter = function(s)
		set_music('pushka.ogg');
		theme.gfx.bg('circus3.png');
	theme.win.color('white', 'yellow', 'red');
	end,
	dsc = function() pn (string.match(myxml, "<act3_1>(.-)</act3_1>"))	end;
	obj = {
		'act3_2';
		'act3_3:disable()';
		'act3_4:disable()';
		'act3_5:disable()';
		'act3_6:disable()';
		'act3_7:disable()';
		'act3_8:disable()';
	},
};
act3_2 = obj{
	nam = 'act32',
	dsc = [[{Ждать}]],
	act = function(s)
		pn (string.match(myxml, "<act3_2>(.-)</act3_2>"));
		disable(s);
		enable('act3_3');
	end,
};
act3_3 = obj{
	nam = 'act33',
	dsc = [[{Слушать Пипкина}]],
	act = function(s)
		pn (string.match(myxml, "<act3_3>(.-)</act3_3>"));
		disable(s);
		enable('act3_4');
	end,
};
act3_4 = obj{
	nam = 'act34',
	dsc = [[{Обратить внимание на сцену}]],
	act = function(s)
		pn (string.match(myxml, "<act3_4>(.-)</act3_4>"));
		disable(s);
		enable('act3_5');
	end,
};
act3_5 = obj{
	nam = 'act35',
	dsc = [[{Интересно, выдержит ли колода?}]],
	act = function(s)
		pn (string.match(myxml, "<act3_5>(.-)</act3_5>"));
		disable(s);
		enable('act3_6');
	end,
};
act3_6 = obj{
	nam = 'act36',
	dsc = [[{Сейчас что-то будет!}]],
	act = function(s)
		pn (string.match(myxml, "<act3_6>(.-)</act3_6>"));
		disable(s);
		enable('act3_7');
	end,
};
act3_7 = obj{
	nam = 'act37',
	dsc = [[{Ну воот!}]],
	act = function(s)
		pn (string.match(myxml, "<act3_7>(.-)</act3_7>"));
		disable(s);
		enable('act3_8');
	end,
};
act3_8 = obj{
	nam = 'act38',
	dsc = [[{Смело выйти на арену}]],
	act = function() walk('tent31') end,
};
tent31 = room{
	nam = 'Большой шатер: Из пушки на луну.',
	enter = function(s)
		set_music('pike.ogg');
		theme.gfx.bg('circus3.png');
		theme.win.color('white', 'yellow', 'red');
	end,
	dsc = [[И вот Ян на арене. Наступил его звездный час!]],
	obj = {
		'cannon';
		'start_false:disable()';
		'upgrade:disable()';
		'start_sucsess:disable()';
		},
};
cannon = obj{
	nam = 'Пушка',
	dsc = [[{"Пушка"} готова к отправке Яна в полет.]],
	act = function()
		pn (string.match(myxml, "<act3_cannon>(.-)</act3_cannon>"));
		enable('start_false');
	end,
	used = function(s,w)
		if w == box_of_chemistry then
			pn (string.match(myxml, "<act3_chemistry>(.-)</act3_chemistry>"));
			enable('upgrade');
			inv():del(w);
		elseif w == box_of_zoo then
			pn (string.match(myxml, "<act3_zoo>(.-)</act3_zoo>"));
			inv():del(w);
		elseif w == box_of_physics then
			pn (string.match(myxml, "<act3_physics>(.-)</act3_physics>"));
			inv():del(w);
		end;
	end,
};
upgrade = obj{
	nam = 'Улучшение пушки',
	dsc = [[{Улучшить "пушку"}]],
	act = function(s)
		if have (barrel_full) and have(vodka) and have (dynamite) then
			pn (string.match(myxml, "<act3_upgrade>(.-)</act3_upgrade>"));
			inv():del('vodka');
			inv():del('barrel_full');
			inv():del('zippo');
			inv():del('dynamite');
			disable('start_false');
			disable(s);
			enable('start_sucsess');
		else pn 'Инструкцию Ян осилить сумел, но увы, подручных средств было недостаточно!'
		end;
	end,
};
start_false = obj{
	nam = 's_false',
	dsc = [[{И тааак сойдет!}]],
	act = function() walk ('circus_loose') end,
};
start_sucsess = obj{
	nam = 's_win',
	dsc = [[{Поехали!}]],
	act = function() walk ('circus_win') end,
};

circus_loose = room{
	nam = 'Полет',
	dsc = function() pn (string.match(myxml, "<act3_loose1>(.-)</act3_loose1>"))	end,
	obj = {
	'fail';
	'sic:disable()';
	},
};
fail = obj{
	nam = 'Фейл',
	dsc = [[{Дааа! Я лечу!}]],
	act = function(s)
		pn (string.match(myxml, "<act3_loose2>(.-)</act3_loose2>"));
		disable(s);
		enable('sic');
	end,
};
sic = obj{
	nam = 'Так',
	dsc = [[{Sic transit Gloria mundi}]],
	act = function()
		gam_end = loose;
		walk ('game_end');
	end,
};
circus_win = room{
	nam = 'Полет',
	dsc = function() pn (string.match(myxml, "<act3_win1>(.-)</act3_win1>"))	end,
	obj = {
		'fly';
		'win:disable()';
		},
};
fly = obj{
	nam = 'flyy',
	dsc = [[{Дааа! Я лечу!}]],
	act = function(s)
		pn (string.match(myxml, "<act3_win2>(.-)</act3_win2>"));
		disable(s);
		enable('win');
	end,
};
win = obj{
	nam = 'wwin',
	dsc = [[{Удачи, Ян!}]],
	act = function()
		gam_end = win;
		walk ('game_end');
	end,
};
game_end = room{
	nam = 'Миссия выполнена',
	dsc = function()
		if gam_end == win then
			theme.gfx.bg('win.png');
			theme.win.color('white', 'yellow', 'blue');
			pn (string.match(myxml, "<game_win>(.-)</game_win>"));
		elseif gam_end == secret then
			pn (string.match(myxml, "<game_secret>(.-)</game_secret>"));
		else
			theme.gfx.bg('loose.png');
			theme.win.color('white', 'yellow', 'blue');
			pn (string.match(myxml, "<game_loose>(.-)</game_loose>"));
		end;
	end,
	obj = {'credits'},
};


