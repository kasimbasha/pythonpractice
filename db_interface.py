#author : Kasim
import sqlite3
"""
DB CURD operation API file,
Create Table
Run SQL from table with commit and without commit
print records
"""
class db_interface:
    def __init__(self,**kwargs):
        self._filename = kwargs.get('filename')
        self._table = kwargs.get('table','')
    def set_table(self,table):
        self._table = table
    @property
    def _filename(self):
        return self._dbfilename
    @_filename.setter
    def _filename(self,fn):
        self._dbfilename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row
    @_filename.deleter
    def _filename(self):
        self.close()
    def close(self):
        self._db.close()
        del self._dbfilename
    def sql_do(self,qury,params=()):
        self._db.execute(qury,params)
        self._db.commit()
    def sql_do_nocommit(self,qury,params=()):
        self._db.execute(qury,params)
    def sql_query(self,qury,params=()):
        c = self._db.execute(qury,params)
        for r in c :
            yield r
    def sql_query_row(self,qury,params=()):
        c = self._db.execute(qury,params)
        c.fetchone()
    def sql_query_value(self,qury,params=()):
        c = self._db.execute(qury,params)
        c.fetchone()[0]
    def commit(self):
        self._db.commit()

    def getrecord(self,id):
        q = f"select * from {self._table} where id= ?"
        c = self._db.execute(q,(id,))
        return c.fetchone()
    def getrecords(self):
        q = f'select * from {self._table}'
        c = self._db.execute(q)
        for r in c:
            yield r
    
    def insert_nocommit(self,recs):
        klist = sorted(recs.keys())
        vlist = [recs[v] for v in klist]
        values = ','.join('?' * len(vlist))
        params = ','.join(klist)
        q = f'insert into {self._table} ({params}) values ({values})'
        c = self._db.execute(q,vlist)
        return c.lastrowid
    
    def insert(self,rec):
        lastrowid =  self.insert_nocommit(rec)
        self._db.commit()
        return lastrowid
    def update_nocommit(self, id, rec):
        klist = sorted(rec.keys())
        values = [rec[v] for v in klist]
        for i, k in enumerate(klist):
            if k == 'id':
                del klist[i]
                del values[i]
        setValues = ',  '.join(map(lambda s: '{} = ?'.format(s), klist))
        q = f'UPDATE {self._table} SET {setValues} WHERE id = ?'
        self._db.execute(q, values + [id])
    def update(self,id,rec):
        self.update_nocommit(id, rec)
        self._db.commit()
    def delete_nocommit(self,id):
        query = f'DELETE FROM {self._table} WHERE id = ?'
        self._db.execute(query, [id])
    def delete(self, id):
        self.delete_nocommit(id)
        self._db.commit() 
    def countrecs(self):
        query = f'SELECT COUNT(*) FROM {self._table}'
        c = self._db.execute(query)
        return c.fetchone()[0]
    
def curd():
    fn = ':memory:'  # in-memory database
    t = 'foo'

    recs = [
        dict(string='one', number=42),
        dict(string='two', number=73),
        dict(string='three', number=123)
    ]

    # -- for file-based database
    # try: os.stat(fn)
    # except: pass
    # else: 
    #     print('Delete', fn)
    #     os.unlink(fn)

    print(f'Create database file {fn} ...', end='')
    db = db_interface(filename=fn, table=t)
    print('Done.')

    print('Create table ... ', end='')
    db.sql_do(f' DROP TABLE IF EXISTS {t} ')
    db.sql_do(f' CREATE TABLE {t} ( id INTEGER PRIMARY KEY, string TEXT, number INTEGER ) ')
    print('Done.')

    print('Insert into table ... ', end='')
    for r in recs:
        db.insert(r)
    print('Done.')

    print(f'There are {db.countrecs()} rows')

    print('Read from table')
    for r in db.getrecords():
        print(dict(r))

    print('Update table')
    db.update(2, dict(string='TWO'))
    print(dict(db.getrecord(2)))

    print('Insert an extra row ... ', end='')
    newid = db.insert({'string': 'extra', 'number': 512})
    print(f'(id is {newid})')
    print(dict(db.getrecord(newid)))
    print(f'There are {db.countrecs()} rows')
    print('Now delete it')
    db.delete(newid)
    print(f'There are {db.countrecs()} rows')
    for r in db.getrecords():
        print(dict(r))
    for r in db.sql_query(f"select * from {t}"):
        print(r)
    db.close()

if __name__ == "__main__": curd()
    