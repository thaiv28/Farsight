DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

rm $DIR/../data/db/stats.db
sqlite3 $DIR/../data/db/stats.db < sql/0_create_tables.sql

sqlite3 $DIR/../data/db/stats.db <<EOF
.import --csv --skip 1 $DIR/../data/preprocessed/player_db.csv playera
.import --csv --skip 1 $DIR/../data/preprocessed/match_stat_db.csv match_stat
.import --csv --skip 1 $DIR/../data/preprocessed/player_stat_db.csv player_stat
EOF

sqlite3 $DIR/../data/db/stats.db < sql/2_dataset_schema.sql

python3 nullify_columns.py
python3 build_dataset.py