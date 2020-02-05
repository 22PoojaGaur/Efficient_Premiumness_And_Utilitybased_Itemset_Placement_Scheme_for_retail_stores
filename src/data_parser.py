'''
Returns Data dictionary with the format -
key -> itemset
value -> (support, price)
'''

import pyfpgrowth
import math
import random

# Set a very low threshold to get all itemsets
SUPPORT_THRESH = 1
K_FOR_KUI_IDX = 4

PRICE_BRACKETS = [
    (0.01, 0.16), (0.17, 0.33), (0.34, 0.50), (0.51, 0.67),
    (0.68, 0.84), (0.85, 1)]

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def parse_data(data_file_name, dataset_name):

    total_items = set()

    transactions = []
    with open(data_file_name, 'r') as f:
        for line in nonblank_lines(f):
            transactions.append(line)
    if dataset_name == 'retail':
        transactions = [[int(item) for item in transaction.strip().split(' ')] for transaction in transactions]
    elif dataset_name == 'tesco':
        transactions = [[item for item in transaction.strip().split(';')] for transaction in transactions]

    for transaction in transactions:
        for item in transaction:    
            total_items.add(item)

    patterns = pyfpgrowth.find_frequent_patterns(transactions, SUPPORT_THRESH)

    data = {}
    # print (patterns)
    for (itemset, support) in patterns.items():
        
        if len(itemset) > K_FOR_KUI_IDX:
            continue
        price_idx = int(math.floor(5.5*random.random()))
        price = random.randint(
            int(100*PRICE_BRACKETS[price_idx][0]), int(100*PRICE_BRACKETS[price_idx][1]))/100.0

        data[itemset] = (support, price)
    print(total_items)
    print (len(total_items))
    
    return data

def parse_ch_dict(ch_file_name):
    item_path_dict = {}
    is_item = True
    cur_item = ''
    path = []
    fin = open(ch_file_name, 'r')
    for line in fin.readlines():
        path = []
        if line.strip() == '':
            continue

        if is_item:
            # line is item
            item = line.strip()
            cur_item = item
            is_item = 0
        else:
            # line is path
            path = line.strip().split(' ')
            item_path_dict[cur_item] = path
            is_item = 1
    return item_path_dict
