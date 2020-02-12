import argparse
import mock_data
import itertools
from data_parser import parse_data
from data_parser import parse_ch_dict
from calculate_drank import get_dranks
from kui_index import get_kui_index
from ARC import get_arc
from slots import get_slots
from PRIP import PRIP
from DPRIP import DPRIP
import globals

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
        kui_idx = get_kui_index(data_dict, dranks=dranks, method='H')
    else:
        # run without diversity mode
        if DEBUG_MODE:
            data_dict = mock_data.DATA_DICT
            kui_idx = mock_data
        else:
            data_dict = parse_data(DATA_FNAME, 'retail')
            kui_idx = get_kui_index(data_dict)
     
    # num_slots gives number of slot in each slot type
    num_slots = globals.NUM_SLOTS
    type_slots = globals.NUM_TYPE_SLOTS
    zipf = globals.ZIPF

    start = time.time()
    # get empty slots
    slots = get_slots(num_slots, type_slots, zipf)
    # get sorted arc
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
    # print (kui_idx[1])
    # print(len(kui_idx[1]))
    # print(kui_idx[2])
    # print (len(kui_idx[3]))
    # print (len(kui_idx[4]))
    # print(len(kui_idx[5]))
    # print (len(kui_idx[6]))
    #print('ARC->')
    #print(arc)
    # print('slots->')
    # print(slots)
