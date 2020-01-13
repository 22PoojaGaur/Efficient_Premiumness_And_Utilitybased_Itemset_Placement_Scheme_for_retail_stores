import argparse
import mock_data
from data_parser import parse_data
from kui_index import get_kui_index_and_arc
from ARC import get_arc
from slots import get_slots
from PRIP import PRIP

DEBUG_MODE = True

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

    num_slots = sum([len(k) for k in data_dict.keys()])
    type_slots = 4
    zipf = 0.7

    slots = get_slots(num_slots, type_slots, zipf)

    slots = PRIP(data_dict, kUI_idx, arc, slots)

    print('KUI INDEX->')
    print(kUI_idx)
    print('ARC->')
    print(arc)
    print('slots->')
    print(slots)
