import MySQLdb
import logging
from .vector import Vector

class DBConnector:

    def __init__(host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.connected = False

    def __enter__(self):
        try:
            self.conn = MySQLdb.connect(self.host, self.user, self.passwd, self.db)
        except MySQLdb.Error:
            logging.error('Unable to connect to mysql database')
            return None
        
        try:
            self.cur = self.conn.cursor()
        except MySQLdb.Error:
            logging.error('Unable to get database cursor')
            self.conn.close()
            return None
        else:
            self.connected = True
            return self

    def __exit__(self, exec_type, exec_inst, exec_tb):
        if exec_type == MySQLdb.Error:
            logging.error('Unable to get wind component rows')
        self.cur.close()
        self.conn.close()
        self.connected = False

    @property
    def vectors(self, query):
        if not self.connected:
            raise RuntimeError('Not connected to database')
        self.cur.execute(query)
        num_rows = self.cur.rowcount
        for i in range(num_rows):
            yield Vector(cur.fetchone())

        
