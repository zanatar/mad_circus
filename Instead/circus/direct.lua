index = room{
	nam = 'Указатель',
	enter = function()
		theme.gfx.bg('direct.png');
		theme.win.color('white', '#46f7f9', 'red');
	end,
	dsc = [[Недалеко от входа в цирк стоит указатель. Ян подошел к нему и принялся внимательно его изучать]],
	obj = {
		'w_circus';
		'w_zak';
		'w_toilets';
		'e_slon';
		'e_rider';
		'e_pool';
		'n_zver';
		'n_jong';
		's_music';
		's_shoot';
		's_trailers';
		'anounser';
		},
};

w_circus = obj{
	nam = 'в шатер',
	dsc = [[Основной достопримечательностью западной части цирка является {большой шатер}.]],
	act = function() walk('tent') end,
};

w_zak = obj{
	nam = 'В закусочную',
	dsc = [[По правую сторону от него манит изголодавшихся путников местная {закусочная}.]],
	act = function() walk('zak') end,
};

w_toilets = obj{
	nam = 'В туалеты',
	dsc = [[Невдалеке от нее весьма кстати располагается {туалет}.]],
	act = function() walk('toilet') end,
};

e_slon = obj{
	nam = 'В слонярню',
	dsc = [[^^На востоке виднеется огромный загон с надписью {«Слонярня»}.]],
	act = function() walk('stable') end,
};

e_rider = obj{
	nam = 'В манеж',
	dsc = [[Неподалеку от него находится {манеж}.]],
	act = function() walk('ride') end,
};

e_pool = obj{
	nam = 'В бассейн',
	dsc = [[Ближе к ограде вырыта большая яма, заполненная водой – {бассейн} для водных выступлений.]],
	act = function()
	if pool3_end == true then pn 'Охранник наверняка запомнил нарушителя. Не стоит туда ходить, ох не стоит!';
	else walk('pool_enter') end;
	end,
};

n_zver = obj{
	nam = 'В зверинец',
	dsc = [[^^ В северной части цирка источает специфические звуки и запахи {зверинец}.]],
	act = function() walk('zoo') end,
};

n_jong = obj{
	nam = 'к площадке жонглеров',
	dsc = [[Ближе к центру расположилась {площадка для жонглеров} и акробатов.]],
	act = function() walk('jongler') end,
};

s_music = obj{
	nam = 'К площадке музыкантов',
	dsc = [[^^На юге находится {площадка музыкантов}.]],
	act = function() walk('stage') end,
};

s_shoot = obj{
	nam = 'в тир',
	dsc = [[Несколько правее стоит несколько палаток, объединённых общей вывеской {«Тир»}.]],
	act = function() walk('tir') end,
};
s_trailers = obj{
	nam = 'К трейлерам персонала',
	dsc = [[У ограды притулились {трейлеры персонала}.]],
	act = function() walk('trailer') end,
};

anounser = obj{
	nam = 'анонс',
	dsc = function()
		pn '^^Рядом с указателем стоит корявая доска.';
		if circus_act1_end == false then pn'К доске приколота мятая бумажка с надписью: "Внеманее! Ф шатре выступаит Клоун Чпок!"';
		elseif circus_act1_end == true and jong_end2 == false then pn 'К доске приколота мятая бумажка с надписью: "Жанглер пришел"';
		elseif act3 == true and circus_final == false then pn 'К доске приколоты 2 клочка бумаги: "Спишити видеть уни кальных русалак в бассейни!" и "Раждественскее катанея в манежи!"';
		elseif circus_final == true then pn 'К доске приколот кусок старой афиши. все буквы истерты, разобрать можно только слова "бальшой шатер" и "ис пушке на"';
		end;
	end,
};
