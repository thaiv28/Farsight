import sqlite3

import farsight.db.connection as connection

def main():
    con, cur = connection.connect()
    
    cur.execute("PRAGMA table_info(player_stat);")
    columns = [info[1] for info in cur.fetchall()]

    update_query = "UPDATE player_stat SET " + ", ".join([f"{col} = NULLIF({col}, '')" for col in columns])
    cur.execute(update_query)

    con.commit()
    con.close()
    
if __name__ == "__main__":
    main()