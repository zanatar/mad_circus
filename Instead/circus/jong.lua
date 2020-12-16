jongler = room{
	nam = 'Площадка жонглеров',
	enter = function()
		if circus_act1_end == true and jong_end2 == false then
			walk(jong2);
		elseif act3 == true and jong_end3 == false then
			walk(jong3);
		else
			pn 'Площадка жонглеров пуста';
			walk(index);
		end;
	end,
};

jong2 = room{
	nam = 'Площадка жонглеров',
	way = {'index'},
	enter = function()
		set_music('durak.ogg');
		theme.gfx.bg('jong1.png');
		theme.win.color('white','yellow', '#4694ec');
	end,
	dsc = [[^^ ^^ ^^На площадке для жонглеров началось выступление. ]],
	obj = {'atlet'},
};

atlet = obj{
	nam = 'жонглер',
	dsc = function() pn (string.match(myxml, "<jong_atlet>(.-)</jong_atlet>"))	end;
	act = [[Жонглер занят представлением и не обращает внимания на публику.]],
	used = function(s,w)
		if w == kettlebell then
			s:disable();
			inv():del(w);
			take('globus');
			pn (string.match(myxml, "<jong_end2>(.-)</jong_end2>"));
			jong_end2 = true;
		end;
	end;
};

jong3 = room{
	nam = 'Площадка жонглеров',
	way = {'index'},
	enter = function()
		set_music('durak.ogg');
		theme.gfx.bg('jong3.png');
		theme.win.color('white','yellow', '#4694ec');
	end,
	dsc = [[^^Площадка жонглеров пустовала, как и прежде.]],
	obj = {'hang'},
};

hang = obj{
	nam = 'Труп',
	dsc = function() pn (string.match(myxml, "<jong_hang>(.-)</jong_hang>"))	end;
	act = function(s)
		s:disable();
		take('rope');
		jong_end3 = true;
		pn (string.match(myxml, "<jong_end3>(.-)</jong_end3>"));
	end,
};

globus = obj{
	nam = 'Глобус украины',
};

rope = obj{
	nam = 'Кусок веревки',
};




