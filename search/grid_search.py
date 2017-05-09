import itertools
from learn.classification.svm import SVM
from utils.mrange import MRange


class GridSearch:

    def __init__(self):
        pass

    @classmethod
    def svm(cls, validator, features, answer, data, print_score, executor):
        hyper_parameter_data = [item for item in itertools.product(
            MRange.create(config['svm']['c_from'], config['svm']['c_to'], config['svm']['c_diff']),
            MRange.create(config['svm']['gamma_from'], config['svm']['gamma_to'], config['svm']['gamma_diff'])
        )]
        executor.execute(lambda c_gamma: validator.execute(SVM(c_gamma[0], c_gamma[1]), features, answer, data, print_score), hyper_parameter_data)
