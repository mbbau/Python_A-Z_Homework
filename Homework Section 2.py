# Law of large Numbers

import numpy as np
from numpy.random import randn

N = 10000
counter = 0

for i in randn(N):
    if(i < 1 and i > -1):
        counter = counter + 1

answer = counter/N
print(answer)


# the answer of the script was 0.6875 for the first run and 0.6837 for the second.