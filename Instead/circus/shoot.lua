tir = room {
	nam ='Тир',
	enter = function()
		set_music('teqila.ogg');
		theme.gfx.bg('shoot.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	way = {'index'},
	dsc = function() pn (string.match(myxml, "<tir_start>(.-)</tir_start>"))	end;
	obj = {
		'krot';
		vway('continue' , '{«Интерактивное метание»}.' , 'int_met');
		'dynamite_crate:disable()';
		},
};

krot = obj{
	nam = 'Взорви крота',
	dsc = [[Лишь два заведения его заинтересовали: {«Взорви крота!»} и ]],
	act = function(s)
		enable('dynamite_crate');
		disable(s);
		pn (string.match(myxml, "<tir_krot>(.-)</tir_krot>"));
	end,
};

dynamite_crate = obj{
	nam = 'Ящик с динамитом',
	dsc = '{Украсть динамит}',
	act = function()
		if tir_win == true then
			if not have (dynamite) then
				pn (string.match(myxml, "<tir_dyn_take>(.-)</tir_dyn_take>"));
				take ('dynamite');
			else
				pn'«Переноска двух и более кусков взрывчатки чреваты риском взаимной детонации!» - подумал Ян и убоялся брать больше.';
			end;
		else
			pn (string.match(myxml, "<tir_dyn_fail>(.-)</tir_dyn_fail>"));
		end;
	end,
};

int_met = room{
	nam = 'Интерактивное метание',
	way = {'tir'},
	enter = function()
		if tir_win == true then
			pn 'С выходом клоуна из строя, площадка «Интерактивное метание» потеряла всякую интерактивность. Больше там делать нечего.';
			walk (tir);
		end;
	end,
	dsc = [[ Площадка «Интерактивное метание» работала, в отличие от соседнего «Взорви крота!».]],
	obj = {
		'clown';
		},
};
clown = obj{
	nam = 'Клоун',
	dsc = function() pn (string.match(myxml, "<tir_clown>(.-)</tir_clown>"))	end,
	act = function()
		if clown_drunk == true then
			pn (string.match(myxml, "<tir_hit_ball>(.-)</tir_hit_ball>"));
		else
			pn (string.match(myxml, "<tir_miss_ball>(.-)</tir_miss_ball>"));
		end;
	end,
	used = function(s,w)
		if w == vodka then
			pn (string.match(myxml, "<tir_clown_drunk>(.-)</tir_clown_drunk>"));
			clown_drunk = true;
			inv():del(w);
			if not have (empty_bottle) then
				take ('empty_bottle');
				pn 'Оставшуюся пустую бутылку хозяйственный Ян прибрал.';
			else
				pn'Как ни любил Ян сбор стеклотары, но одной бутылки ему пока было достаточно'
			end;
		elseif w == egg then
			if clown_drunk == true then
				pn (string.match(myxml, "<tir_hit_egg>(.-)</tir_hit_egg>"));
				inv():del(w);
				take ('barrel');
				tir_win = true;
				walk (tir);
			else
				pn (string.match(myxml, "<tir_miss_egg>(.-)</tir_miss_egg>"));
			end;
		end;
	end,
};

barrel = obj{
	nam = 'Пустой бочонок',
};

dynamite = obj{
	nam = 'Шашечка динамита',
};









