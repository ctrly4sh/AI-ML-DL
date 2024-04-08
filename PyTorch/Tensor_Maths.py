# Tensor maths and Comparison

import torch
import numpy as np

x = torch.tensor([1,2,3])
y = torch.tensor([4,5,6])

#addition
ADDITON = torch.add(x,y)
print("The Sum of the Tensors is : "  , ADDITON)

#Subtraction
SUBSTRACTION = torch.subtract(x,y) 
print("The Substractoin of the Tensors are : " , SUBSTRACTION)

#Division
DIVISION = torch.true_divide(x,y)
print("Division is " , DIVISION)

#inplace operation
t = torch.zeros(3)
t.add_(x) 


#Exponentiation
z = x.pow(2)
# or
z = x**2

#simple comaprison
z = x > 0
z = x < 0

#Matrix Multiplication
x1 = torch.rand((2,5))
x2 = torch.rand((5,3))

tensor_mult = torch.mm(x1,x2)

