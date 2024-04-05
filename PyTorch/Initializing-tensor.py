'''
 What is a tensor ?
 Tensor is a imperative n-dimensional array that runs on a GPU(often)
'''

#Initilizing first tensor
import torch 

DEVICE="cuda" if torch.cuda.is_available() else "cpu"
first_tensor = torch.tensor([[1,2,3],[4,5,6]], device=DEVICE , dtype=torch.float32 , requires_grad=True)

#details of the tensor

print(first_tensor) #tensor
print(first_tensor.dtype) # type of the tensor
print(first_tensor.device) #device of the tensor CPU || CUDA(GPU)
print(first_tensor.shape) #shape of the tensor
print(first_tensor.requires_grad) #does the tensor required grqdiant or not


#Other comman initializing methods
