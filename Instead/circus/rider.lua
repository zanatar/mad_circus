ride = room {
	nam = '1',
	enter = function()
		if act3 == true then
			walkin(ride3)
		else
			walkin(ride1)
		end;
	end,
};
ride1 = room {
	nam ="Манеж",
	enter = function()
		set_music('dogon.ogg');
		theme.gfx.bg('ride1.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	way = { 'index' },
	forcedsc = true,
	dsc = [[Манеж представлял собой круглую ограду из кривых и косых жердин, держащихся на честном слове и соплях. ]],
	obj = {
		'pony',
		'puddle',
		'galop',
	};
};
pony = obj{
	nam = 'пони',
	dsc = function() pn (string.match(myxml, "<ride1_pony>(.-)</ride1_pony>"))	end;
	act = function()
		pn (string.match(myxml, "<pony_act>(.-)</pony_act>"));
	end;
	used = function(s, w)
		if w == carrot then
			pn (string.match(myxml, "<pony_carrot>(.-)</pony_carrot>"));
			pony_feed = true;
			inv():del('carrot');
		elseif w == vodka and pony_feed == true then
			pn (string.match(myxml, "<pony_vodka>(.-)</pony_vodka>"));
			pony_drink = pony_drink + 1;
			inv():del('vodka');
			if not have (empty_bottle) then
				take ('empty_bottle');
				pn 'Оставшуюся пустую бутылку хозяйственный Ян прибрал.';
			else
				pn'Как ни любил Ян сбор стеклотары, но одной бутылки ему пока было достаточно'
			end;
		elseif w == purgen then
			pn (string.match(myxml, "<pony_purgen(.-)</pony_purgen>"));
			inv():del('purgen');
			if not have (empty_bottle) then
				take ('empty_bottle');
				pn 'Оставшуюся пустую бутылку хозяйственный Ян прибрал.';
			else
				pn'Как ни любил Ян сбор стеклотары, но одной бутылки ему пока было достаточно'
			end;
		end;
	end,
};
puddle = obj{
	nam = 'лужа',
	dsc = function()
			pn (string.match(myxml, "<ride1_puddle>(.-)</ride1_puddle>"));
	end,
	act = function(s)
		if skol_taken == true then pn'Сколько не шарил Ян в мутных водах, ничего интересного он более не сыскал.';
		else
			pn (string.match(myxml, "<ride1_skol>(.-)</ride1_skol>"));
			take ('skol');
			skol_taken = true;
		end;
	end,
};
galop = obj{
	nam = 'Понаблюдать за катанием',
	dsc = [[{Понаблюдать за катанием}]],
	act = function()
		if pony_drink == 1 then
			pn (string.match(myxml, "<pony_ride1>(.-)</pony_ride1>"));
		elseif pony_drink == 2 then
			pn (string.match(myxml, "<pony_ride2>(.-)</pony_ride2>"));
		elseif pony_drink == 3 then
			pn (string.match(myxml, "<pony_ride3>(.-)</pony_ride3>"));
		elseif pony_drink >= 3 then
			pn (string.match(myxml, "<pony_end>(.-)</pony_end>"));
			disable('pony');
			disable('galop');
			take('zippo');
		end;
	end;
};

skol = obj{
	nam = 'Сколопендра',
};
zippo = obj{
	nam = 'Зажигалка'
};
carrot = obj{
	nam = 'Морковка'
};
ride3 = room{
	nam ="Катание",
	enter = function()
		set_music('dogon.ogg');
		theme.gfx.bg('ride3.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	way = { 'index' },
	dsc = [[Манеж представлял собой круглую ограду из кривых и косых жердин, держащихся на честном слове и соплях. ]],
	obj = {
		'deer',
		'rush',
	};
};
deer = obj{
	nam ='олень',
	dsc = function()
		pn (string.match(myxml, "<ride_deer>(.-)</ride_deer>"))
	end,
	act = [[Голодный олень с несчастным видом стоит в упряжке.]],
	used = function(s,w)
		if w == carrot then
			pn (string.match(myxml, "<deer_feed>(.-)</deer_feed>"));
			deer_carrot = deer_carrot +1;
			inv():del('carrot');
			if deer_carrot == 42 then
				gam_end = secret;
				walk ('game_end');
			end;
		elseif w == adrenalin then
			pn (string.match(myxml, "<deer_boost>(.-)</deer_boost>"));
			deer_boost = true;
			inv():del('adrenalin');
		end;
	end,
};

rush = obj{
	nam = 'Понаблюдать за катанием.',
	dsc = [[{Понаблюдать за катанием}]],
	act = function()
		if deer_boost == true then
			pn (string.match(myxml, "<deer_rush>(.-)</deer_rush>"));
			deer_rush = true;
			disable('deer');
			disable('rush');
			take('stick');
		else
			pn (string.match(myxml, "<deer_ride>(.-)</deer_ride>"));
		end;
	end,
};

stick = obj{
	nam = 'Жердина',
};

secret = room{
	nam = 'секретная концовка',
}
empty_bottle = obj{
	nam = 'Пустая бутылка'
};
