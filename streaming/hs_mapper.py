#!/usr/bin/python

import sys

def __mapper__(data, *args):
    fields = []

    for i in args:
        if i >= len(data):
            raise IndexError('Index value exceeds list size.')
        fields.append(data[i])
        
    return fields


"""
    Generic mapper function for Hadoop streaming.
    total_fields = Number of fields in the data
    *args = Index of the key and the value fields
"""
def mapper(total_fields, *args):
    for line in sys.stdin:
        data = line.strip().split('\t')
        
        if len(data) != total_fields: continue

        fields = __mapper__(data, *args)

        print '%s\t%s' % (fields[0], fields[1])

if __name__ == '__main__':
    mapper(6, 3, 4)
