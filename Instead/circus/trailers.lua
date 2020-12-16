trailer = room{
	nam = 'Трейлеры персонала',
	forcedsc = true,
	enter = function()
		set_music('teqila.ogg');
		theme.gfx.bg('trailer.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	way = {'index'},
	dsc = function() pn (string.match(myxml, "<trailer_start>(.-)</trailer_start>"))	end;
	obj = {
		'check';
		'red_atlet:disable()';
		'red_doctor:disable()';
		'secret:disable()'
		},
};

check = obj{
	nam = 'Осмотр',
	dsc = [[{Осмотреть трейлеры}]],
	act = function()
		p '';
		if jong_end2 == false and not have ('kettlebell') then
			enable('red_atlet');
		elseif jong_end2 == true and doctor_check == false then
			enable('red_doctor');
		elseif have('key') then
			enable('secret');
		else pn'Сколько ни шатался Ян меж вагончиками - интересных или хотя-бы доступных объектов он найти не смог.';
		end;
	end,
};

red_atlet = obj{
	nam = 'трейлер1',
	dsc = [[Дверь {фургона}, покрашенного в красный цвет, была непредусмотрительно открыта.]],
	act = function()
		pn (string.match(myxml, "<trailer_kettlebell>(.-)</trailer_kettlebell>"));
		take('kettlebell');
		disable('red_atlet');
	end,
};

red_doctor = obj{
	nam = 'трейлер2';
	dsc = [[Около {фургона}, покрашенного в красный цвет, собралась толпа народу. Люди с интересом заглядывали внутрь через окна и двери.]],
	act = function() walk ('trailer_doctor') end,
};

secret = obj{
	nam = 'трейлер3',
	dsc = [[Потолкавшись возле трейлеров, Ян отыскал ту {дверь}, к которой подходил ключик.]],
	act = [[Дверь заперта. Как неожиданно!]],
	used = function(s,w)
		if w == key then
			s:disable();
			inv():del(w);
			walk('secret_trailer');
		end;
	end,
};

trailer_doctor = room{
	nam = 'Красный трейлер',
	enter = function()
		set_music('teqila.ogg');
		theme.gfx.bg('trailer_doctor.png');
		theme.win.color('white', 'yellow', 'blue');
	end,
	way = {'trailer'},
	dsc = function() pn (string.match(myxml, "<trailer_red>(.-)</trailer_red>"))	end;
	obj = {'doctor'},
};

doctor = obj{
	nam = 'доктор',
	dsc = function() pn (string.match(myxml, "<trailer_doctor>(.-)</trailer_doctor>"))	end;
	act = function() walk(doctor_dlg) end,
	used = function(s,w)
		if w == knife then
			disable('doctor');
			disable('red_doctor');
			inv():del(w);
			pn (string.match(myxml, "<trailer_oper>(.-)</trailer_oper>"));
			take ('adrenalin');
			doctor_check = true;
		end;
	end,
};

doctor_dlg = dlg{
	nam = 'разговор c доктором',
	title = [[Разговор c доктором]],
	enter = [[Ян всенепременно решил помочь доктору.]],
	phr = {
		{always = true,'Конем, ходи, конем - век воли не видать!' , 'Доктор всем своим видом дал понять, куда бы он ввел ферзя любителю шахмат' };
		{always = true, 'Цапу надо крутить' , 'Доктор с раздражением взглянул на поцака без цака'};
		{always = true, 'Семь раз отмерь, один раз отрежь.' , 'Доктор с энтузиазмом воспринял данное предложение. Жаль, скальпель для данной операции не подойдет'};
		{always = true, 'Кантуй по малу' , 'Доктор не проявил интереса к потенциальному грузчику'};
		{always = true, 'Господа, позвольте я пробью с ноги!' , 'Господа, возможно, позволили бы. Но доктор верен клятве Гиппократа!'};
		{always = true, 'Прекратить подавать ценные советы' , 'Доктор с облегчением вздохнул', [[back()]]};
		},
};

secret_trailer = room{
	nam = 'Закрытый трейлер',
	enter = function()
		set_music('teqila.ogg');
		theme.gfx.bg('trailer_secret.png');
		theme.win.color('white', 'yellow', 'red');
	end,
	dsc = function() pn (string.match(myxml, "<trailer_secret>(.-)</trailer_secret>"))	end;
	obj = {
		'box_of_zoo';
		'box_of_chemistry';
		'box_of_physics';
		},
};





adrenalin = obj{
	nam = 'Шприц с адреналином',
};

kettlebell = obj{
	nam = 'Гиря',
};

box_of_chemistry = obj{
	nam = 'Набор "Юный химик"',
	dsc = [[{Набор "Юный химик"}]],
	tak = function()
		pn (string.match(myxml, "<trailer_choice>(.-)</trailer_choice>"));
		take('box_of_chemistry');
		disable('secret');
		walk(trailer);
	end,
};
box_of_zoo = obj{
	nam = 'Набор "Юный зоотехник"',
	dsc = [[{Набор "Юный зоотехник"}]],
	tak = function()
		take('box_of_zoo');
		pn (string.match(myxml, "<trailer_choice>(.-)</trailer_choice>"));
		disable('secret');
		walk(trailer);
	end,
};
box_of_physics = obj{
	nam = 'Набор "Юный физик"',
	dsc = [[{Набор "Юный физик"}]],
	tak = function()
		take('box_of_physics');
		pn (string.match(myxml, "<trailer_choice>(.-)</trailer_choice>"));
		disable('secret');
		walk(trailer);
	end,
};

