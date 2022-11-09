from mongoengine import *

import os

database_host = os.getenv("DATABASE_HOST")
database_port = int(os.getenv("DATABASE_PORT"))
database_db_name = os.getenv("DATABASE_DBNAME")

connect(
    host=database_host,
    port=database_port,
    db=database_db_name,
)
