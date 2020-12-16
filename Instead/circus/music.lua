stage = room{
	nam = 'Сцена музыкантов',
	enter = function()
		if act3 == true then
			walkin(stage3)
		else
			walkin(stage1)
		end;
	end,
};

stage1 = room{
	nam = 'Сцена музыкантов',
	forcedsc = true,
	enter = function()
		if stage1_end == true then
			pn 'Музыкальная сцена опустела, лишь ветер гоняет по ней пыль и обрывки бумаги. Делать там пока совсем нечего.';
			walk('index');
		else
			set_music('teqila.ogg');
			theme.gfx.bg('music1.png');
			theme.win.color('white', 'yellow', 'red');
		end;
	end,
	way = {'index'},
	dsc = function() pn (string.match(myxml, "<stage1_start>(.-)</stage1_start>"))	end;
	obj = {'horner'};
};

horner = obj{
	nam = 'Дудочник',
	dsc = function() pn (string.match(myxml, "<stage1_horner>(.-)</stage1_horner>"))	end;
	act = [[Боже, как он достал!]],
	used = function(s,w)
		if w == carrot then
			walk(stage1_win)
			inv():del(w);
		end;
	end,
}
stage1_win = room{
	nam ='Модификация инструмента',
	dsc = function() pn (string.match(myxml, "<stage1_stuck>(.-)</stage1_stuck>"))	end;
	obj = {
		'wait';
		'leave:disable()';
		};
};
wait = obj{
	nam = 'Ждать',
	dsc = [[{Подождать}]],
	act = function(s)
		pn (string.match(myxml, "<stage1_end>(.-)</stage1_end>"));
		take ('horn');
		enable ('leave');
		disable(s);
		stage1_end = true;
	end,
};

horn = obj{
	nam = 'Обломок рога',
};
leave = obj{
	nam = 'Уйти',
	dsc = [[{Уйти}]],
	act = function() walk('index') end;
};

stage3 = room{
	nam = 'Сцена музыкантов',
	way = {'index'},
	dsc = function() pn (string.match(myxml, "<stage3_start>(.-)</stage3_start>"))	end;
	enter = function()
		if stage3_end == true then
			pn (string.match(myxml, "<stage3_end>(.-)</stage3_end>"));
			walk('index');
		else
		set_music('teqila.ogg');
		theme.gfx.bg('music3.png');
		theme.win.color('white', 'yellow', 'red');
		end;
	end,
	obj = {
		'singer';
		'listen';
		};
};

singer = obj{
	nam = 'Пьяница - кастрат',
	dsc = function() pn (string.match(myxml, "<stage3_drunk>(.-)</stage3_drunk>"))	end;
	act = function()
		if stage_listen == true then
			if romeo_listen == true then
				pn 'Ян попросил исполнить арию Ромео на бис. Пьяница был не против.';
				walk(romeo)
			else
				walkin (request)
			end;
		else
			pn 'Пьяница готовится к исполнению арии и ни на что не реагирует'
		end;
	end,
	used = function(s,w)
		if stage_listen == true then
			if w == vodka or w == purgen then
				pn (w.nam, string.match(myxml, "<stage3_vodka>(.-)</stage3_vodka>"));
				inv():del(w);
				if not have (empty_bottle) then
					take ('empty_bottle');
				end;
			end;
		else
			pn 'Пьяница готовится к исполнению арии и ни на что не реагирует'
		end;
	end,
};

listen = obj{
	nam = 'Слушать музыку',
	dsc = [[{Послушать музыку}]],
	act = function() walkin('euredica_start') end,
};

euredica_start = room{
	nam = 'Эвредика',
	dsc = function() pn(string.match(myxml, "<stage3_eu_start>(.-)</stage3_eu_start>")) end,
	obj = {vway("next", "{Наслаждаться музыкой}.", 'euredica')},
}
euredica = room{
	nam = 'Эвредика',
	dsc = img('euredica.png'),
	entered = function()
        save_music();
        set_music('e.mp3');
		theme.gfx.bg('euredica2.png');
    end;
    left = restore_music;
	obj = {'out'}
};

out = obj{
	nam = 'Стоп',
	dsc = [[{Перестать слушать музыку}]],
	act = function()
		pn (string.match(myxml, "<stage3_eu_end>(.-)</stage3_eu_end>"));
		stage_listen = true;
		walk(stage3);
	end,
};

request = dlg{
	nam = 'Заказ песни',
	enter = function()
		pn (string.match(myxml, "<stage3_request_start>(.-)</stage3_request_start>"));
		pjump '0';
	end;
	phr = {
		{tag = '0'},
		{always = true,'Эээ, песня про зайцев!', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Маэстро, урежте марш!', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Non più compagni: andate', 'Пьяница взглянул на Яна с удивлением, услышав что-то отдаленно знакомое. Нужно продолжать', [[pjump '1']]};
		{always = true,'Спой, светик, не стыдись!', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Я требую продолжения банкета!', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{tag = '1'},
		{always = true,'Хоп хоп, мусорок, не шей мне срок!', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Розовые розы Светке Соколовой', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Das ist der Pariser Tango Monsieur', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Solo restar desio, meco non bramo', 'Интерес усилился. Нужно продолжать.', [[pjump '2']]};
		{always = true,'Союз нерушимый республик свободных', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{tag = '2'},
		{always = true,'Потерял я Эвридику', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Che il mio dolor crudel: mi dà conforto', 'Да, эта вещь определенно ему знакома. Но нужна конкретика.', [[pjump '3']]};
		{always = true,'Из за острова на стрежень', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Куда, куда, куда вы удалились?', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Der Hölle Rache kocht in meinem Herzen', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{tag = '3'},
		{always = true,'Solo il barbaro affanno:', 'Пьяница почти уловил мелодию и буквально умоляет взором о последней строке', [[pjump'4']]};
		{always = true,'Casta diva', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Être ou ne pas être', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Vive la Résistance', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Aut Caesar, aut nihil.', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{tag = '4'},
		{always = true,'Lascia ch`io pianga', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Ogni altro oggetto a me divien tiranno', 'Наконец-то уловив желаемое, пьяница махнул шарманщику. Кивнув, тот щелкнул парой переключателей на шарманке и начал крутить ручку. Полилась прекрасная симфоническая музыка, под аккомпанемент которой пьяница запел что-то на незнакомом Яну языке. Однако, вскоре, перед глазами Яна словно загорелись строки.', [[walkin(romeo)]]};
		{always = true,'Ridi, Pagliaccio, sul tuo amore infranto!', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'Dove andrò senza il mio ben?', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
		{always = true,'La donna è mobile', 'Пьяница разочарованно поморщился, не сумев уловить знакомые слова', [[back()]]};
	},
};

romeo = room{
	nam = 'Ария Ромео',
	entered = function()
        save_music();
        set_music('r.ogg');
		theme.gfx.bg('euredica2.png');
    end;
    left = restore_music;
	dsc = img('romeo2.png'),
	obj = {
		'flask';
		'out2';
		},
};
flask = obj{
	nam = 'Место для яда',
	dsc = [[^(Cava un'ampolla, e beve il veleno.)	^(Достает {флакон} и выпивает яд.)]],
	used = function(s,w)
		if w == purgen then
			pn (string.match(myxml, "<stage3_win>(.-)</stage3_win>"));
			inv():del(w);
			take('hook');
			stage3_end = true;
			walk('index');
		end;
	end,
};

out2 = obj{
	nam = 'Дождаться окончания арии',
	dsc = [[{^^Дождаться окончания арии}]],
	act = function()
		pn (string.match(myxml, "<stage3_romeo_end>(.-)</stage3_romeo_end>"));
		romeo_listen = true;
		walk(stage3);
	end,
};

hook = obj{
	nam = 'Крючок',
};


