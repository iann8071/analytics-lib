# -*- coding: utf-8 -*-

import numpy as np
from sklearn import svm
import warnings;warnings.filterwarnings('ignore')
from utils.adapter import Adapter


class SVM:

    def __init__(self, c, gamma):
        self.c = c
        self.gamma = gamma
        self.predictor = None

    def predict(self, data):
        return self.predictor.predict(Adapter.to_np(data))

    def hyper_parameters(self):
        return {
            'c': self.c,
            'gamma': self.gamma
        }

    def train(self, training_data_features, training_data_answers):
        self.predictor = svm.SVC(C=self.c, gamma=self.gamma).fit(training_data_features, training_data_answers)