from pymongo import MongoClient
from .business import BusinessHandler
from .businessstructure import BusinessStructureHandlerMongoDb


class DatabaseLayer:
    
    def __init__(self):
        self.client = MongoClient()
        self.mongodb = self.client.proddb

    def new_business_handler(self):
        return BusinessHandler(self.mongodb.business)


    def new_businessstructure_handler(self):
        return BusinessStructureHandlerMongoDb(self.mongodb.business)
