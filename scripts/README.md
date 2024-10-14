# Farsight Script Usage

This README will provide a description of the one-time scripts (and the data they were used on)
to create and transform the dataset. All scripts are located in the `/scripts/`
directory.

### Merge CSV
- File: `merge_csv.py`
- Usage: Merges the raw data (originally split by year) into a single CSV file
- Input: CSV files split by year in `/data/raw/` directory
- Output: `complete_raw_data.csv` in `/data/raw/` directory

### Prepare CSV
- File: `prepare_csv.py`
- Usage: Converts the master CSV into separate CSVs representing a table in the
database: player, player_stat, match_stat
- Input: `complete_raw_data.csv` in `/data/raw/` directory
- Output: CSV files in `/data/preprocessed/` directory

## Create/Build Database
The following files create and build an SQLite3 database stored in `/data/db/`.
The `runner.sh` script will create the database, then automatically run all of 
the following scripts.

### Create tables (SQL)
- File: `sql/0_create_tables.sql`
- Usage: Generates schema for database tables

### Copy CSV (SQL)
- File: `sql/1_copy_csv.sql`
- Usage: Copies the data from the CSV files to the database

### Dataset Schema (SQL)
- File: `sql/2_dataset_schema.sql`
- Usage: Generates schema for dataset table in database

### Nullify Columns
- File: `nullify_columns.py`
- Usage: Converts empty values in database (a result of empty CSV cells) to NULL values

### Build Dataset
- File: `build_dataset.py`
- Usage: Builds the dataset by querying the database for historical player averages

