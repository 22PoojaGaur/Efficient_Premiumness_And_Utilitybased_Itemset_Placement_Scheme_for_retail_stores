TRAIN_SPLIT = 0.2
TEST_SPLIT = 1 - TRAIN_SPLIT
SUPPORT_THRESHOLD = 0.001
SD = 1.1
LS = 0.001
PRICE_BRACKETS = [
    (0.01, 0.16), (0.17, 0.33), (0.34, 0.50), (0.51, 0.67),
    (0.68, 0.84), (0.85, 1)]
K_FOR_KUI_IDX = 6
ALPHA = 0.2
KUI_DRANK_THRESHOLD = 0.2 # note that change is made on '>=' threshold
LAMBDA = 5000
NUM_TYPE_SLOTS = 3
# NUM_SLOTS is a dictionary to give num slots in each slot type
# so number of keys in NUM_SLOTS is equal to NUM_TYPE_SLOTS
# NUM_SLOTS = { 0: 220, 1: 400, 2: 450 }
# Max ration of a slot to be filled by one itemsets
ONE_ITEMSET_RATIO = 0.5 
ZIPF = 0.7


# slots for each size
# NUM_SLOTS =  { 0: 20, 1: 25, 2: 25 }
# NUM_SLOTS =  { 0: 50, 1: 60, 2: 60 }
# NUM_SLOTS =  { 0: 70, 1: 90, 2: 110 }
# NUM_SLOTS =  { 0: 80, 1: 90, 2: 200 }
# NUM_SLOTS =  { 0: 120, 1: 150, 2: 200 }
# NUM_SLOTS =  { 0: 120, 1: 200, 2: 250 }
#NUM_SLOTS =  { 0: 170, 1: 200, 2: 300 }
# NUM_SLOTS =  { 0: 170, 1: 250, 2: 350 }
# NUM_SLOTS =  { 0: 170, 1: 300, 2: 400 }
# NUM_SLOTS =  { 0: 170, 1: 400, 2: 400 }
#NUM_SLOTS =  { 0: 220, 1: 400, 2: 450 }

NUM_SLOTS = {0:4000, 1:5000, 2:4000}
