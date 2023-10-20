#################################################
#	Filename: database_connect.py
#	Author: Ovidiu
#	Date: 2023-10-19
#################################################
# Include Libs
import sqlite3
import os

def db_con():
	dir = os.path.dirname(__file__)
	database_connection = sqlite3.connect(os.path.join(dir, 'database_application.db'))
	return database_connection