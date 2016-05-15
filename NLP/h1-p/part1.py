# -*- coding: utf-8 -*-
"""
Created on Wed May 04 14:48:25 2016

@author: Leonspirit
"""

import sys

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
                gene = fields[2]
                types = fields[1]
                count = fields[0]
                
                #print "name " + name + " gen " + gene + " tipe " + types + " jumlah " + count
                yield count, types, gene, name
            #else: # Empty line
            #    yield (None, None, None, None)
            l = corpus_file.readline()
    except IndexError:
        sys.stderr.write("Could not read line: \n")
        sys.stderr.write("\n%s" % line)
        sys.exit(1)

def corpus_test(corpus_file):
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
                yield name
            else: # Empty line
                yield None
            l = corpus_file.readline()
    except IndexError:
        sys.stderr.write("Could not read line: \n")
        sys.stderr.write("\n%s" % line)
        sys.exit(1)
'''     
def corpus_ngram(corpus_file):
    """
    Get an iterator object over the corpus file. The elements of the
    iterator contain (word, ne_tag) tuples. Blank lines, indicating
    sentence boundaries return (None, None).
    """
    l = corpus_file.readline()    

    try:
        while l:
            line = l.strip()
            if line and line.split(" ")[1] == "1-GRAM": 
                fields = line.split(" ")
                cnt = fields[0]
                n1 = fields[2]
                yield cnt, n1
            elif line and line.split(" ")[1] == "2-GRAM":
                fields = line.split(" ")
                cnt = fields[0]
                n1 = fields[2]
                n2 = fields[3]
                yield cnt, n1, n2
            elif line and line.split(" ")[1] == "3-GRAM":
                fields = line.split(" ")
                cnt = fields[0]
                n1 = fields[2]
                n2 = fields[3]
                n3 = fields[4]
                yield cnt, n1, n2, n3
            #else: # Empty line
            #    yield (None, None, None, None)
            l = corpus_file.readline()
    except IndexError:
        sys.stderr.write("Could not read line: \n")
        sys.stderr.write("\n%s" % line)
        sys.exit(1)
'''
class Emission_Param(object):
    
    global classes 
    classes = ["O", "I-GENE"]
    global total 
    total = [0, 0]
    global counters
    counters = dict()
    global wordtag
    wordtag = dict()
    
    def __init__(self, check_corpus, wordtag_corpus):
        for count, name in check_corpus:
            if name in counters:
                counters[name] = counters[name] + int(count)
            else :
                counters[name] = int(count)
        
        for count, types, gene, name in wordtag_corpus:
            tuples = (name, gene)
            wordtag[tuples]= int(count)
            if gene == "O":
                total[0] = total[0] + int(count)
            else:
                total[1] = total[1] + int(count)
            #print "fuks " + name + " " + gene + " " + wordtag[(name, gene)]
        '''
        for arg in ngram_corpus:
            print "fukyu " + arg[0] + " tes " + arg[1]
        '''
    
    def test(self, test_corpus):
        for name in test_corpus:
            if name is not None:
                check_name = name
                if name in counters:
                    if counters[name] < 5:
                        check_name = "_RARE_"
                else:
                    check_name = "_RARE_"
                
                gene = (check_name, classes[1])
                obj = (check_name, classes[0])
                
                
                em = [0, 0]
                if obj in wordtag:
                    em[0] = float(wordtag[obj]) / float(total[0])
                if gene in wordtag:
                    em[1] = float(wordtag[gene]) / float(total[1])
                
                if em[0] > em[1]:
                    sys.stdout.write("%s %s\n" % (name, classes[0]))
                else:
                    sys.stdout.write("%s %s\n" % (name, classes[1]))
            else:
                sys.stdout.write("\n")
            
if __name__ == "__main__":
    
    check = corpus_check(file(sys.argv[1]))
    counter = corpus_count(file(sys.argv[2]))
    tests = corpus_test(file(sys.argv[3]))
    em_param = Emission_Param(check, counter)
    em_param.test(tests)