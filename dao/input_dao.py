import pandas as pd
import pymysql
from config.database_config import DatabaseConfig
from config.sql_config import SqlConfig


class InputDao:

    def __init__(self):
        self.db_config = DatabaseConfig().parse_config()
        self.sql_config = SqlConfig().parse_config()
        self.db_con = pymysql.connect(
            host=self.db_config['database']['host'],
            user=self.db_config['database']['user'],
            password=self.db_config['database']['password'],
            db=self.db_config['database']['db_name'],
            charset=self.db_config['database']['charset']
        )

    def db_con(self):
        return self.db_con

    def read_data_as_pdf(self):
        return pd.read_sql(open(self.sql_config['sqls']['read_data']).read(), self.db_con)
