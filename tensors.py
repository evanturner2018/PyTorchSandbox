# Try out tensors as a start
# https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
# "conda activate pytorchOne"
# "conda list" to see what packages are already there
# use "python" for the conda version of python

import torch
import numpy as np

data = [[1,2],[3,4]]
np_data = np.array(data)
tensor_data = torch.from_numpy(np_data)
print(tensor_data)