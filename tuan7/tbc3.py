import numpy as np
X = np.array([[9, 8], [5, 4]])
print("Mean X = ", np.mean(X))
print("Mean X với axis = 0: ", np.mean(X, axis=0))
print("Mean X với axis = 1: ", np.mean(X, axis=1))
#mean x=6.5
#mean x voi axis = 0: [7. 6.]
#mean x voi axis = 1: [8.5 4.5]