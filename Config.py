import os


class Config:
    # DB_USER = os.getenv('DB_USER')
    # DB_PASSWORD = os.getenv('DB_PASSWORD')
    # DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
