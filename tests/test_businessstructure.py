
import sys
sys.path.append('../')

import serious.webapp.businessstructure as businessstructure
import pickle

import serious.webapp.databaselayer as db

DatabaseLayer = db.DatabaseLayer
from pymongo import MongoClient


def test_thetest():
    assert True

testdb = MongoClient()['serious-test-db']
testcol = testdb['test-businessstructure']


handler = businessstructure.BusinessStructureHandlerMongoDb(testcol)

def test_load_empty():
    assert handler.data == {}
    
        
