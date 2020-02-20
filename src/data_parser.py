'''
Returns Data dictionary with the format -
key -> itemset
value -> (support, price)
'''

# import pyfpgrowth
from efficient_apriori import apriori
import math
import random
import globals

# Set a very low threshold to get all itemsets
SUPPORT_THRESH = globals.SUPPORT_THRESHOLD
K_FOR_KUI_IDX = globals.K_FOR_KUI_IDX
TEST_RATIO = globals.TEST_SPLIT
TRAIN_RATIO = globals.TRAIN_SPLIT

PRICE_BRACKETS = globals.PRICE_BRACKETS

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def parse_data(data_file_name, dataset_name):
    '''
    Args -
        data_file_name: str. file name for dataset
        dataset_name: str. Name of dataset in ['tesco', 'retail']
    '''
    transactions = []
    with open(data_file_name, 'r') as f:
        for line in nonblank_lines(f):
            transactions.append(line)
    if dataset_name == 'retail':
        transactions = [[int(item) for item in transaction.strip().split(' ')] for transaction in transactions]
    elif dataset_name == 'tesco':
        transactions = [[item for item in transaction.strip().split(';')] for transaction in transactions]

    # split transactions in test train
    data_size = len(transactions)
    train_transactions = transactions
    test_transactions = transactions[int(TRAIN_RATIO*data_size)+1 : data_size]
    test_transactions = [trans for trans in test_transactions if len(trans) <= K_FOR_KUI_IDX and len(trans) > 1]

    patterns, rules = apriori(train_transactions, min_support=SUPPORT_THRESH, min_confidence=1)
    # get patterns to pyfpgrowth result format
    mod_patterns = {}
    for key in patterns.keys():
        for k, v in patterns[key].items():
            mod_patterns[k] = v
    patterns = mod_patterns

    prices = {}
    for (itemset, support) in patterns.items():
        if len(itemset) == 1:
            price_idx = random.randint(0, len(PRICE_BRACKETS) -1)
            price = random.randint(
                int(100*PRICE_BRACKETS[price_idx][0]), int(100*PRICE_BRACKETS[price_idx][1]))/100.0
            prices[itemset[0]] = price
    
    data = {}
    for (itemset, support) in patterns.items():
        if len(itemset) > K_FOR_KUI_IDX:
            continue
        # price_idx = random.randint(0, len(PRICE_BRACKETS) - 1)
        # price = random.randint(
        #     int(100*PRICE_BRACKETS[price_idx][0]), int(100*PRICE_BRACKETS[price_idx][1]))/100.0
        sum_price = 0
        for item in itemset:
            sum_price += prices[item]
        data[itemset] = (support, sum_price)

    return (data, test_transactions)

def parse_ch_dict(ch_file_name):
    '''
    Args -
        ch_file_name: str. File name containing concept hierarchy data.
    '''
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
