import pickle

class Analytics:

    def __init__(self):
        pass

    @classmethod
    def start(cls, search, executor, validator, learner, hyper_parameter_values, data, features, answer, print_score):
        search.execute(executor, validator, learner, hyper_parameter_values, data, features, answer, print_score)

    @classmethod
    def start(cls, executor, validator, learner, data, features, answer, print_score):
        # executor.execute(
        #     lambda hyper_parameter_value: validator.execute(learner(hyper_parameter_value), features, answer, data,
        #                                                     print_score), hyper_parameter_data)
        pass

    @classmethod
    def save_predictor(cls, executor, learner, features, answer, data):
        executor.execute(
            lambda value: learner.train_and_save_predictor(data.loc[:, features], data.loc[:, answer]), ['dummy'])

