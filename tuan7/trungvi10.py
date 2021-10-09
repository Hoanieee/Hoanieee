import numpy as ab
x = ab.array([2, ab.nan, 5, 9])
print("mean = ", ab.nanmean(x))
print("median = ", ab.nanmedian(x))