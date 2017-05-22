class Analytics:

    def __init__(self):
        pass

    @classmethod
    def start(cls, search, executor, validator, learner, hyper_parameter_values, data, features, answer, write_score):
        search.execute(executor, validator, learner, hyper_parameter_values, data, features, answer, write_score)

    @classmethod
    def start(cls, executor, validator, learner, data, features, answer, write_score):
        paralleled_data = validator.points(data)
        executor.execute(
            lambda paralleled_data_element: write_score(
                learner.train_and_predict (
                    paralleled_data_element["training_data"].loc[:, features],
                    paralleled_data_element["training_data"].loc[:, answer],
                    paralleled_data_element["test_data"].loc[:, features]
                ),
                paralleled_data_element["test_data"].loc[:, answer],
                paralleled_data_element["test_data"],
                paralleled_data_element["count"]
            ),
            paralleled_data
        )