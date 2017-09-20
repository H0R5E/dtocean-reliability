

import os
import pprint
import time
from collections import Counter

import numpy as np
import matplotlib.pylab as plt

from dtocean_reliability import start_logging
from dtocean_reliability.main import Variables, Main

this_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(this_dir, "..", "sample_data")

def main():    
    '''Test that main generates a non empty output'''
    
    input_variables = Variables(20.0 * 365.25 * 24.0, # mission time in hours
                                'wavefloat', # user-defined bill of materials
                                eval(open(os.path.join(data_dir, 'dummydb1.txt')).read()), #Options: 'tidefloat', 'tidefixed', 'wavefloat', 'wavefixed'
                                0.4 * 20.0 * 365.25 * 24.0, # target mean time to failure in hours
                                'multiplehubs', #Options: 'radial', 'singlesidedstring', 'doublesidedstring', 'multiplehubs' 
                                eval(open(os.path.join(data_dir, 'dummystarhier.txt')).read()), # electrical system hierarchy
                                eval(open(os.path.join(data_dir, 'dummystarbom.txt')).read()), # database
                                None,#eval(open(os.path.join(data_dir, 'dummymoorhiereg10.txt')).read()), # mooring system hierarchy
                                None)#eval(open(os.path.join(data_dir, 'dummymoorbomeg10.txt')).read())) # database
                                
    test = Main(input_variables)    
    mttf, rsystime = test()
    
    return mttf, rsystime, test
    
def plot(rsystime):
    
    data = np.array(rsystime)
    plt.plot(data[:,0], data[:,1])
    plt.ylabel('System reliability', fontsize=10)
    plt.xlabel('Time [hours]', fontsize=10)     
    plt.show()
    
if __name__ == "__main__":

    start_logging(level="DEBUG")
    
    mttf, rsystime, test = main()
    
    pprint.pprint(['Mean time to failure (hours)',mttf])
    pprint.pprint(['Mean time to failure (years)',mttf/(24.0*365.25)])
#    plot(rsystime)

    pprint.pprint(test.rsubsysvalues2)
    pprint.pprint(test.rsubsysvalues3)
