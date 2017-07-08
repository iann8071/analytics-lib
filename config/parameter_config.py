import configparser as parser
import os

from config.base_config import BaseConfig


class ParameterConfig(BaseConfig):
    def __init__(self):
        self.file = 'hyper_parameter.ini'
