"""
Recurse directorys and create a cached db of data to update.
A seperate log will need to be created for the databasing


2022-06-07: Matthew Wells
"""
import os
import sys
import dbm
sys.path.insert(0, os.getcwd()) # bring in db config
from data.DBConfig import DBConfig 


class DirectoryChecks:
    """
    Recurse through a directory specified in a config file. All files should have same root directory
    """

    def __init__(self) -> None:
        self.directory_check = DBConfig.RecursePath
        self.db_path = FileDBOperator()
        with open(self.db_path.db_path, "w") as db: # open db in sync mode so all writes are provided
            self.recurse_directory()
    
    def recurse_directory(self):
        """
        Recurse through directories and determine if a path has been seen before
        """
        for par, dirs, file in os.walk(self.directory_check):
            for fi in file:
                print(os.path.isfile(os.path.join(par, fi)))

class FileDBOperator:
    """
    Create and maintain a database of file information for information to be added when ready
    """
    db_name = "testing_daemondb.db"
    def __init__(self) -> None:
        self.db_path = self.check_if_db_exists()

    
    def check_if_db_exists(self):
        """
        Deterine weather or not a database exists
        """
        db_path = os.path.join(DBConfig.DBStorage, self.db_name)
        if not os.path.isfile(db_path):
            new_db = dbm.open(db_path, 'c') # intialize a db
            new_db.close()
        return db_path

if __name__=="__main__":
    DirectoryChecks()