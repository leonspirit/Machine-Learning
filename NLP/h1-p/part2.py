# -*- coding: utf-8 -*-
"""
Created on Thu May 05 14:53:44 2016

@author: Leonspirit
"""

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
        
