#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Return ID of ID of sequence string and content of GC from file c
containing multiple sequences.
"""	

#Import statements    	
from sys import argv

def read_dataset(filetxt):
    """
    Turns dataset into string object
    
    Input: txt file with string
    Output: string of data from txt file.
    """
    text = open(filetxt, 'r')
    dataset = text.read()
    
    text.close()
    
    return dataset

def split_dataset(dataset):
    """
    Turns dataset into dictonary with id and sequence object
    Input: txt file with fasta sequences
    Output: dictonary of id and sequences.
    """
    dataset = dataset.split(">")
    del dataset[0]
    #print(dataset)
    sequences = {}
    for sequence in dataset:
        rosa_id, seq = sequence.split("\n",1)
        sequences[rosa_id] = seq
    for rosa_id in sequences.keys():
        sequences[rosa_id] = sequences[rosa_id].replace("\n","")
  
    return sequences

def count_gc(dna_sequence):
    """
        Determines gc content for sequences
        Input: dictornary  with id and fasta sequences
        Output: dictonary of id and gc content.
    """
    id_gc_dict = {}
    for key, sequence in dna_sequence.items():
        gc_count = 0
        for nuc in sequence:
            if nuc == "G" or nuc == "C":
                gc_count +=1
        id_gc_dict[key] = gc_count/len(sequence)*100
    
    return id_gc_dict

def max_count_gc(dna_sequence):
    """
        Determine Id with highest gc content
        Input: dictionary with id and gc content
        Output: print of id with highest gc content
    """
    max_gc_value= max(dna_sequence.values())
    max_gc_key=''
    for key,value in dna_sequence.items():
        if value == max_gc_value:
            max_gc_key = key
    max_gc_value = round(max_gc_value,7)
    print(max_gc_key)
    print(max_gc_value)
    return


if __name__ == "__main__":
    sequence = read_dataset(argv[1])
    #print(sequence)
    sequence_dict = split_dataset(sequence)
    gc_content = count_gc(sequence_dict)
    max_count_gc(gc_content)
