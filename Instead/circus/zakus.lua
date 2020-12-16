zak = room{
	--pic = 'zak.jpg',
	nam ='закусочная',
	way = { 'index' },
	enter = function()
		set_music('kozl.ogg')
		theme.gfx.bg('zak.png')
		theme.win.color('white', 'yellow', 'red');
	end,
	forcedsc = true,
	dsc = '^^ ^^Цирковое заведение общепита ужасно, но, судя по всему, вполне удовлетворяет местных работников и артистов.',
	obj = {
		'desk',
		'prod',
		'crate',
		'drunk',
		},
}

desk = obj {
	nam = 'прилавок',
	dsc = 'Коряво сколоченный из щелястых досок {прилавок} манит посетителей обилием тарелочек с заветревшимися кусками мяса непонятного происхождения, склизкими бутербродами, салатиками из нарванной с газона травы, и пирожками, которые вполне могла испечь бабуля Яна, почившая пятнадцать лет назад.',
	act = function(s)
		if seen 'prod' then
			p 'Прилавок находится под бдительным присмотром продавщицы. Стащить ничего не удасться...' ;
		elseif  not have (mouse) then
			pn (string.match(myxml, "<desk_mouse>(.-)</desk_mouse>"));
			take ('mouse');
		else
			pn'Ян подошел к прилавку. Увы, даже при более  тщательном осмотре ничего, к чему хотелось хотя бы прикоснуться, найдено не было.';
		end;
	end,
	used = function(s,w)
		if w == skol then
			disable('prod');
			inv():del(w);
			take ('knife');
			pn (string.match(myxml, "<desk_skol>(.-)</desk_skol"));
		end;
	end,
};
vodka = obj {
	nam = 'Бутылка водки',
	dsc = 'Бутылка паленой водки',
	inv = 'Эту дрянь я пить не буду!',
};


crate = obj {
	nam = 'ящик с водкой',
	dsc = 'Сбоку от прилавка стоит  {ящик с водкой}.',
	act = function(s)
		if seen 'prod' then
			pn 'Ян подошел к ящику с водкой. Дождавшись, пока очередная муха отвлекла продавщицу, он попытался украдкой стащить бутылку. ^^ - Руки убрал! - немедленно зарычала хозяйка прилавка, угрожающе взмахивая ножовкой. Ян решил не рисковать и ретировался.';
		elseif  not have (vodka) then
			take ('vodka');
			pn (string.match(myxml, "<crate_vodka>(.-)</crate_vodka>"));
		else
			pn'Тут и с одной бутылкой непонятно, что делать. Не то, что с двумя';
		end
	end,
};

drunk = obj {
	nam = 'пьяница',
	dsc = 'За одним из столиков примостился {пьяница}.',
	drunk_event = false,

	act = function()
		pn (string.match(myxml, "<drunk_start>(.-)</drunk_start>"));
	end;
	used = function(s, w)
		if w == vodka then
			inv():del('vodka');
			pn (string.match(myxml, "<drunk_vodka>(.-)</drunk_vodka>"));
		elseif w == purgen then
			inv():del('purgen');
			disable (s);
			drunk_event = true;
			pn (string.match(myxml, "<drunk_purgen>(.-)</drunk_purgen"));
		end;
	end,
	};

mouse = obj {
	nam = 'Дохлая мышь',
	inv = 'Исключительно ценный трофей',
};

prod = obj {
	nam = 'продавщица',
	dsc = function()
		pn (string.match(myxml, "<desk_start>(.-)</desk_start>"));
	end;
	act = [[Скосив на Яна глаза и моментально оценив платежеспособность клиента, продавщица недовольно хмыкнула и продолжила пялиться в пустоту.]],
};
knife = obj{
	nam = 'Ржавая ножовка',
};

