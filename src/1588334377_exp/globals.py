TRAIN_SPLIT = 0.2
TEST_SPLIT = 1 - TRAIN_SPLIT
MINING_METHOD = 'apriori'
SUPPORT_THRESHOLD = 0.002

# below are specifically for ims apriori
SD = 1.1
LS = 0.001

PRICE_BRACKETS = [
    (0.01, 0.16), (0.17, 0.33), (0.34, 0.50), (0.51, 0.67),
    (0.68, 0.84), (0.85, 1)]
METHOD = 'RH'
# This will change the placement scheme to 
# place slot with higher per_slot_drank
# in case of D and remain same in case of others
SEPARATE_PLACEMENT_SCHEMES = True

# below are specifically for RH (similar to HC-HCHD) method.
R_RATIO = 0.2
H_RATIO = 0.8

K_FOR_KUI_IDX = 4
ALPHA = 0.2
KUI_DRANK_THRESHOLD = 0.1 # note that change is made on '>=' threshold
LAMBDA = 100000
NUM_TYPE_SLOTS = 3
# NUM_SLOTS is a dictionary to give num slots in each slot type
# so number of keys in NUM_SLOTS is equal to NUM_TYPE_SLOTS
# NUM_SLOTS = { 0: 220, 1: 400, 2: 450 }
# Max ration of a slot to be filled by one itemsets
ONE_ITEMSET_RATIO = 0.5 
ZIPF = 0.7


# slots for each size
# 70
NUM_SLOTS =  { 0: 20, 1: 25, 2: 25 }

# 170
# NUM_SLOTS =  { 0: 50, 1: 60, 2: 60 }

# 270
# NUM_SLOTS =  { 0: 70, 1: 90, 2: 110 }

# 370
# NUM_SLOTS =  { 0: 80, 1: 90, 2: 200 }

# 470
# NUM_SLOTS =  { 0: 120, 1: 150, 2: 200 }

# 570 
# NUM_SLOTS =  { 0: 120, 1: 200, 2: 250 }

# 670
# NUM_SLOTS =  { 0: 170, 1: 200, 2: 300 }

# 770
# NUM_SLOTS =  { 0: 170, 1: 250, 2: 350 }

# 870
# NUM_SLOTS =  { 0: 170, 1: 300, 2: 400 }

# 970
# NUM_SLOTS =  { 0: 170, 1: 400, 2: 400 }

# 1070
# NUM_SLOTS =  { 0: 220, 1: 400, 2: 450 }

# # 1200
# NUM_SLOTS = {0: 400, 1: 400, 2: 400}

# 1500
#NUM_SLOTS = {0: 400, 1: 500, 2: 600}

# # 2000
# NUM_SLOTS = {0: 500, 1: 700, 2: 800}

# # 2500
#NUM_SLOTS = {0: 700, 1: 900, 2: 900}

# 300
# NUM_SLOTS = {0: 100, 1: 100, 2: 100}

# # 600
# NUM_SLOTS = {0: 150, 1: 250, 2: 200}

# # 900
# NUM_SLOTS = {0: 250, 1: 250, 2: 400}

# # 3000
#NUM_SLOTS = {0: 800, 1: 1100, 2: 1100}

# # 4000
#NUM_SLOTS = {0: 1000, 1: 1500, 2: 1500}

# # 5000
#NUM_SLOTS = {0: 1500, 1: 1500, 2: 2000}

# 6000
#NUM_SLOTS = {0: 2000, 1: 2000, 2: 2000}

# 8000
#NUM_SLOTS = {0: 3000, 1: 2500, 2: 2500}

# 10000
#NUM_SLOTS = {0: 3000, 1: 3500, 2: 3500}
#NUM_SLOTS = {0: 40000, 1:40000, 2:40000}

#-----------------------------------------
# 500
# NUM_SLOTS = {0: 150, 1: 150, 2: 200}

# # 2000
# NUM_SLOTS = {0: 700, 1: 600, 2: 700}

# # 4000
# NUM_SLOTS = {0: 1000, 1: 1500, 2: 1500}

# # 8000
# NUM_SLOTS = {0: 3000, 1: 3000, 2: 2000}

# 10000
# NUM_SLOTS = {0: 3500, 1: 3500, 2: 3000}
NUM_SLOTS = {0: 20, 1: 25, 2: 25}
NUM_SLOTS = {0: 50, 1: 60, 2: 60}
NUM_SLOTS = {0: 80, 1: 90, 2: 200}
NUM_SLOTS = {0: 150, 1: 250, 2: 200}
NUM_SLOTS = {0: 250, 1: 250, 2: 400}
NUM_SLOTS = {0: 400, 1: 500, 2: 600}
NUM_SLOTS = {0: 500, 1: 700, 2: 800}
NUM_SLOTS = {0: 800, 1: 1100, 2: 1100}
NUM_SLOTS = {0: 1500, 1: 1500, 2: 2000}
NUM_SLOTS = {0: 3000, 1: 2500, 2: 2500}
NUM_SLOTS = {0: 3000, 1: 3500, 2: 3500}