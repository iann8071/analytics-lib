from config.base_config import BaseConfig


class SqlConfig(BaseConfig):

    def __init__(self):
        super().__init__()
        self.file = 'sql.ini'
