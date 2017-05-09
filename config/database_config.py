from config.base_config import BaseConfig


class DatabaseConfig(BaseConfig):

    def __init__(self):
        super().__init__()
        self.file = 'database.ini'
