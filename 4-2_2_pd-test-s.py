import pandas as pd, numpy as np
a = [1.0, 3.0, 5.0, 7.0, 9.0]
s = pd.Series(a)
print(s)
x = pd.DataFrame(a)
print(x)
print(s.shape) 