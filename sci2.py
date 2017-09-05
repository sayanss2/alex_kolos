#!/usr/bin/env python3
from ns4 import *
from stupid import *

def main():
    num = 0
    func = counter
    time_run = 10
    
    new_model = Model(func, num) #Create a model with previously described parameters
    new_model.run(time_run) #Run simulation model
        
if __name__ == '__main__':
    main()