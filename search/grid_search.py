import itertools
from learn.classification.svm import SVM
from utils.mrange import MRange


class GridSearch:

    def __init__(self):
        pass

    def execute(cls, executor, validator, learner, hyper_parameter_values, data, features, answer, print_score):
        hyper_parameter_data = zip(hyper_parameter_values.keys(),
            zip(*[MRange.create(*(hyper_parameter_values[key].values())) for key in hyper_parameter_values.keys()])
        )
        executor.execute(lambda hyper_parameter_value: validator.execute(learner(hyper_parameter_value), features, answer, data, print_score), hyper_parameter_data)
