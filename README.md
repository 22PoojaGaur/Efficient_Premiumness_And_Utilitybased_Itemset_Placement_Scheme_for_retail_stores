# Efficient_Premiumness_And_Utilitybased_Itemset_Placement_Scheme_for_retail_stores
Implementation of the paper "An Efficient Premiumness and Utility based Itemset Placement Scheme for Retail Stores".


# process to run and generate data for plotting graph

-> cd results/
-> rm \*.pkl
-> cd ../
-> run the command `bash commands.sh` continuously with changing variables in global files
-> The results would be generated in format `results/METHOD_METRIC.pkl`. Each `.pkl` file in results folder is a list.
-> to read the list run below commands
-> ipython
-> import pickle as pkl
-> lis = pkl.load(open(filename, 'rb')) # this will load pickle file in lis as a list
-> lis # this will print the list in ipython terminal copy paste to graph file for plotting.

