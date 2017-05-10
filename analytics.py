class Analytics:

    def __init__(self):
        pass

    @classmethod
    def start(cls, search, executor, validator, learner, hyper_parameter_values, data, features, answer, print_score):
        search.execute(executor, validator, learner, hyper_parameter_values, data, features, answer, print_score)