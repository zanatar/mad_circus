zoo = room{
	nam = 'Зверинец',
	enter = function()
		set_music('durak.ogg');
		theme.gfx.bg('zver.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	dsc = function() pn (string.match(myxml, "<zver_start>(.-)</zver_start>"))	end;
	way = {'index';'deer_cage'; 'seal_cage';'pig_cage' },
--	enter = function()	if act3 == true then disable('deer_cage') end,
};
deer_cage = room{
	nam = 'Клетка с оленем',
	forcedsc = true,
	enter = function()
		theme.gfx.bg('zver.png');
		theme.win.color('white', 'yellow', 'blue');
		if act3 == true then
			pn'Клетка с оленем неожиданно опустела';
			walk (zoo);
		end;
	end,
	dsc = [[^^ ^^ ^^ ^^ ^^Ян подошел к корявой, давно не чищенной клетке.]],
	obj = {'deer1'},
	way = {'zoo'},
};
deer1 = obj{
	nam = 'Олень',
	dsc = function() pn (string.match(myxml, "<zver_deer>(.-)</zver_deer>"))	end;
	act = [[Все силы оленя уходят на поддержание равновесия.]],
	used = function(s,w)
		if w == carrot then
			inv():del(w);
			pn (string.match(myxml, "<zver_deer_feed>(.-)</zver_deer_feed>"));
		end;
	end,
};
seal_cage = room{
	nam = 'Клетка с тюленем',
	forcedsc = true,
	enter = function()
		theme.gfx.bg('zver.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	dsc = [[^^ ^^ ^^ ^^ ^^Ян подошел к средних размеров клетке, в центре которой стояло большое корыто с водой.]],
	way = {'zoo'},
	obj = {'seal'},
};
seal = obj{
	nam = 'Тюлень',
	dsc = [[Рядом с корытом лежит {тюлень} и спит. Или притворяется, что спит.]],
	act = [[Тюлень не реагирует]],
	used = function(s,w)
		if w == carrot then
			pn'Ян кинул морковку тюленю. Тюлень не отреагировал. Очевидно, тюлени морковку не едят.';
			inv():del(w);
		elseif w == fugu then
			pn (string.match(myxml, "<zver_key>(.-)</zver_key>"));
			inv():del(w);
			take('key');
			circus_final = true;
		end;
	end,
};
key = obj{
	nam = '"Золотой" ключик',
};
pig_cage = room{
	nam = 'Загон свиньи',
	forcedsc = true,
	way = {'zoo'},
	enter = function()
		theme.gfx.bg('zver_pig.png');
		theme.win.color('white', 'yellow', 'red')
		if pig_caboom == true then
			pn 'Загон пуст, и лишь пятна крови и жира тут и там напоминают о случившейся трагедии.';
			walk (zoo);
		end;
	end,
	obj = {'pig'},
	dsc = function() pn (string.match(myxml, "<zver_pig_start>(.-)</zver_pig_start>"))	end;
};
pig = obj{
	nam = 'Свинья',
	dsc = function() pn (string.match(myxml, "<zver_boar>(.-)</zver_boar>"))	end;
	act = [[Свинья нагло продолжает лежать в грязи. Ей все по барабану. Как же бесит!!]],
	used = function(s,w)
		if w == carrot then
			pn'Ян кинул морковку в открытую пасть свиньи. Пасть захлопнулась.';
			inv():del(w);
		elseif w == dynamite then
			pn'Ян кинул шашечку динамита в открытую пасть свиньи. Пасть захлопнулась.';
			pig_armed = true;
			inv():del(w);
		elseif w == zippo and pig_armed == true then
			walk('waait')
		end;
	end,
};

waait = room{
	nam = 'Уже почти...!',
	enter = function() disable('leave') end,
	dsc = function() pn (string.match(myxml, "<zver_armed>(.-)</zver_armed>"))	end;
	obj = { 'boom';
			'leave:disable()';
			},
};
boom = obj{
	nam = 'Бдыщ',
	dsc = [[{Катарсис, очищение, да, да, да!!!}]],
	act = function(s)
		theme.gfx.bg('zver_blow.png');
		theme.win.color('white', 'yellow', 'blue');
		take('salo');
		pn (string.match(myxml, "<zver_caboom>(.-)</zver_caboom>"));
		pig_caboom = true;
		disable(s);
		enable('leave');
	end,
};

salo = obj{
	nam = 'Шматок сала',
};






