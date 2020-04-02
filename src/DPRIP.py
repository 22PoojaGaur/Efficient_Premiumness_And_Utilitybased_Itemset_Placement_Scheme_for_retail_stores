'''
Given arc, kui index, data dictionary, dranks, slots
Runs DPRIP algorithm and returns slots.
'''
from PRIP import PRIP

# This placement scheme will place itemsets based on the per_slot_revenue
# contribution
def _DPRIP(deta_dict, kui_idx, dranks, arc, slot_sizes):
    TOTAL_PATTERNS = 0
    TOTAL_SLOTS = 0
    TOTAL_REVENUE = 0
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
        top_kui_per_slot_rev[i] = (kui_idx[i][top_kui_ptrs[i]][-2])/float(i)
    total_placed = 0
    drank_mean = 0
    for stype in range(0, slot_types):
        while CAS[stype] >= 0:
            # top -> [idx, price]
            top = [0,0]
            for idx, val in enumerate(top_kui_per_slot_rev):
                if val > top[1]:
                    top = [idx, val]
            top_kui_node = kui_idx[top[0]][top_kui_ptrs[top[0]]]
            print (top)
            print (top_kui_node)
            if len(kui_idx[top[0]][top_kui_ptrs[top[0]]][0]) > 1:
                TOTAL_PATTERNS += 1
                slots[stype].append((
                    kui_idx[top[0]][top_kui_ptrs[top[0]]][0],
                    kui_idx[top[0]][top_kui_ptrs[top[0]]][2], 
                    kui_idx[top[0]][top_kui_ptrs[top[0]]][-1]))
                drank_mean += kui_idx[top[0]][top_kui_ptrs[top[0]]][-1]
                total_placed += 1
                TOTAL_REVENUE += (kui_idx[top[0]][top_kui_ptrs[top[0]]][-2] * 1.0)/(1+stype)
                CAS[stype] -= len(kui_idx[top[0]][top_kui_ptrs[top[0]]][0])
            top_kui_ptrs[top[0]] += 1
            if top_kui_ptrs[top[0]] >= len(kui_idx[top[0]]):
                top_kui_per_slot_rev[top[0]] = -1
            else:
                top_kui_per_slot_rev[top[0]] = kui_idx[top[0]][top_kui_ptrs[top[0]]][-2]/float(top[0])

    print ('TOTAL REVENUE TRAINING ')
    print (TOTAL_REVENUE)
    print ('DRANK MEAN')
    print (drank_mean/float(total_placed))
    print ('PATTERNS PLACED (TRAIN)')
    print (TOTAL_PATTERNS)
    print ('SLOTS TOTAL')
    print (TOTAL_SLOTS)
    # print ('CAS ->')
    # print (CAS)
    # print (top_kui_per_slot_rev)
    # print (slot_types)
    # print (max(enumerate(top_kui_per_slot_rev)))
    # print (kui_idx[4][0])
    # print (kui_idx[3][0])
    # print (kui_idx[2][0])
    # print (kui_idx[1][0])
    return slots

def DPRIP(data_dict, kui_idx, dranks, arc, slot_sizes, method='INDIVIDUAL'):
    slots = _DPRIP(data_dict, kui_idx, dranks, arc, slot_sizes)
    # if method == 'INDIVIDUAL':
    #     slots = PRIP(data_dict, kui_idx, arc, slot_sizes)
    # elif method == 'OVERALL':
    #     slots = _DPRIP(data_dict, kui_idx, dranks, arc, slot_sizes)
    return slots
