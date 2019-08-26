#!/usr/bin/env python3
"""
Author: Wing Yu Chung

"""	

#Import statements    	
from sys import argv

def read_dataset(filetxt):
    """"
    Turns dataset into list object
    
    Input: txt file separated by tabs
    Output: List of data from txt file.
    """"
    text = open(filetxt, 'r')
    dataset = text.read()
    dataset = dataset.split()
    text.close()
    return dataset

def dataset_to_int(dataset):
    dataset = list(map(int,dataset))
    return dataset
    
def sum_square_num(num_list):
    square_sum = 0
    for i in num_list:
        square_sum += i**2
    return square_sum

if __name__ == "__main__":
    dataset = read_dataset(argv[1])
    dataset = dataset_to_int(dataset)
    print(sum_square_num(dataset))
