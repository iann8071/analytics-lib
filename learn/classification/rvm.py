# -*- coding: utf-8 -*-

from skrvm import RVC
import warnings;warnings.filterwarnings('ignore')
from utils.adapter import Adapter


class RVM:

    def __init__(self):
        self.predictor = None

    @classmethod
    def result_columns(self):
        return ['class1', 'class2']

    def train_and_predict(self, training_data_features, training_data_answers, data):
        self.train(training_data_features, training_data_answers)
        return self.predict(data)

    def predict(self, data):
        return self.predictor.predict_proba(Adapter.to_np(data))

    def train(self, training_data_features, training_data_answers):
        clf = RVC()
        self.predictor = clf.fit(training_data_features, training_data_answers)
