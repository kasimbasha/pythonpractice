#author : Kasim
import sqlite3

def main() :
    print("connect")
    db = sqlite3.connect('db-api.db')
    cr = db.cursor()
    print('create')
    cr.execute('drop table if exists kasim_test')
    cr.execute(' create table kasim_test (id INTEGER PRIMARY KEY, string TEXT, number INTEGER)')
    print('insert row')
    cr.execute("insert into kasim_test(string,number) values ('one',1)")
    print('insert row')
    cr.execute("insert into kasim_test(string,number) values ('two',2)")
    print('insert row')
    cr.execute("insert into kasim_test(string,number) values ('three',3)")
    print('commite')
    db.commit()
    print('count')
    cr.execute('select * from kasim_test')
    c = cr.fetchone()[0]
    print(f' they are [c] rows in table')
    print('read')
    for r in cr.execute('select * from kasim_test') :
        print(r)
    print('drop')
    cr.execute("drop table kasim_test")
    print('close')
    db.close()

if __name__ == "__main__": main()

