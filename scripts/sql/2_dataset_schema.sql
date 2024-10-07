create table dataset (
	dataset_id int primary key,
	match_key text references match_stat(match_key),
	position text not null
	constraint check_position check (position in ('top', 'jng', 'mid', 'bot', 'sup')),
	date text not null,
	target_kills int,
	player_avg_result real,
	player_avg_length real,
	player_avg_gold_spent_percent_difference real,
	player_avg_gold_percent_rating real,
	player_avg_kills real,
	player_avg_deaths real,
	player_avg_assists real,
	player_avg_dmg_to_champs real,
	player_avg_dmg_per_min real,
	player_avg_dmg_share real,
	player_avg_dmg_taken_per_min real,
	player_avg_wards_per_min real,
	player_avg_vision_score_per_min real,
	player_avg_earned_gold_per_min real,
	player_avg_earned_gold_share real,
	player_avg_cs_per_min real,
	player_avg_gold_at_10 real,
	player_avg_xp_at_10 real,
	player_avg_cs_at_10 real,
	player_avg_opp_gold_at_10 real,
	player_avg_opp_xp_at_10 real,
	player_avg_opp_cs_at_10 real,
	player_avg_gold_diff_at_10 real,
	player_avg_xp_diff_at_10 real,
	player_avg_cs_diff_at_10 real,
	player_avg_kills_at_10 real,
	player_avg_assists_at_10 real,
	player_avg_deaths_at_10 real,
	player_avg_opp_kills_at_10 real,
	player_avg_opp_assists_at_10 real,
	player_avg_opp_deaths_at_10 real,
	player_avg_gold_at_15 real,
	player_avg_xp_at_15 real,
	player_avg_cs_at_15 real,
	player_avg_opp_gold_at_15 real,
	player_avg_opp_xp_at_15 real,
	player_avg_opp_cs_at_15 real,
	player_avg_gold_diff_at_15 real,
	player_avg_xp_diff_at_15 real,
	player_avg_cs_diff_at_15 real,
	player_avg_kills_at_15 real,
	player_avg_assists_at_15 real,
	player_avg_deaths_at_15 real,
	player_avg_opp_kills_at_15 real,
	player_avg_opp_assists_at_15 real,
	player_avg_opp_deaths_at_15 real,
	player_avg_gold_at_20 real,
	player_avg_xp_at_20 real,
	player_avg_cs_at_20 real,
	player_avg_opp_gold_at_20 real,
	player_avg_opp_xp_at_20 real,
	player_avg_opp_cs_at_20 real,
	player_avg_gold_diff_at_20 real,
	player_avg_xp_diff_at_20 real,
	player_avg_cs_diff_at_20 real,
	player_avg_kills_at_20 real,
	player_avg_assists_at_20 real,
	player_avg_deaths_at_20 real,
	player_avg_opp_kills_at_20 real,
	player_avg_opp_assists_at_20 real,
	player_avg_opp_deaths_at_20 real,
	player_avg_gold_at_25 real,
	player_avg_xp_at_25 real,
	player_avg_cs_at_25 real,
	player_avg_opp_gold_at_25 real,
	player_avg_opp_xp_at_25 real,
	player_avg_opp_cs_at_25 real,
	player_avg_gold_diff_at_25 real,
	player_avg_xp_diff_at_25 real,
	player_avg_cs_diff_at_25 real,
	player_avg_kills_at_25 real,
	player_avg_assists_at_25 real,
	player_avg_deaths_at_25 real,
	player_avg_opp_kills_at_25 real,
	player_avg_opp_assists_at_25 real,
	player_avg_opp_deaths_at_25 real,
	opp_avg_result real,
	opp_avg_length real,
	opp_avg_gold_spent_percent_difference real,
	opp_avg_gold_percent_rating real,
	opp_avg_kills real,
	opp_avg_deaths real,
	opp_avg_assists real,
	opp_avg_dmg_to_champs real,
	opp_avg_dmg_per_min real,
	opp_avg_dmg_share real,
	opp_avg_dmg_taken_per_min real,
	opp_avg_wards_per_min real,
	opp_avg_vision_score_per_min real,
	opp_avg_earned_gold_per_min real,
	opp_avg_earned_gold_share real,
	opp_avg_cs_per_min real,
	opp_avg_gold_at_10 real,
	opp_avg_xp_at_10 real,
	opp_avg_cs_at_10 real,
	opp_avg_opp_gold_at_10 real,
	opp_avg_opp_xp_at_10 real,
	opp_avg_opp_cs_at_10 real,
	opp_avg_gold_diff_at_10 real,
	opp_avg_xp_diff_at_10 real,
	opp_avg_cs_diff_at_10 real,
	opp_avg_kills_at_10 real,
	opp_avg_assists_at_10 real,
	opp_avg_deaths_at_10 real,
	opp_avg_opp_kills_at_10 real,
	opp_avg_opp_assists_at_10 real,
	opp_avg_opp_deaths_at_10 real,
	opp_avg_gold_at_15 real,
	opp_avg_xp_at_15 real,
	opp_avg_cs_at_15 real,
	opp_avg_opp_gold_at_15 real,
	opp_avg_opp_xp_at_15 real,
	opp_avg_opp_cs_at_15 real,
	opp_avg_gold_diff_at_15 real,
	opp_avg_xp_diff_at_15 real,
	opp_avg_cs_diff_at_15 real,
	opp_avg_kills_at_15 real,
	opp_avg_assists_at_15 real,
	opp_avg_deaths_at_15 real,
	opp_avg_opp_kills_at_15 real,
	opp_avg_opp_assists_at_15 real,
	opp_avg_opp_deaths_at_15 real,
	opp_avg_gold_at_20 real,
	opp_avg_xp_at_20 real,
	opp_avg_cs_at_20 real,
	opp_avg_opp_gold_at_20 real,
	opp_avg_opp_xp_at_20 real,
	opp_avg_opp_cs_at_20 real,
	opp_avg_gold_diff_at_20 real,
	opp_avg_xp_diff_at_20 real,
	opp_avg_cs_diff_at_20 real,
	opp_avg_kills_at_20 real,
	opp_avg_assists_at_20 real,
	opp_avg_deaths_at_20 real,
	opp_avg_opp_kills_at_20 real,
	opp_avg_opp_assists_at_20 real,
	opp_avg_opp_deaths_at_20 real,
	opp_avg_gold_at_25 real,
	opp_avg_xp_at_25 real,
	opp_avg_cs_at_25 real,
	opp_avg_opp_gold_at_25 real,
	opp_avg_opp_xp_at_25 real,
	opp_avg_opp_cs_at_25 real,
	opp_avg_gold_diff_at_25 real,
	opp_avg_xp_diff_at_25 real,
	opp_avg_cs_diff_at_25 real,
	opp_avg_kills_at_25 real,
	opp_avg_assists_at_25 real,
	opp_avg_deaths_at_25 real,
	opp_avg_opp_kills_at_25 real,
	opp_avg_opp_assists_at_25 real,
	opp_avg_opp_deaths_at_25 real
);