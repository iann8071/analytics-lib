# -*- coding: utf-8 -*-

import numpy as np
from sklearn import svm
import warnings;warnings.filterwarnings('ignore')
from utils.adapter import Adapter


class SVM:

    def __init__(self):
        self.c = None
        self.gamma = None
        self.predictor = None

    def predict(self, data):
        return self.predictor.predict(Adapter.to_np(data))

    def set_hyper_parameters(self, hyper_parameter_value):
        self.c = hyper_parameter_value['c']
        self.gamma = hyper_parameter_value['gamma']
        return self

    def hyper_parameters(self):
        return {
            'c': self.c,
            'gamma': self.gamma
        }

    def train(self, training_data_features, training_data_answers):
        self.predictor = svm.SVC(C=self.c, gamma=self.gamma).fit(training_data_features, training_data_answers)