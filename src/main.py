import argparse
import mock_data
from data_parser import parse_data
from data_parser import parse_ch_dict
from calculate_drank import get_dranks
from kui_index import get_kui_index
from ARC import get_arc
from slots import get_slots
from PRIP import PRIP

import _pickle as pkl
import time
from os import path

DEBUG_MODE = False

# Adding argument parser.
parser = argparse.ArgumentParser()
parser.add_argument('--data', '-d', help='add path to data file')
parser.add_argument(
    '--with_ch_path', '-ch_path', help='run the experiment with diversity', default=None)

args = parser.parse_args()

# Global variables.
DATA_FNAME = args.data
CH_FNAME = args.with_ch_path

if __name__ == '__main__':

    data_dict = {}
    ch_dict = {}
    dranks = {}
    if CH_FNAME is not None:
        # run with diversity mode
        data_dict = parse_data(DATA_FNAME, 'tesco')
        ch_dict = parse_ch_dict(CH_FNAME)
        dranks = get_dranks(data_dict.keys(), ch_dict)
    else:
        # run without diversity mode
        if DEBUG_MODE:
            data_dict = mock_data.DATA_DICT
        else:
            data_dict = parse_data(DATA_FNAME, 'retail')
    
    print (data_dict)
    print (ch_dict)
    print (dranks)
    

    print ('storing data dict for retail.txt in pickled dictionary')
    pkl.dump(data_dict, open('../data/retail_data_dict.pkl', 'wb'))

    if DEBUG_MODE:
        kUI_idx = mock_data.KUI_IDX
        arc = mock_data.ARC
    else:
        kUI_idx = get_kui_index(data_dict)
    print('Done kUI Index and ARC...')


    num_slots = sum([len(k) for k in data_dict.keys()])
    type_slots = 24
    zipf = 0.7

    start = time.time()
    slots = get_slots(num_slots, type_slots, zipf)
    arc = get_arc(data_dict)
    slots = PRIP(data_dict, kUI_idx, arc, slots)
    end = time.time()

    print ('TIME -> ')
    print (end - start)

    output = open('prip_slots_24.pkl', 'wb')
    pkl.dump(slots, output)
    output.close()

    #print('KUI INDEX->')
    #print(kUI_idx)
    #print('ARC->')
    #print(arc)
    # print('slots->')
    # print(slots)
