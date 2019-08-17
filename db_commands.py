import sqlite3


class Database:

    def __init__(self, dbname='chatlog.sqlite'):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = 'CREATE TABLE IF NOT EXISTS msglog (messages text)'
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text):
        stmt = 'INSERT INTO msglog (messages) VALUES (?)'
        args = (item_text,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = 'DELETE FROM msglog WHERE messages = (?)'
        args = (item_text,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        stmt = 'SELECT messages FROM msglog'
        return [x[0] for x in self.conn.execute(stmt)]