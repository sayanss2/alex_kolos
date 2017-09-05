#!/usr/bin/env python3
from ns4 import *
from stupid import *

def main():
    func = time_show #Running function
    file_input = '/tmp/fileIN.tmp' #Source file
    file_output = '/tmp/fileOUT.tmp' #File-sink
    file_io = file_input, file_output #Tuple of variables (Source file, File-sink)
    num_node = 2 #Number of connected nodes
    transport_protocol = 'TCP' #Connection protocol
    time_run = 10 #Simulation time
    
    new_model = Model(func, f_io=file_io, n_nde=num_node, t_prl=transport_protocol) #Create a model with previously described parameters
    new_model.run(time_run) #Run simulation model
        
if __name__ == '__main__':
    main()
