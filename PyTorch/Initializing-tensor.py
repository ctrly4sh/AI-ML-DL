#Initilizing first tensor

'''
 What are tensors ?
 Tensors are imperative n-dimensional array that runs on a GPU(often),
 Tensors are use to encode the inputs and outputs of a model as well as the model's parameters. 
'''

import torch
import numpy

DEVICE="cuda" if torch.cuda.is_available() else "cpu"
first_tensor = torch.tensor([[1,2,3],[4,5,6]], device=DEVICE , dtype=torch.float32 , requires_grad=True)

#details of the tensor

def tensor_details(tensor_name):
    print(tensor_name) #tensor
    print(tensor_name.dtype) # type of the tensor
    print(tensor_name.device) #device of the tensor CPU || CUDA(GPU)
    print(tensor_name.shape) #shape of the tensor
    print(tensor_name.requires_grad) #does the tensor required gradiant or not

tensor_details(first_tensor)

#way to initialize a tensor using simple array 

T_array = [[11,22,33],[44,55,66]]
tensor_array = torch.tensor(T_array)
print(tensor_array)


#using numpy array

n_array = numpy.array([[111,222,333],[444,555,666]])
tensor_numpy = torch.from_numpy(n_array)
print(tensor_numpy)