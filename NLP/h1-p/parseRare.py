# -*- coding: utf-8 -*-
"""
Created on Thu May 05 08:57:55 2016

@author: Leonspirit
"""

import sys

def corpus_count(corpus_file):
    """
    Get an iterator object over the corpus file. The elements of the
    iterator contain (word, ne_tag) tuples. Blank lines, indicating
    sentence boundaries return (None, None).
    """
    l = corpus_file.readline()    

    try:
        while l:
            line = l.strip()
            if line and line.split(" ")[1] == "WORDTAG":
                fields = line.split(" ")
                name = fields[3]
                count = fields[0]
                
                #print "name " + name + " gen " + gene + " tipe " + types + " jumlah " + count
                yield count, name
            #else: # Empty line
            #    yield (None, None, None, None)
            l = corpus_file.readline()
    except IndexError:
        sys.stderr.write("Could not read line: \n")
        sys.stderr.write("\n%s" % line)
        sys.exit(1)
        
def corpus_check(corpus_file):
    """
    Get an iterator object over the corpus file. The elements of the
    iterator contain (word, ne_tag) tuples. Blank lines, indicating
    sentence boundaries return (None, None).
    """
    l = corpus_file.readline()    

    try:
        while l:
            line = l.strip()
            if line:
                fields = line.split(" ")
                name = fields[0]
                types = fields[1]
                
                yield name, types
            #else: # Empty line
            #    yield (None, None, None, None)
            l = corpus_file.readline()
    except IndexError:
        sys.stderr.write("Could not read line: \n")
        sys.stderr.write("\n%s" % line)
        sys.exit(1)
        
class operations(object):
    
    global counters
    counters = dict()
    
    def __init__(self, count_corpus):
        for count, name in count_corpus:
            if name in counters:
                counters[name] = counters[name] + int(count)
            else :
                counters[name] = int(count)
            
    def compute(self, check_corpus, outfile):
        for name, types in check_corpus:
            if counters[name] < 5:
                outfile.write("_RARE_ %s\n" % (types))
            else:
                outfile.write("%s %s\n" % (name, types))        
        
        
if __name__ == "__main__":
    
    counter = corpus_count(file(sys.argv[1]))
    train_data = corpus_check(file(sys.argv[2]))
    op = operations(counter)
    op.compute(train_data, sys.stdout)