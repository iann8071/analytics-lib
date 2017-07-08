import pandas as pd


class Adapter:

    @classmethod
    def to_np(cls, obj):
        if isinstance(obj, pd.DataFrame):
            return obj.as_matrix()
        else:
            return obj
