import argparse
from data_parser import parse_data
from kui_index import get_kui_index

# Adding argument parser.
parser = argparse.ArgumentParser()
parser.add_argument('--data', '-d', help='add path to data file')

args = parser.parse_args()

# Global variables.
DATA_FNAME = args.data

if __name__ == '__main__':
    data_dict = parse_data(DATA_FNAME)

    kUI_idx = get_kui_index(data_dict)
