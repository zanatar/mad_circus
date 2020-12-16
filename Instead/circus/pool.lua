pool_enter = room{
	nam = 'Б',
	enter = function()
		if act3 == true and pool3_end == false then walk(pool3);
		else walk(pool1) end;
	end,
};
pool1 = room{
	nam = 'Бассейн',
	enter = function()
		set_music('teqila.ogg');
		theme.gfx.bg('pool.png');
		theme.win.color('white', 'yellow', 'red');
	end,
	way = {'index'},
	dsc = [[^^ ^^ Бассейн представлял собой приличных размеров яму, заполненную мутноватой водой. ]],
	obj = {
		'guard';
		'border'
		},
};

guard = obj{
	nam = 'Охранник',
	dsc = function(s)
		if here() == pool1 then
			pn'Вокруг никого не было, не считая {охранника}, сонно опершегося на ограждение. ';
		elseif here() == pool3 and deer_rush == false then
			pn (string.match(myxml, "<pool_guard2>(.-)</pool_guard2>"));
		elseif here() == pool3 and deer_rush == true then
			pn (string.match(myxml, "<pool_guard3>(.-)</pool_guard3>"));
		end;
	end,
	act = [[^^ ^^Охранник взглянул на Яна с неодобрением.]],
};

border = obj{
	nam ='край бассейна',
	dsc = [[{Подойти к краю бассейна}]],
	act = function()
		if here() == pool1 then
			pn (string.match(myxml, "<border1>(.-)</border1>"));
		elseif here() == pool3 and deer_rush == false then
			pn (string.match(myxml, "<border2>(.-)</border2>"));
		elseif here() == pool3 and deer_rush == true then
			pn '^^ ^^Ян подошел к бассейну. Охранник был так занят работой с санями, что не обратил на него ни малейшего внимания.';
			walk (swim);
		end;
	end,
};
pool3 = room{
	nam = 'Бассейн',
	enter = function()
		set_music('teqila.ogg');
		theme.gfx.bg('pool.png');
		theme.win.color('white', 'red', 'yellow');
	end,
	way = {'index'},
	dsc = function()
		pn'^^ ^^Бассейн представлял собой приличных размеров яму, заполненную мутноватой водой.';
		if pool_clean == false then
			pn (string.match(myxml, "<pool_mermaids>(.-)</pool_mermaids>"));
		elseif pool_clean == true and waves_calm == false then
			pn'По бассейну гуляют волны';
		end;
	end,
	obj = {
		'guard';
		'border'
		},
};

swim = room{
	nam = 'Бассейн: у воды',
	way = {'pool3'},
	dsc = [[Нет ничего лучше, чем освежиться в жаркий денек. И не важно, что вода нечиста - прохлада дороже!]],
	obj = {
		'mermaids';
		'waves:disable()';
		'swimm';
		'fishing:disable()';
		},
	exit = function() fishing_rod = 0 end,
};

mermaids = obj{
	nam = '"Русалки"',
	dsc = [[{"Девочки-русалки"} продолжают бултыхаться в бассейне.]],
	act = [[Из-за громкого плеска и визга "русалки" ничего не слышат.]],
	used = function(s,w)
		if w == mouse then
			s:disable();
			inv():del(w);
			enable('waves');
			pn (string.match(myxml, "<pool_clean>(.-)</pool_clean>"));
			pool_clean = true;
		end;
	end,
};
waves = obj{
	nam = 'Волны',
	dsc = [[По странному капризу стихии, физики отражения и предвзятости судьбы, {волны}, поднятые «русалками» все не затихали и не затихали.]],
	act = [[Увы, но Ян - не Посейдон, не Моисей и даже не Ксеркс...]],
	used = function(s,w)
		if w == barrel_full then
			s:disable();
			inv():del(w);
			pn (string.match(myxml, "<waves_calm>(.-)</waves_calm>"));
			waves_calm = true;
			take ('barrel');
		end;
	end,
};

swimm = obj{
	nam = 'Купание',
	dsc = [[{Искупаться}]],
	act = function(s)
		if pool_clean == false then
			pn (string.match(myxml, "<swim1>(.-)</swim1>"));
		elseif pool_clean == true and waves_calm == false then
			pn 'В волнах купаться опасно, можно и утонуть!';
		elseif waves_calm == true then
			pn (string.match(myxml, "<pool_swim>(.-)</pool_swim>"));
			s:disable();
			enable('fishing');
			swim.dsc = [[В пучинах вод скрывается ценная добыча!]];
			walk('pool3');
		end;
	end,
};


fishing = obj{
	nam = 'Рыбалка',
	dsc = [[Задача проста и ясна. Нужно {Поймать рыбу}!]],
	act = function()
		if fishing_rod == 0 then
			pn 'На что ловить то будем? Руками не вариант.';
		elseif fishing_rod == 1 then
			pn 'Оглушить рыбу палкой не получиться - вода слишком мутная.';
		elseif fishing_rod == 2 then
			pn 'Такой удочкой можно поймать рыбу, только если долго читать ей произведения Эдгара По. Возможно тогда она захочет свить из веревки петлю и повеситься. Ах, да, у рыб нет гортани.';
		elseif fishing_rod == 3 then
			pn ' Ян закинул удочку в воду и долго сидел у берега выжидая. Но рыба так и не клюнула. Может быть требуется что-то еще?';
		elseif fishing_rod == 4 then
			walk (trip);
		end;
	end,
	used = function(s,w)
		if w == stick and fishing_rod == 0 then
			pn 'Уперев припасенную жердину в ограду, Ян приготовился к сборке удочки. Удилище в наличие, нужно остальное';
			fishing_rod = 1;
		elseif w == rope and fishing_rod == 1 then
			pn 'Ян достал веревку и привязал ее к жердине.';
			fishing_rod = 2;
		elseif w == hook and fishing_rod == 2 then
			pn 'Ян достал крючок от колета пьяницы и привязал его веревке. Что-ж, удочка готова.';
			fishing_rod = 3;
		elseif w == penis and fishing_rod == 3 then
			pn 'Ян достал оторванный член и насадил его на крючок. Хоть на что-то он сгодится. Ну вот, для рыбалки все готово.';
			fishing_rod = 4;
		end;
	end,
};


trip = room{
	nam = 'Рыбалка удалась',
	enter = function()
		disable('leave');
		theme.win.color('white', 'yellow', 'violet');
	end,
	dsc = [['^^ ^^ ^^ ^^Ян закинул импровизированную удочку в мутные воды и принялся ждать.']],
	obj = {
		'fish';
		'fug:disable()';
		'eat:disable()';
		'trip1:disable()';
		'trip2:disable()';
		'trip3:disable()';
		'trip4:disable()';
		'trip5:disable()';
		'trip6:disable()';
		'leave:disable()';
		},
};

fish = obj{
	nam ='поймал',
	dsc = [[{Ловись рыбка большая и очень большая!}]],
	act = function(s)
		pn (string.match(myxml, "<fish_sucess>(.-)</fish_sucess>"));
		s:disable();
		enable('fug');
	end,
};


fug = obj{
	nam ='странная рыба',
	dsc = [[{Какая странная рыба..}]],
	act = function(s)
		pn (string.match(myxml, "<fish_fugu>(.-)</fish_fugu>"));
		s:disable();
		enable('eat');
		take('fugu');
	end,
};
eat = obj{
	nam ='еда',
	dsc = [[{Хм, впрочем неважно, жрать охота!}]],
	act = function(s)
		pn (string.match(myxml, "<fish_eat>(.-)</fish_eat>"));
		s:disable();
		enable('trip1');
		inv():del('fugu');
	end,
};

trip1 = obj{
	nam ='трип1',
	dsc = [[{Омномном!}]],
	act = function(s)
		set_music('trip.ogg');
		theme.gfx.bg('trip.png');
		pn (string.match(myxml, "<trip1>(.-)</trip1>"));
		s:disable();
		enable('trip2');
	end,
};

trip2 = obj{
	nam ='трип2',
	dsc = [[{Фто пваивфодит??!!}]],
	act = function(s)
		pn (string.match(myxml, "<trip2>(.-)</trip2>"));
		s:disable();
		enable('trip3');
	end,
};

trip3 = obj{
	nam ='трип3',
	dsc = [[{Пора валить!}]],
	act = function(s)
		pn (string.match(myxml, "<trip3>(.-)</trip3>"));
		s:disable();
		enable('trip4');
	end,
};

trip4 = obj{
	nam ='трип4',
	dsc = [[{SOS   ... --- ... SOS}]],
	act = function(s)
		pn (string.match(myxml, "<trip4>(.-)</trip4>"));
		s:disable();
		enable('trip5');
	end,
};

trip5 = obj{
	nam ='трип5',
	dsc = [[{NOOOOOOOOOOOOOOOOOOOOOO.....}]],
	act = function(s)
		pn (string.match(myxml, "<trip5>(.-)</trip5>"));
		s:disable();
		enable('trip6');
		inv():del('stick');
		inv():del('rope');
		inv():del('hook');
		inv():del('penis');
	end,
};

trip6 = obj{
	nam ='трип6',
	dsc = [[{Это нужно повторить!!!}]],
	act = function(s)
		pn (string.match(myxml, "<trip6>(.-)</trip6>"));
		s:disable();
		enable('leave');
		take('fugu');
		pool3_end = true;
	end,
};

fugu = obj{
	nam = 'Рыба фугу',
};

