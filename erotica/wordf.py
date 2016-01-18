#!/usr/bin/python2.7

import numpy as np
import os

def file_to_list(filename):
    with open(filename, "r") as f:
        return [line.strip(" \n") for line in f]

def list_to_dict(word_list):
    return {word: int(freq) for freq, word in [w.split(",") for w in word_list]}

def normalize(word_dict):
    sum_words = float(sum(v for __, v in word_dict.iteritems()))
    return {k: v/sum_words for k, v in word_dict.iteritems()}   

def compare(word_list, words_dict):
    diff = [w for w in word_list if not w in words_dict]
    words = dict((key, val) for key, val in words_dict.iteritems() \
                 if key in word_list)
    for w in diff:
        words[w] = 0.
    return words

def usage():
    print "wordf <base_file> <file_1> ... <filen>"

def filename(path):
    return os.path.basename(path).split(".")[0]

def main():
    import sys
    if len(sys.argv) < 3:
        usage()
        exit()

    base_file = file_to_list(sys.argv[1])
    files = sys.argv[2:]

    for f in files:
        print "in '%s' ..." % f
        word_list = file_to_list(f)
        word_dict = normalize(list_to_dict(word_list))
        freq = compare(base_file, word_dict)
        save_fn = os.path.join(os.path.dirname(f), filename(f)) + ".csv"

        with open(save_fn, "w") as freq_file:
            for w in base_file:
                freq_file.write("%.9f,%s\n" % (freq[w], w))
        
if __name__ == "__main__":
    main()
