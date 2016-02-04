## Streaming utilities for Hadoop 2.x

### Generic python based mapper & reducer for hadoop streaming
**For a given key calculates the following for the value: running total, average, count, min & max**  

**Files**  
1. hs_mapper.py  
2. hs_reducer.py

**Assumptions**  
1. Tab separated records  
2. Tested with Python 2.7.6, Hadoop 2.7.1  

**Example**  
*Data Fields*  
location, branch_name, branch_code, staff_strength  
*Data Sample*  
Kolkata\tChowringhee Road\tSBT000897\t233  
Kolkata\tBowbazar\tSBT000076\t198  

If we wish to investigation the *staff_strength* per *branch_name*, then **key=branch_name** and **value=staff_strength**.  
So we need to call mapper(4, 1, 3) where total number of fields are 4, and *key* index in the record is 1 and *value* index is 3.  

**hs_mapper.py**  
Generic mapper function for Hadoop streaming.  
*Arguments*  
1. total_fields = Number of fields in the data  
2. *args = Indexes of the key and the value fields  

**hs_reducer.py**  
Generic reducer function for Hadoop streaming. Computes the running total, average, max, min and count for each key.  



