from pymongo import MongoClient
class MongoDBHelper:
    def __init__(self,collection_name=None):
        self._client = MongoClient('localhost',27017)
        self._test = self._client['test']
        self._name=self._test[collection_name]

    def insert_item(self,item):
        self._name.insert_one(item)

    def find_item(self):
        data=self._name.find()
        return data

def main():
    mongo=MongoDBHelper('collection')
    mongo.insert_item({'a':1})

if __name__== '__main__':
    main()