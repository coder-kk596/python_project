import pymysql


class mySqlHelper:
    '''def __init__(self,databaseName=None):
        self.db = pymysql.connect(host='localhost', user='root', password='admin', port=3306)
        self.cursor =self.db.cursor()
        self.cursor.execute('SELECT VERSION()')
        data = self.cursor.fetchone()
        print('Database Version:', data)
        self.cursor.execute("CREATE DATABASE "+databaseName+" DEFAULT CHARACTER SET utf8")
'''

    def createTable(self):
        db = pymysql.connect(host='localhost', user='root', password='L5201314', port=3306,db='spiders')
        cursor=db.cursor()
        #sql="CREATE TABLE IF NOT EXISTS student(id VARCHAR(255) NOT NULL, u_name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))"
        sql='CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL)'
        cursor.execute(sql)

    def insert(self,item):
        db = pymysql.connect(host='localhost', user='root', password='L5201314', port=3306, db='spiders')
        cursor = db.cursor()
        data={
            'id':'001',
            'name':'lkk',
            'age':'22'
        }
        table='student'
        keys=','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)

        # print(i["directors"])
        directors = ",".join(item["directors"])
        casts = ",".join(item["casts"])

        data1 = {
            'directors': directors,
            'rate': item["rate"],
            'cover_x': item['cover_x'],
            'star': item['star'],
            'title': item['title'],
            'url': item['url'],
            'casts': casts,
            'cover': item['cover'],
            'id': item['id'],
            'cover_y': item['cover_y']
        }
        print(data1)

        try:
            table = 'doubanMoviesAll'
            keys = ','.join(data1.keys())
            values = ','.join(['%s'] * len(data1))
            sql1 = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
            cursor.execute(sql1, tuple(data1.values()))
            db.commit()
        except:
            print('Failed')
            db.rollback()
        db.close()


    def findMovies(self):
        db = pymysql.connect(host='localhost', user='root', password='L5201314', port=3306, db='spiders')
        cursor = db.cursor()
        sql="SELECT * from doubanMoviesAll"
        cursor.execute(sql)
        re=cursor.fetchall()
        return re


    def findMovie(self,title):
        db = pymysql.connect(host='localhost', user='root', password='L5201314', port=3306, db='spiders')
        cursor = db.cursor()
        sql="SELECT title from doubanMoviesAll where title='"+title+"'"
        cursor.execute(sql)
        re=cursor.fetchall()
        return re





def main():
    db=mySqlHelper()
    db.findMovie_none()
    print(db.findMovie('lkk'))
    #db.insert()

if __name__== '__main__':
    main()