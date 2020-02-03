import argparse
import mock_data
from data_parser import parse_data
from data_parser import parse_ch_dict
from calculate_drank import get_dranks
from kui_index import get_kui_index
from ARC import get_arc
from slots import get_slots
from PRIP import PRIP
from DPRIP import DPRIP

import _pickle as pkl
import time
from os import path
from random import random

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
        # kui_idx = get_kui_index(data_dict, dranks=dranks, method='R')
        kui_idx = get_kui_index(data_dict, dranks=dranks, method='R')
    else:
        # run without diversity mode
        if DEBUG_MODE:
            data_dict = mock_data.DATA_DICT
            kui_idx = mock_data
        else:
            data_dict = parse_data(DATA_FNAME, 'retail')
            kui_idx = get_kui_index(data_dict)
    # shuffling dict
    shuffled_key_value_list = sorted(data_dict.items(), key=lambda x: random())
    data_dict = dict(shuffled_key_value_list)
        
    
    # print (data_dict)
    # print (ch_dict)
    # print (dranks)
    # print (kui_idx)

    # to modify number of slots vary the number (second argument) below
    # data_dict = dict(itertools.islice(data_dict.items(), 1900))
    
    num_slots = sum([len(k) for k in data_dict.keys()])
    type_slots = 4
    zipf = 0.7

    start = time.time()
    slots = get_slots(num_slots, type_slots, zipf)
    arc = get_arc(data_dict)
    if CH_FNAME is not None:
        slots = DPRIP(data_dict, kui_idx, dranks, arc, slots)
    else:
        slots = PRIP(data_dict, kui_idx, arc, slots)
    end = time.time()

    print ('TIME -> ')
    print (end - start)

    output = open('prip_slots_%d.pkl' % type_slots, 'wb')
    pkl.dump(slots, output)
    output.close()

    #print('KUI INDEX->')
    #print(kUI_idx)
    #print('ARC->')
    #print(arc)
    # print('slots->')
    # print(slots)
