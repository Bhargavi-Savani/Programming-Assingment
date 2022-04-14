import statistics
import pandas as pds 
a = pds.Series([10, 50, 80, 70, 49, 23, 11, 4]) 
mean = a.mean() 
median = a.median() 
mode = a.mode() 
range1 = a.max() - a.min(); 
stdeviation = a.std(axis=0, skipna=True) 
print(mean) 
print(median) 
print(mode) 
print(range1)
print(stdeviation)
print("The variance is %s" % (statistics.variance(a)))