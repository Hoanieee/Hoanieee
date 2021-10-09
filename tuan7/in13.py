import numpy as ab
a = ab.array([1, ab.nan, 3, 4])
print("var = ", ab.var(a))
print("std = ", ab.std(a))
print("nanvar = ", ab.nanvar(a))
print("nanstd = ", ab.nanstd(a))