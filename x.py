import numpy as np

matrica = np.arange(2,1000)
res = matrica[(matrica ** 0.5) % 1 == 0].reshape(6,5)
print(res)
