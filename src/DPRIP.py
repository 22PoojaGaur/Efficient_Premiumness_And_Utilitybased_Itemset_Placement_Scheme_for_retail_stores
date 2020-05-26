'''
Given arc, kui index, data dictionary, dranks, slots
Runs DPRIP algorithm and returns slots.
'''
from PRIP import PRIP
import globals

TOTAL_SLOTS = 0
TOTAL_REVENUE = 0
DRANK_MEAN = 0
TOTAL_PLACED = 0


# takes advantage of the fact that everything is passed
# by reference in python. So
# even though this function does not return anything,
# it still changes both slots and top_kui_per_slot_rev
# arrays
def insert_one_itemset(slots, top_kui_per_slot_rev, top_kui_ptrs, kui_idx, CAS, stype, method=None):
    global TOTAL_SLOTS, TOTAL_REVENUE, DRANK_MEAN, TOTAL_PLACED

    found = False

    while not found:
        top = [None,0]
        for idx, val in enumerate(top_kui_per_slot_rev):
            # ignoring single itemsets
            if idx == 0 or idx == 1:
                continue
            if val > top[1]:
                top = [idx, val]

        if top[0] is None:
            print ('NOT ENOUGH ITEMSETS')
            return
    
        top_kui_node = kui_idx[top[0]][top_kui_ptrs[top[0]]]
        all_slots = list()
        for slot_type in range (0, globals.NUM_TYPE_SLOTS):
            all_slots.extend(slots[slot_type])
        placed = [node[0] for node in all_slots]
        # print (top_kui_per_slot_rev)
        
        if top_kui_node[0] not in placed:
            slots[stype].append((
                kui_idx[top[0]][top_kui_ptrs[top[0]]][0],
                kui_idx[top[0]][top_kui_ptrs[top[0]]][2], 
                kui_idx[top[0]][top_kui_ptrs[top[0]]][-1]))

            DRANK_MEAN += kui_idx[top[0]][top_kui_ptrs[top[0]]][-1]
            TOTAL_PLACED += 1
            TOTAL_REVENUE += (kui_idx[top[0]][top_kui_ptrs[top[0]]][-2] * 1.0)/(1+stype)
            CAS[stype] -= len(kui_idx[top[0]][top_kui_ptrs[top[0]]][0])
        
            found = True
        else:
            pass

        top_kui_ptrs[top[0]] += 1

        # if all itemstes of certain sized already placed
        if top_kui_ptrs[top[0]] >= len(kui_idx[top[0]]):
            top_kui_per_slot_rev[top[0]] = -1
        else:
            if globals.SEPARATE_PLACEMENT_SCHEMES and method == 'D':
                top_kui_per_slot_rev[top[0]] = kui_idx[top[0]][top_kui_ptrs[top[0]]][-1]/float(top[0])
            else:
                top_kui_per_slot_rev[top[0]] = kui_idx[top[0]][top_kui_ptrs[top[0]]][-2]/float(top[0])
        
        if found:
            break
    return


# This placement scheme will place itemsets based on the per_slot_revenue
# contribution
def _DPRIP(deta_dict, kui_idx, dranks, slot_sizes, method):
    global TOTAL_SLOTS, TOTAL_REVENUE, DRANK_MEAN, TOTAL_PLACED

    slots = []
    slot_types = len(slot_sizes)
    for i in range(0, slot_types):
        TOTAL_SLOTS += len(slot_sizes[i])
        slots.append([])
    CAS = []
    for stype in range(0, slot_types):
        CAS.append(len(slot_sizes[stype]))
    top_kui_ptrs = [0]*(len(kui_idx.keys())+1)
    top_kui_per_slot_rev = [0]*(len(kui_idx.keys())+1)
    for i in kui_idx.keys():
        try:
            if method == 'D' and globals.SEPARATE_PLACEMENT_SCHEMES == True:
                top_kui_per_slot_rev[i] = (kui_idx[i][top_kui_ptrs[i]][-1])/float(i)
            else:
                top_kui_per_slot_rev[i] = (kui_idx[i][top_kui_ptrs[i]][-2])/float(i)
        except:
            top_kui_per_slot_rev[i] = -1
    for stype in range(0, slot_types):
        while CAS[stype] > 0:
            insert_one_itemset(
                slots, top_kui_per_slot_rev,
                top_kui_ptrs, kui_idx, CAS, stype, method)
    
    print ('TOTAL REVENUE TRAINING ')
    print (TOTAL_REVENUE)
    print ('DRANK MEAN')
    print (DRANK_MEAN/float(TOTAL_PLACED))
    # print ('PATTERNS PLACED (TRAIN)')
    # print (TOTAL_PATTERNS)
    print ('SLOTS TOTAL')
    print (TOTAL_SLOTS)
    
    return (slots, TOTAL_SLOTS, TOTAL_REVENUE,
                DRANK_MEAN/float(TOTAL_PLACED))


def _RHDPRIP(data_dict, kui_R, kui_H, dranks, slot_sizes):
    global TOTAL_SLOTS, TOTAL_REVENUE, DRANK_MEAN, TOTAL_PLACED

    slots = [] # final slots 2d list
    CAS = [] # currently available slots
    slot_types = len(slot_sizes)

    for stype in range(0, slot_types):
        TOTAL_SLOTS += len(slot_sizes[stype])
        slots.append([])
        CAS.append(len(slot_sizes[stype]))

    # store pointers to next candidate of each itemset length
    top_kuir_ptrs = [0] * (len(kui_R.keys()) + 1)
    top_kuir_per_slot_revenue = [0] * (len(kui_R.keys()) + 1)
    for i in kui_R.keys():
        try:
            top_kuir_per_slot_revenue[i] = kui_R[i][0][-2]
        except:
            top_kuir_per_slot_revenue[i] = -1

    top_kuih_ptrs = [0] * (len(kui_H.keys()) + 1)
    top_kuih_per_slot_revenue = [0] * (len(kui_H.keys()) + 1)
    for i in kui_H.keys():
        try:
            top_kuih_per_slot_revenue[i] = kui_H[i][0][-2]
        except:
            top_kuih_per_slot_revenue[i] = -1

    pick_r_or_h = list(['R']*int(globals.R_RATIO * 10))
    pick_r_or_h.extend(['H']*int(globals.H_RATIO * 10))
    kui_to_pick_ptr = 0

    for stype in range(0, slot_types):
        while CAS[stype] > 0:
            if pick_r_or_h[kui_to_pick_ptr] == 'R':
                insert_one_itemset(
                    slots, top_kuir_per_slot_revenue,
                    top_kuir_ptrs, kui_R, CAS, stype)
            elif pick_r_or_h[kui_to_pick_ptr] == 'H':
                insert_one_itemset(
                    slots, top_kuih_per_slot_revenue,
                    top_kuih_ptrs, kui_H, CAS, stype)
            kui_to_pick_ptr = (kui_to_pick_ptr + 1)%10

    print ('TOTAL REVENUE TRAINING ')
    print (TOTAL_REVENUE)
    print ('DRANK MEAN')
    print (DRANK_MEAN/float(TOTAL_PLACED))
    print ('SLOTS TOTAL')
    print (TOTAL_SLOTS)

    return (slots, TOTAL_SLOTS, TOTAL_REVENUE,
                DRANK_MEAN/float(TOTAL_PLACED))


def DPRIP(data_dict, kui_idx, dranks, slot_sizes, method='INDIVIDUAL'):
    if method == 'RH':
        return _RHDPRIP(data_dict, kui_idx['R'], kui_idx['H'], dranks, slot_sizes)
    else:
        return _DPRIP(data_dict, kui_idx, dranks, slot_sizes, method)
