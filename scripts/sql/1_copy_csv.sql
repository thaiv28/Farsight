SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

.import --csv --skip 1 $SCRIPT_DIR/../../data/preprocessed/player_db.csv player
.import --csv --skip 1 $SCRIPT_DIR/../../data/preprocessed/match_stat_db.csv match_stat
.import --csv --skip 1 $SCRIPT_DIR/../../data/preprocessed/player_stat_db.csv player_stat