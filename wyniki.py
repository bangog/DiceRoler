import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user="root",
                     passwd="dupa",
                     db="diceapp")

wynik = db.cursor()

wynik.execute("SELECT * FROM dice")

for rec in wynik.fetchmany(2):
    print"Nick: %s\nWynik: %d\n" % (rec[0], rec[1])



