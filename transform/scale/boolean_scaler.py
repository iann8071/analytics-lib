import numpy as np


class BooleanScaler:

    def __init__(self, threshold):
        self.threshold = threshold

    def transform(self, data):
        return np.where(data <= self.threshold, 1, 0)
