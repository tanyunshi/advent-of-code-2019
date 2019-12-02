from os import path

DATA_PATH = path.join(path.dirname(__file__), 'data')


def get_input_entries(file_name):
    data_file = path.join(DATA_PATH, file_name)
    with open(data_file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def read_int_inline(file_name):
    data_file = path.join(DATA_PATH, file_name)
    with open(data_file, 'r') as f:
        return [int(number) for number in f.readline().split(',')]
