import pathlib
import sqlite3

def connect():
    file_dir = pathlib.Path(__file__).parent.resolve() 
    con = sqlite3.connect(file_dir / "../data/db/stats.db")	
    cur = con.cursor()	
 
    return con, cur

