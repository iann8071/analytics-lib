import configparser as parser
import os
import zipfile


class BaseConfig:

    config_dir = 'config'
    ini_dir = 'ini'
    lib_zip = 'analytics-lib.zip'

    def __init__(self):
        self.file = 'config.ini'
        self.config = None

    def parse_config(self):
        config = parser.ConfigParser()
        _zip = zipfile.ZipFile(self.lib_zip)
        zip_config = _zip.open(os.path.join(self.config_dir, self.ini_dir, self.file), "rU")
        zip_config_data = zip_config.read().decode('ascii')
        config.read_string(zip_config_data)
        return config

    def __getitem__(self, item):
        return getattr(self, item)

