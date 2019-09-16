#!/usr/bin/env python3
"""
Author: Wing Yu Chung

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation
to generate terms for progressively larger values of n. This problem introduces us to the computational technique of
dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

# Import statements
from sys import argv


def read_dataset(filetxt):
    """
    Turns dataset into string object
    Input: txt file with string
    Output: string of data from txt file.
    """
    text = open(filetxt, 'r')
    dataset = text.read()
    dataset = dataset.strip()
    text.close()
    return dataset

def split_dataset(dataset):
    """
    Turns dataset string separated by \n into a list
    """
    sequence = dataset.split()
    return sequence

def extract_sequence(list):
    """
    extract longest sequence from list of sequences
    Input: list with sequences
    Output: string of longest sequence
    """
    long_sequence = max(list,key=len)
    return long_sequence

def extract_subsequence(list):
    """
    extract sub/shortest sequence from list of sequences
    Input: list with sequences
    Output: string of subsequence
    """
    short_sequence = min(list,key=len)
    return short_sequence



def detect_position(long,sub):
    """
    detect position of sub sequence in sequence.
    Input: two sequence strings 1: long sequence 2: subsequence
    Output: list of the positions that subsequence is present in sequence
    Return position of subsequence in sequence
    """
    position_list =[]

    for nucl in range(len(long)):
        if long[nucl:nucl+len(sub_sequence)] == sub:
            position_list.append(nucl+1)
    return position_list

def join_list_int(list):
    """
    combine integers into 1 string separated by a space.
    """
    str_list = map(str,list)
    joined_string = ' '.join(str_list)
    return joined_string

def write_to_txt(string):
    text_file = open("answer.txt", "w")
    text_file.write(string)
    text_file.close()



def fibonacci_rabbit(n, k):
    adult = [None] * (n)
    young = [None] * (n)
    adult[0] = 0
    young[0] = 1
    adult[1] = 1
    young[1] = 0
    adult[2] = 1
    young[2] = 1


    if n == 1 or n == 2:
        return 1

    for month in range(3, n):
        if month >= k:
            adult[month] = adult[month-1] + young[month-1] - young[month-k]
        else:
            adult[month] = adult[month - 1] + young[month - 1]
        young[month] = adult[month-1]

    print(adult)
    print(young)
    total_rabbits = adult[month] + young[month]

    return total_rabbits


if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    fibonacci_numbers = sequences.split()
    fibonacci_numbers = list(map(int, fibonacci_numbers))
    print(fibonacci_numbers)
    rabbits = fibonacci_rabbit(fibonacci_numbers[0], fibonacci_numbers[1])
    print(rabbits)
    # write_to_txt(rabbits)
    # sequences = split_dataset(sequences)
    # long_sequence = extract_sequence(sequences)
    # sub_sequence = extract_subsequence(sequences)
    # position_list = detect_position(long_sequence,sub_sequence)
    # print(join_list_int(position_list))
