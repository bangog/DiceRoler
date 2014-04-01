import MySQLdb
import random

class Roller:

    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost',user="root",passwd="dupa",db="diceapp")
        self.cursor = self.conn.cursor()


    def get_nick(self):
        self.nick = raw_input("Podaj nick")


    def roll (self, walls):
        self.cursor.execute("INSERT INTO dice VALUES ('%s',%d)" % (self.nick,random.randint(1,walls)))
        self.conn.commit()

    def show(self):
        for rec in self.cursor.fetchmany(2):
            print"Nick: %s\nWynik: %d\n" % (rec[0], rec[1])



x=Roller()
x.get_nick()
x.roll(10)
