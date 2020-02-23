TRAIN_SPLIT = 0.9
TEST_SPLIT = 1 - TRAIN_SPLIT
SUPPORT_THRESHOLD = 0.001
SD = 1.1
LS = 0.001
PRICE_BRACKETS = [
    (0.01, 0.16), (0.17, 0.33), (0.34, 0.50), (0.51, 0.67),
    (0.68, 0.84), (0.85, 1)]
K_FOR_KUI_IDX = 4
ALPHA = 0.2
LAMBDA = 5000
NUM_TYPE_SLOTS = 3
# NUM_SLOTS is a dictionary to give num slots in each slot type
# so number of keys in NUM_SLOTS is equal to NUM_TYPE_SLOTS
NUM_SLOTS = { 
    0: 10,
    1: 10,
    2: 10
}
# Max ration of a slot to be filled by one itemsets
ONE_ITEMSET_RATIO = 0.8
ZIPF = 0.7