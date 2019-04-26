import pymysql


class mysqlHelper:


    def insert(self,item):
        db=pymysql.connect(host='localhost', user='root', password='L5201314', port=3306, db='spiders')
        print(db)
        cursor=db.cursor()
        table='house'

        data={
            'title':item['title'],
            'address':item['address'],
            'price':item['price'],
            'url':item['url'],
        }

        '''try:
            
        except:
            print('fail')
            db.rollback()'''

        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        print(keys)
        print(values)
        print(data.values())

        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        cursor.execute(sql, tuple(data.values()))

        db.commit()
        db.close()


    def find(self):
        db=pymysql.connect(host='localhost', user='root', password='L5201314', port=3306, db='spiders')
        cursor=db.cursor()
        sql1='SELECT * FROM house'
        cursor.execute(sql1)
        re=cursor.fetchall()
        return re
















