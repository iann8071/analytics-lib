import os
import csv


class OutputWriter:
    output_dir = 'output'

    @classmethod
    def dict_to_csv(cls, file_name, field_names, row):
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), cls.output_dir, file_name)
        is_new = not os.path.exists(file_path)

        with open(file_path, 'a', newline='') as _csv:
            writer = csv.DictWriter(_csv, field_names)
            if is_new:
                writer.writeheader()
            writer.writerow(row)
