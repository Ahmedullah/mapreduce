#!/usr/bin/python

import sys

def reducer():
    old_key = None
    cnt = 0
    value_list = []
    
    for line in sys.stdin:
        data = line.strip().split('\t')

        # expecting a key-value pair
        if len(data) != 2: continue
        
        new_key, value = data

        f_value = float(value)

        # if value is zero ignore the record
        if f_value == 0: continue

        if old_key != None and old_key != new_key:
            printline(old_key, cnt, value_list)
            cnt = 0
            del value_list[:]
                                              

        value_list.append(f_value)
        old_key = new_key
        cnt += 1
        
    # for the last record...
    if old_key != None: printline(old_key, cnt, value_list)

def printline(key, cnt, value_list):
    total = sum(x for x in value_list)
    print '%s\t%s\t%s\t%s\t%s\t%s' % (key, cnt, total, total/cnt,
                                      max(x for x in value_list),
                                      min(x for x in value_list))

    
if __name__ == '__main__':
    reducer()
