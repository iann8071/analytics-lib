# -* coding: utf-8 -*-

from skrvm import RVC
import warnings;warnings.filterwarnings('ignore')
from utils.adapter import Adapter
import pickle


class RVM:

    def __init__(self):
        self.predictor = None

    @classmethod
    def result_columns(self):
        return ['class1', 'class2']

    def predict(self, data):
        return self.predictor.predict_proba(Adapter.to_np(data))

    def train(self, training_data_features, training_data_answers):
        clf = RVC(coef1=1/1024)
        self.predictor = clf.fit(training_data_features, training_data_answers)

    def train_and_save_predictor(self, training_data_features, training_data_answers):
        self.train(training_data_features, training_data_answers)
        self.save_predictor()

    def save_predictor(self):
        with open('learner.dump', mode='wb') as f:
            pickle.dump(self.predictor, f)

    def __getitem__(self, item):
        return getattr(self, item)
