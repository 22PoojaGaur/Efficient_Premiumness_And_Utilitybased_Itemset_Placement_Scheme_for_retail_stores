SUPPORT_THRESHOLD = 0.01
PRICE_BRACKETS = [
    (0.01, 0.16), (0.17, 0.33), (0.34, 0.50), (0.51, 0.67),
    (0.68, 0.84), (0.85, 1)]
K_FOR_KUI_IDX = 6
ALPHA = 0.2
LAMBDA = 500
NUM_TYPE_SLOTS = 4
# NUM_SLOTS is a dictionary to give num slots in each slot type
# so number of keys in NUM_SLOTS is equal to NUM_TYPE_SLOTS
NUM_SLOTS = {
    0: 100,
    1: 100,
    2: 100,
    3: 100
}
ZIPF = 0.7