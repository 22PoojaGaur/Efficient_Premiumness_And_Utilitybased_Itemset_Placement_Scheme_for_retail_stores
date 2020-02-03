'''
Given arc, kui index, data dictionary, dranks, slots
Runs DPRIP algorithm and returns slots.
'''
from PRIP import PRIP

def _DPRIP(deta_dict, kui_idx, dranks, arc, slot_sizes):
    return slot_sizes

def DPRIP(data_dict, kui_idx, dranks, arc, slot_sizes, method='INDIVIDUAL'):
    if method == 'INDIVIDUAL':
        slots = PRIP(data_dict, kui_idx, arc, slot_sizes)
    elif method == 'OVERALL':
        slots = _DPRIP(data_dict, kui_idx, dranks, arc, slot_sizes)
    return slots
