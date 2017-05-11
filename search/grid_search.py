import itertools
from learn.classification.svm import SVM
from utils.mrange import MRange


class GridSearch:

    def __init__(self):
        pass

    def execute(cls, executor, validator, learner, hyper_parameter_values, data, features, answer, print_score):
        hyper_parameter_data = [dict(zip(hyper_parameter_values.keys(), value)) for value in
            [*itertools.product(*[MRange.create(hyper_parameter_values[key]['from'],hyper_parameter_values[key]['to'],hyper_parameter_values[key]['unit'])
            for key in hyper_parameter_values.keys()])]]
        print(hyper_parameter_data)
        executor.execute(lambda hyper_parameter_value: validator.execute(learner.set_hyper_parameters(hyper_parameter_value), features, answer, data, print_score), hyper_parameter_data)
