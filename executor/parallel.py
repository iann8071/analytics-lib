from pyspark import SparkConf, SparkContext


class Parallel:

    def __init__(self, app_name):
        conf = (SparkConf().setAppName(app_name))
        self.context = SparkContext(conf=conf)

    def execute(self, search, data):
        rdd = self.context.parallelize(data, len(data))
        rdd.foreach(search)