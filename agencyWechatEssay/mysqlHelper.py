import pymysql

class mySqlHelper:
    def insert(self,item):
        db=pymysql.connect(host='localhost', user='root', password='L5201314', port=3306,db='spiders')
        cursor=db.cursor()
        table='wechatEssays'

        data={
            'title':item['title'],
            'txt_info':item['txt_info'],
            'account':item['account'],
            'url':item['url']
        }

        try:
            keys=','.join(data.keys())
            values=','.join(['%s']*len(data))
            sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
            cursor.execute(sql,tuple(data.values()))
            db.commit()
        except:
            print('fail')
            db.rollback()
        db.close()

