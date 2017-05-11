import pymysql
from config.database_config import DatabaseConfig
from config.sql_config import SqlConfig


class OutputDao:

    table_name = 'outputs'

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

    def init_table(self, columns):
        with self.db_con.cursor() as cursor:
            sql = "create table {outputs} ({columns})".format(
                outputs=self.table_name,
                columns=",".join([" ".join([key, columns[key]]) for key in columns.keys()])
            )
            result = cursor.execute(sql)
            self.db_con.commit()

    def write_data(self, value):
        with self.db_con.cursor() as cursor:
            sql = "INSERT INTO {table_name} ({keys}) VALUES ({values})".format(
                table_name=self.table_name,
                keys=','.join(value.keys()),
                values = ','.join([str(_value) for _value in value.values()])
            )
            result = cursor.execute(sql)
            self.db_con.commit()

