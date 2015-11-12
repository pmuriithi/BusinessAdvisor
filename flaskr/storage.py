
import pymongo
from pymongo import MongoClient
import json 
import sys
import urllib

def main():
    """ Connect to MongoDB """
    """client = pymongo.MongoClient("mongodb://bb0e13f4-e2b2-4c92-bf54-9ef30beae791:b7dec6e9-5fc0-4e3e-8456-598ad501fe1a@159.8.128.67:10247/db")"""
    client = pymongo.MongoClient('localhost', 27017)
    print ("Connected successfully")
    print (client) 

    db = client.test_database
    
    collection = db['test-collection']

    input_file = open('temp_files/MOCK_DATA_User.json', encoding='utf-8')
    
    for line in input_file:
    	collection.insert_many(json.loads(line))
    print ("Data inserted")
        
if __name__ == "__main__": main()