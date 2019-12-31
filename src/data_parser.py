'''
Returns Data dictionary with the format -
key -> itemset
value -> (support, price)
'''

import pyfpgrowth
import math
import random

# Set a very low threshold to get all itemsets
SUPPORT_THRESH = 10
K_FOR_KUI_IDX = 4

PRICE_BRACKETS = [
    (0.01, 0.16), (0.17, 0.33), (0.34, 0.50), (0.51, 0.67),
    (0.68, 0.84), (0.85, 1)]

def parse_data(data_file_name):
    transactions = None
    with open(data_file_name, 'r') as f:
        transactions = f.readlines()
    transactions = [[int(item) for item in transaction.strip().split(' ')] for transaction in transactions]

    patterns = pyfpgrowth.find_frequent_patterns(transactions, SUPPORT_THRESH)

    data = {}
    # print (patterns)
    for (itemset, support) in patterns.items():
        if len(itemset) > K_FOR_KUI_IDX:
            continue
        price_idx = math.floor(6.5*random.random())
        price = random.randint(
            100*PRICE_BRACKETS[price_idx][0], 100*PRICE_BRACKETS[price_idx][1])/100.0

        data[itemset] = (support, price)
    
    return data
