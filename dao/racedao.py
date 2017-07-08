from config.base_config import BaseConfig
import pandas as pd
import pymysql
import os


class RaceDao:
    def __init__(self):
        self.config = BaseConfig().parse_config()
        self.db_con = pymysql.connect(
            host=self.config['database']['host'],
            user=self.config['database']['user'],
            password=self.config['database']['password'],
            db=self.config['database']['db_name'],
            charset=self.config['database']['charset']
        )

    def db_con(self):
        return self.db_con

    def read_data_as_pdf(self):
        return pd.read_sql(open(os.path.join(os.path.dirname(__file__), self.config['files']['read_data'])).read(), self.db_con)
