toilet = room {
	nam = 'Туалеты',
	enter = function()
		set_music('kozl.ogg')
		theme.gfx.bg('toi.png')
		theme.win.color('white', 'yellow', 'blue');
	end,
	forcedsc = true,
	dsc = [[^^ ^^ ^^ ^^ ^^Две наспех сколоченные кабинки стоят у ограды цирка.]],
	way = { 'index' },
	obj = {'tablets' , 'm','g' ,
	};
};

m = obj {
	nam = '"МЭ"',
	dsc = [[{"МЭ"}]],
	act = function()
		if toilet_destroy == true then
			pn 'Туалет с табличкой "МЭ" сильно поврежден. Воспользоваться им по назначению не выйдет.';
		elseif tablets_switch == false then
			if drunk_event == true then
				pn (string.match(myxml, "<toilet_fail>(.-)</toilet_fail>"));
				drunk_event = false;
				enable('drunk');
				toilet_check = true;
			elseif drunk_event == false then
				pn (string.match(myxml, "<toilet_m>(.-)</toilet_m"));
			end;
		else
			pn (string.match(myxml, "<toilet_fem_m>(.-)</toilet_fem_m>"));
		end;
	end,
};
g = obj{
	nam = '"ЖО"',
	dsc = [[и {"ЖО"}, кое-как прикрепленные к дверцам, а также жуткая вонь. Только безысходность и/или пренебрежение всеми правилами санитарии и личной гигиены могут подвигнуть кого-либо на посещение сих заведений. Впрочем, наличие достаточно широких смотровых щелей в конструкции дает возможность хоть как-то позабавиться.]],
	act = function()
		if tablets_switch == true then
			if drunk_event == true then
				walkin(toilet_win1);
			else
				pn (string.match(myxml, "<toilet_f>(.-)</toilet_f>"));
			end;
		else
			pn (string.match(myxml, "<toilet_fem_f>(.-)</toilet_fem_f>"));
		end;
	end;
};
tablets = obj{
	nam = 'таблички',
	dsc = [[Об их назначении красноречиво свидетельствуют {таблички}]],
	act = function(s)
		if toilet_check == true then
			pn (string.match(myxml, "<toilet_switch>(.-)</toilet_switch>"));
			tablets_switch = true;
			s.dsc = [[Об их назначении красноречиво свидетельствуют таблички]];
		end;
	end;
};
toilet_win1 = room {
	nam = 'Шалость удалась',
	dsc = function()
		pn (string.match(myxml, "<toilet_win1>(.-)</toilet_win1>"));
	end,
	obj = {vway('continue' , '{^Прислушаться}' , 'toilet_win2')},
};

toilet_win2 = room {
	nam = 'Успех!',
	enter = function()
		theme.gfx.bg('fem_end.png')
		pr (string.match(myxml, "<toilet_win2>(.-)</toilet_win2>"));
		theme.win.color('white', 'yellow', 'blue');
		take('egg');
		take('penis');
		toilet_destroy = true;
		drunk_event = false;
	end,
	obj = {vway('continue' , '{^Уйти}' , 'toilet')};
};
egg = obj {
	nam = 'Стальное яйцо',
};
penis = obj{
	nam = 'Оторванный член',
};







