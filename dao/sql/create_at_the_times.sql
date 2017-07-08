create table player_at_the_time (
	heldy varchar(4),
	heldm varchar(4),
	raceno varchar(2),
	jockeyname text,
	sosu int(11),
	win decimal(10,5),
	rentai decimal(10,5),
	fukusyo decimal(10,5)
);

create table uma_at_the_time (
	heldy varchar(4),
	heldm varchar(4),
	kettono varchar(11),
	sosu int(11),
	win decimal(10,5),
	rentai decimal(10,5),
	fukusyo decimal(10,5)
);

create table teacher_at_the_time (
	heldy varchar(4),
	heldm varchar(4),
	racecoursecd varchar(2),
	raceno varchar(2),
	trainername text,
	sosu int(11),
	win decimal(10,5),
	rentai decimal(10,5),
	fukusyo decimal(10,5)
);