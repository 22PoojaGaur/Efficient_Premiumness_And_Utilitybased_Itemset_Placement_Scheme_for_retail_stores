
import time
import os
import shutil
import subprocess

# Number of slots to use
NUM_SLOTS = {
    '70': { 0: 20, 1: 25, 2: 25 },
    '170': { 0: 50, 1: 60, 2: 60 },
    '370': { 0: 80, 1: 90, 2: 200 },
    '600': {0: 150, 1: 250, 2: 200},
    '900': {0: 250, 1: 250, 2: 400},
    '1500': {0: 400, 1: 500, 2: 600},
    '2000': {0: 500, 1: 700, 2: 800},
    '3000': {0: 800, 1: 1100, 2: 1100},
    '5000': {0: 1500, 1: 1500, 2: 2000},
    '8000': {0: 3000, 1: 2500, 2: 2500},
    '10000': {0: 3000, 1: 3500, 2: 3500}
}

bash_cmd = 'python3 main.py -d ../data/grocery_transactions.txt -ch_path ../data/grocery_ch.txt'

# create directory to save experiment details
create_experiment_dir = 'exp_alpha0.7_Rratio0.1_Hratio0.9/'
if not os.path.exists(create_experiment_dir):
    os.mkdir(create_experiment_dir)

shutil.copyfile('globals.py', 'globals_bk.py')

for key in NUM_SLOTS.keys():
    gfile = open('globals.py', 'a')
    num_slots_str = '\nNUM_SLOTS = ' + str(NUM_SLOTS[key])
    gfile.write(num_slots_str)
    gfile.close()

    process = subprocess.Popen(bash_cmd.split())

    stdout, stderr = process.communicate()

if not os.path.exists(create_experiment_dir + 'globals.py'):
    shutil.move('globals.py', create_experiment_dir)

if not os.path.exists(create_experiment_dir + 'results/'):
    os.mkdir(create_experiment_dir + 'results/')

files = os.listdir('results/')

for f in files:
    shutil.move('results/'+f, create_experiment_dir + 'results/')

shutil.move('globals_bk.py', 'globals.py')
