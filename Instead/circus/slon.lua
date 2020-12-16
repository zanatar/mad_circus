stable = room{
	nam = 'Слонярня',
	enter = function()
		set_music('dogon.ogg');
		if seen 'slon' then
			theme.gfx.bg('slon1.png');
		else theme.gfx.bg('slon2.png') end;
		theme.win.color('white', 'yellow', 'blue');
	end,
	forcedsc = true,
	way = { 'index' },
	dsc = [[^^ ^^ ^^ ^^Ян с интересом осмотрел добротно построенный (по сравнению с остальными зданиями) вольер.]],
	obj = {
		'slon',
		'ass',
		'kon',
		'purgen_barrel',
		'carrot_crate',
	};
};
kon = obj{
	nam = 'Конюх',
	dsc = function() pn (string.match(myxml, "<slon_kon>(.-)</slon_kon>"))	end,
	act = function() walkin 'kondlg' end,
};

kondlg = dlg{
	nam = 'разговор',
	title = [[Разговор с конюхом]],
	enter = [[Конюх не против поболтать, в отличие от слона]],
	phr = {
		{tag = '0','Звать тебя как?', '- Овдоким',[[pon '1']]};
		{false, tag = '1' , 'А это что за чудо?' , '- Слон, не видишь что ль. Жипкой кличут.', [[pon '2']]};
		{false, tag = '2', 'А почему это у слона такая большая… задница?' , '- Порода такая, стало быть. Elephas maximus podex.', [[pon '3']]};
		{false, tag = '3', 'И чего он тут делает?' , '- К выступлению готовится, стал быть. Вона, накормим и на арену, публику поражать.', [[pon '4']]};
		{false, tag = '4', 'Чем поражать?' , '- Увидишь, хе-хе.', [[pon '5']]};
		{false, tag = '5', 'А пурген зачем?' , '- Энто помощь ему важнейшая на спектакле. Старенький Жипка, самому тяжело под себя ходить. Вот пургенчиком и пользуем.'};
		{always = true, 'Ну покеда' , '- Иди ужо.', [[pon '0'; poff '1'; poff '2'; poff '3'; poff '4'; poff '5';back()]]};
	},
};
slon = obj{
	nam = 'слон',
	dsc = [[Лениво помахивая обвисшими ушами, в стойле стоял небольшой, довольно старый {слон} ]],
	act = [[Слон вяло пожирает сечку, не обращая ни на что внимания]],
	used = function(s,w)
		if w == carrot then pn'Ян достал морковку и ткнул ею морду слона. Жипка ненадолго отвлекся, ухватил морковку хоботом, засунул ее себе в пасть и продолжил кормиться.';
		inv():del(w);
		end;
	end,

};
dynamite = obj{
	nam = 'Шашечка динамита',
};
ass = obj{
	nam = 'зад',
	dsc = [[ с непропорционально огромным {задом}.]],
	act = [['Ян подошел к заднице слона. Впечатляюще огромная, она нависала над ним, словно отвесный утес, суровая и  непоколебимая. Внутри Яна все сильнее нарастало желание сделать с ней  что-нибудь эдакое.]],
	used = function(s,w)
		if w == carrot or w == vodka or w == purgen or w == empty_bottle then
			pn (w.nam,' с легкостью проникла в слоновью задницу и затерялась там, судя по всему, не доставив слону никакого дискомфорта.');
			inv():del(w);
		elseif w == dynamite then
			pn (w.nam,' с легкостью проникла в слоновью задницу и затерялась там, судя по всему, не доставив слону никакого дискомфорта.');
			slon_armed = true;
			inv():del(w);
		elseif w == zippo and slon_armed == true then
			pn (string.match(myxml, "<slon_boom>(.-)</slon_boom>"));
			slon_armed = false;
		elseif w == salo then
			pn 'Шматок свиного жира с легкостью проник в слоновью задницу, параллельно от души ее смазав.';
			slon_lubed = true;
			inv():del(w);
		elseif w == globus then
			if slon_lubed == true then
				inv():del(w);
				act2 = true;
				walk 'slon_end';
			else
				pn (string.match(myxml, "<slon_globus>(.-)</slon_globus>"));
			end;
		end;
	end,
};

slon_end = room{
	nam = 'Успех все ближе',
	enter = function()
		disable('kon');
		disable('ass');
		disable('slon');
	end,
	dsc = function() pn (string.match(myxml, "<slon_win>(.-)</slon_win>"))	end,
	obj = {vway('continue' , '{^Немедленно отправиться в цирк}' , 'tent')},
};

carrot_crate = obj{
	nam ='Ящик с морковкой',
	dsc = [[Из стоящего в стороне {ящика} призывно торчала морковка.]],
	act = function()
		if not have (carrot) then
				take ('carrot');
				pn 'Ян подошел к ящику с морковкой и стащил оттуда одну. Увлеченный кормлением слона конюх ничего не заметил.';
			else
				pn'Тут и с одной то морковкой непонятно, что делать. Куда уж с двумя.'
			end;
	end,
};
purgen_barrel = obj{
	nam = 'Бочонок с пургеном',
	dsc = [[Вдоль открытого стойла стояли разнообразные ящики и бочки. На одном {бочонке} было желтой краской выведено «ПургенЪ».]],
	act = [[Ян подошел к бочке с пургеном. Данная субстанция вполне может пригодиться, но в чем ее переносить? Не в горстях же.]],
	used = function(s,w)
		if w == empty_bottle then
			if not have (purgen) then
				take ('purgen');
				inv():del(w);
				pn'Ян подошел к бочке с пургеном. Стараясь не запачкать руку, наполнил пустую бутылку и завинтил крышку. Водка «Особая» готова к употреблению.';
			else
				pn'Так как в ближайшее время Ян не планировал открывать аптеку, одной бутылки Пургена ему хватит'
			end;
		end;
	end,
};
purgen = obj {
	nam = 'Бутылка пургена',
	inv = 'эту дрянь я пить не буду!',
};

