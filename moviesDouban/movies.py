import logging
import random
import string
import requests
import time
from collections import deque
from urllib import parse

from settings import User_Agents
from mongoHelper import MongoDBHelper
from mysqlHelper import mySqlHelper



class moviesSpider(object):
    def __init__(self):
        self.base_url='https://movie.douban.com/j/new_search_subjects?'
        self.full_url=self.base_url+'{query_params}'
        self.headers={'User-Agent':random.choice(User_Agents)}
        self.form_tag=None #电影 电视剧 综艺等
        self.type_tag=None #剧情 喜剧 爱情等
        self.area_tag=None  #中国大陆 美国 香港等
        self.year_tag=None #年代
        self.feat_tag=None #经典 青春 文艺等特色
        self.sort='U'
        self.range=0, 10
        self.playable=''
        self.unwatched=''
        #连接数据库
        self.db=MongoDBHelper('moviesdouban')
        self.db1=mySqlHelper()

    def get_query_parameter(self):
        self.form_tag=input("请输入你想看的影视形式（电影｜电视剧｜综艺）")
        self.type_tag=input("请输入你想看的类型（剧情｜喜剧｜动作）")
        self.area_tag = input("请输入你想看的地区（中国大陆｜美国｜香港）")
        self.year_tag = input("请输入你想看的类型（2019｜2018｜2010年代）")
        self.feat_tag = input("请输入你想看的特色（经典｜文艺｜搞笑）")


    def get_default_parameter(self):
        self.range=input('请输入评分范围［0-10］：')
        self.sort=input('请输入排序顺序（近期热门：，标记最多：T，评分最高：，最新上映：R）：')
        self.playable=input('请选择是否可播放（默认不可播放）：')
        self.unwatched=input('请选择是否是看过的（默认为没看过）：')



    def encode_query_data(self):

        all_tags = [self.form_tag, self.type_tag, self.area_tag, self.year_tag, self.feat_tag]
        query_param = {
            'sort': self.sort,
            'range': self.range,
            'tags': all_tags,
            'playable': self.playable,
            'unwatched': self.unwatched,

        }
        query_params=parse.urlencode(query_param, safe=string.printable) #printable表示ASCII字符就不用编码了
        invalid_chars=['(', ')', '[', ']', '+', '\'']
        for char in invalid_chars:
            if char in query_params:
                query_params=query_params.replace(char,'')
        self.full_url = self.full_url.format(query_params=query_params) + '&start={start}'


    def movies_download(self,offset):
        full_url=self.full_url.format(start=offset)
        print(full_url)
        resp=None
        try:
            resp=requests.get(full_url,headers=self.headers)
        except Exception as e:
            logging.error(e)
        return resp


    def get_movies(self,resp):
        if resp:
            if resp.status_code==200:
                movies=dict(resp.json()).get('data')
                if movies:
                    print(movies)
                    return movies
                else:
                    return None
        else:
            return None


    def save_movies(self,movies,id):
        if not movies:
            print('save_movies() error:movies为None!!!!')
            return
        all_movies=self.find_movies()
        if len(all_movies) == 0:
            for movie in movies:
                id += 1
                movie['_id'] = id
                self.db.insert_item(movie)
                print(movie)
        else:
            titles = []
            for existed_movie in all_movies:
                titles.append(existed_movie.get('title'))
                #print(titles)

            for movie in movies:
                if movie.get('title') not in titles:
                    id += 1
                    movie['_id'] = id
                    self.db.insert_item(movie)
                    print(id)
                    print(movie)
                else:
                    print('save_movies():该电影"{}"已经在数据库了！！！'.format(movie.get('title')))


    def save_1(self,movies):

        if not movies:
            print('save_movies() error:movies为None!!!!')
            return
        all_movies=self.findMovies()

        if len(all_movies) == 0:
            for movie in movies:
                self.db1.insert(movie)


        else:
            titles = []
            for existed_movie in all_movies:
                titles.append(existed_movie[5])
                #print(titles)


            for movie in movies:
                if movie.get('title') not in titles:
                    #id += 1
                    #movie['_id'] = id
                    self.db1.insert(movie)
                    print(movie)
                else:
                    print('save_movies():该电影"{}"已经在数据库了！！！'.format(movie.get('title')))






    def find_movies(self):
        all_movies = deque()
        data = self.db.find_item()
        for item in data:
            all_movies.append(item)
        return all_movies

    def findMovies(self):
        all_movies = deque()
        data = self.db1.findMovies()
        for item in data:
            all_movies.append(item)
        return all_movies

    def findMovie(self,title):
        all_movies = deque()
        data = self.db1.findMovie(title)
        for item in data:
            all_movies.append(item)
        return all_movies



def main():
    spider=moviesSpider()
    spider.get_query_parameter()
    ret=input('是否需要设置排序方式，评分范围（Y/N)：')
    if ret.lower()=='y':
        spider.get_default_parameter()
    spider.encode_query_data()
    id=offset=0
    while True:
        reps = spider.movies_download(offset)
        movies = spider.get_movies(reps)
        #spider.save_movies(movies, id)
        spider.save_1(movies)
        offset += 20
        id = offset
        time.sleep(5)

if __name__ == '__main__':
    main()






