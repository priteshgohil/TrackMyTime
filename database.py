import sqlite3
from constants import DATABASE_FILE
class Database:
    def __init__(self):
        self.conn=sqlite3.connect(DATABASE_FILE)
        self.conn.execute("CREATE TABLE IF NOT EXISTS stats(day TEXT PRIMARY KEY, active INTEGER,idle INTEGER,locked INTEGER)")
        self.conn.commit()
    def save_day(self,day,a,i,l):
        self.conn.execute("INSERT OR REPLACE INTO stats VALUES(?,?,?,?)",(day,a,i,l)); self.conn.commit()
    def get_recent(self,limit=31):
        return self.conn.execute("SELECT * FROM stats ORDER BY day DESC LIMIT ?",(limit,)).fetchall()
    def close(self): self.conn.close()
