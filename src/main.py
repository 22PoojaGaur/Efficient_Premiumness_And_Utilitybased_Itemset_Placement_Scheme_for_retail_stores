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
from evaluate import evaluate
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
        if path.isfile('dataset.pkl') and path.isfile('test.pkl'):
            train_data_dict = pkl.load(open('dataset.pkl', 'rb'))
            test_transactions = pkl.load(open('test.pkl', 'rb'))
        else:
            (train_data_dict, test_transactions) = parse_data(DATA_FNAME, 'tesco')
            pkl.dump(train_data_dict, open('dataset.pkl', 'wb'))
            pkl.dump(test_transactions, open('test.pkl', 'wb'))
        ch_dict = parse_ch_dict(CH_FNAME)
        dranks = get_dranks(train_data_dict.keys(), ch_dict)
        # kui_idx = get_kui_index(data_dict, dranks=dranks, method='R')
        kui_idx = get_kui_index(train_data_dict, dranks=dranks, method='R')
    else:
        # run without diversity mode
        if DEBUG_MODE:
            train_data_dict = mock_data.DATA_DICT
            kui_idx = mock_data
        else:
            (train_data_dict, test_transactions) = parse_data(DATA_FNAME, 'retail')
            kui_idx = get_kui_index(train_data_dict)
     
    # num_slots gives number of slot in each slot type
    num_slots = globals.NUM_SLOTS
    type_slots = globals.NUM_TYPE_SLOTS
    zipf = globals.ZIPF

    start = time.time()
    # get empty slots
    slots = get_slots(num_slots, type_slots, zipf)
    # get sorted arc
    arc = get_arc(train_data_dict)
    if CH_FNAME is not None:
        slots = DPRIP(train_data_dict, kui_idx, dranks, arc, slots)
    else:
        slots = PRIP(train_data_dict, kui_idx, arc, slots)
    end = time.time()

    print ('TIME -> ')
    print (end - start)

    output = open('prip_slots_%d.pkl' % type_slots, 'wb')
    pkl.dump(slots, output)
    output.close()
    # print (kui_idx)

    evaluate(slots, test_transactions)
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
