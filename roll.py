import MySQLdb
import random

db = MySQLdb.connect(host='localhost',
                     user="root",
                     passwd="dupa",
                     db="diceapp")
c= db.cursor()
nick = raw_input("Podaj NICK: ")
ster = 1
while(ster==1):
    liczba = random.randint(1,10)
    c.execute("INSERT INTO dice VALUES ('%s',%d)" % (nick, liczba))
    db.commit()
    ster=raw_input("1 - to do again")
