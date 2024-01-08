import os
from zipfile import ZipFile 
import shutil
from server.db import conn as db

def save_db_dump(byte_file):
    clean_dir_exist("data")
    save_zip_file(byte_file)
    upzip_db()
    create_sql_db()


def save_zip_file(byte_file):
    os.makedirs("data", exist_ok=True)
    with open("data/raw_dump.zip", "wb") as binary_file:
   
        # Write bytes to file
        binary_file.write(byte_file)

def upzip_db(file_loc= "data/raw_dump.zip"):
    # loading the temp.zip and creating a zip object 
    with ZipFile(file_loc, 'r') as zObject: 
    
        # Extracting all the members of the zip  
        # into a specific location. 
        zObject.extractall(path="data") 

def clean_dir_exist(loc):
    if os.path.exists(loc) and os.path.isdir(loc):
        shutil.rmtree(loc)

def create_sql_db():
    file_name = "data/db8sqnszgozxhp.sql"

    create_db_infile_sqlite(file_name)
    pass

def create_db_infile_sqlite(create_filename):
    with open(create_filename, 'r') as sql_file:
        sql_script = sql_file.read()

        cursor = db.cursor()
        cursor.executescript(sql_script)
        db.commit()

def create_db_inmemory_sqlite(create_fn):
    pass




