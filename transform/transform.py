class Transform:

    def __init__(self, valid_ranges, scale_types):
        self.valid_ranges = valid_ranges
        self.scale_types = scale_types

    def extract_valid_data(self, data):
        valid_data = data
        for key in self.valid_ranges.keys():
            for _min, _max in self.valid_ranges[key]:
                valid_data = valid_data[(valid_data[key] >= _min) & (valid_data[key] <= _max)]
        return valid_data

    def scale_data(self, data):
        scaled_data = data
        for key in self.scale_types.keys():
            scaler = self.scale_types[key]
            data[key] = scaler.transform(data[key])
        return scaled_data

    def execute(self, row_data):
        valid_data = self.extract_valid_data(row_data)
        scaled_valid_data = self.scale_data(valid_data)
        scaled_valid_data = scaled_valid_data.convert_objects(convert_numeric=True).dropna().reset_index(drop=True)
        return scaled_valid_data

