import argparse
import mock_data
from data_parser import parse_data
from kui_index import get_kui_index_and_arc
from ARC import get_arc

DEBUG_MODE = False

# Adding argument parser.
parser = argparse.ArgumentParser()
parser.add_argument('--data', '-d', help='add path to data file')

args = parser.parse_args()

# Global variables.
DATA_FNAME = args.data

if __name__ == '__main__':
    if DEBUG_MODE:
        data_dict = mock_data.DATA_DICT
    else:
        data_dict = parse_data(DATA_FNAME)
    print ('Data dictionary formed...')

    if DEBUG_MODE:
        kUI_idx = mock_data.KUI_IDX
        arc = mock_data.ARC
    else:
        (kUI_idx, arc) = get_kui_index_and_arc(data_dict)
    print('Done kUI Index and ARC...')

    print('KUI INDEX->')
    print(kUI_idx)
    print('ARC->')
    print(arc)
