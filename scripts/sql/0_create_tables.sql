create table player (
	player_key text primary key
	constraint valid_player_key check (player_key like ('oe:player:%'))
);
go;

create table player_alias (
	id serial primary key,
	alias text not null,
	player_key references player(player_key)
);
go;

create table team (
	team_key text primary key
	constraint valid_team_key check (team_key like ('oe:team:%'))
);
go;

create table match_stat (
	match_key text primary key,
	url text not null,
	year int not null,
	playoffs bool not null,
	date timestamp not null,
	game int not null,
	patch real not null,
	side text
	constraint check_side check (side in ('Blue', 'Red')),
	teamname text not null,
	length int not null,
	result bool not null,
	inhibitors int not null,
	opp_inhibitors int not null,
	gold_spent_percent_difference numeric (3, 10) not null,
	gold_percent_rating numeric (3, 10) not null
);
go;

create table player_stat (
	player_stat_key text primary key
	constraint valid_player_stat_key check (player_stat_key like ('%\_\b(10|[1-9])\b%')),
	match_key text references match_stat(match_key),
	player_key text references player(player_key),
	position text not null
	constraint check_position check (position in ('top', 'jng', 'mid', 'bot', 'sup')),
	kills int not null,
	deaths int not null,
	assists int not null,
	teamkills int not null,
	teamdeaths int not null,
	doublekills int not null,
	triplekills int not null,
	quadrakills int not null,
	pentakills int not null,
	first_blood bool not null,
	first_blood_kill bool not null,
	first_blood_assist bool not null
	constraint check_first_blood check (first_blood = false or first_blood_kill != first_blood_assist),
	dmg_to_champs int not null,
	dmg_per_min numeric(10, 10) not null,
	dmg_share numeric(3, 10) not null,
	dmg_taken_per_min numeric (10, 10) not null,
	dmg_mitigated_per_min numeric (10, 10) not null,
	wards_placed int not null,
	wards_per_min numeric (3, 10) not null,
	control_wards_bought int not null,
	vision_score int not null,
	vision_score_per_min numeric (3, 10) not null,
	total_gold int not null,
	earned_gold int not null,
	earned_gold_per_min numeric (10, 10) not null,
	earned_gold_share numeric (3, 10) not null,
	gold_spent int not null,
	total_cs int not null,
	cs_per_min numeric (5, 10) not null,
	gold_at_10 int not null,
	xp_at_10 int not null,
	cs_at_10 int not null,
	opp_gold_at_10 int not null,
	opp_xp_at_10 int not null,
	opp_cs_at_10 int not null,
	gold_diff_at_10 int not null,
	xp_diff_at_10 int not null,
	cs_diff_at_10 int not null,
	kills_at_10 int not null,
	assists_at_10 int not null,
	deaths_at_10 int not null,
	opp_kills_at_10 int not null,
	opp_assists_at_10 int not null,
	opp_deaths_at_10 int not null,
	gold_at_15 int not null,
	xp_at_15 int not null,
	cs_at_15 int not null,
	opp_gold_at_15 int not null,
	opp_xp_at_15 int not null,
	opp_cs_at_15 int not null,
	gold_diff_at_15 int not null,
	xp_diff_at_15 int not null,
	cs_diff_at_15 int not null,
	kills_at_15 int not null,
	assists_at_15 int not null,
	deaths_at_15 int not null,
	opp_kills_at_15 int not null,
	opp_assists_at_15 int not null,
	opp_deaths_at_15 int not null,
	gold_at_20 int not null,
	xp_at_20 int not null,
	cs_at_20 int not null,
	opp_gold_at_20 int not null,
	opp_xp_at_20 int not null,
	opp_cs_at_20 int not null,
	gold_diff_at_20 int not null,
	xp_diff_at_20 int not null,
	cs_diff_at_20 int not null,
	kills_at_20 int not null,
	assists_at_20 int not null,
	deaths_at_20 int not null,
	opp_kills_at_20 int not null,
	opp_assists_at_20 int not null,
	opp_deaths_at_20 int not null,
	gold_at_25 int not null,
	xp_at_25 int not null,
	cs_at_25 int not null,
	opp_gold_at_25 int not null,
	opp_xp_at_25 int not null,
	opp_cs_at_25 int not null,
	gold_diff_at_25 int not null,
	xp_diff_at_25 int not null,
	cs_diff_at_25 int not null,
	kills_at_25 int not null,
	assists_at_25 int not null,
	deaths_at_25 int not null,
	opp_kills_at_25 int not null,
	opp_assists_at_25 int not null,
	opp_deaths_at_25 int not null
)
