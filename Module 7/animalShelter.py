#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:36:29 2024

@author: hoangkimvyngu_snhu
"""

from pymongo import MongoClient

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, USER, PASS):
        """Initialize MongoClient and connect to the database"""
        # Connection parameters
        # USER = 'aacuser'
        # PASS = 'snhu305'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30778
        DB = 'aac'
        COL = 'animals'
        
        # Initialize connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]
        print("Connection Sucessful")

    def create(self, data):
        """Insert a document into the collection"""
        if data:
            self.collection.insert_one(data)
            return True  # Return True if successful insert
        else:
            return False  # Return False if data is empty

    def read(self, query):
        """Query documents from the collection based on a key/value lookup pair"""
        cursor = self.collection.find(query)
        result = list(cursor)  # Convert cursor to list of documents
        return result
    
    def update(self, update_query, updated_data):
        """Update documents in the collection"""
        result = self.collection.update_many(update_query, {"$set": updated_data})
        return result.modified_count

    def delete(self, delete_query):
        """Delete document from the collection"""
        result = self.collection.delete_many(delete_query)
        return result.deleted_count