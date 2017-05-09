from sklearn.model_selection import KFold


class CrossValidation:

    def __init__(self, k_fold):
        self.k_fold = k_fold

    def execute(self, learner, features, answer, data, write_score):
        results = []
        count = 1
        for training_data_indices, test_data_indices in KFold(n_splits=self.k_fold).split(data):
            training_data = data.loc[training_data_indices, :]
            test_data = data.loc[test_data_indices, :]
            learner.train(training_data.loc[:, features], training_data.loc[:, answer])
            write_score(learner.predict(
                test_data.loc[:, features]),
                test_data.loc[:, answer],
                test_data,
                learner.hyper_parameters()
            )
            count += 1

        return results
