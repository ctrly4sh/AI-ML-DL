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

#Matrix exponentiation
matrix_exp = torch.rand(5,5)
print(matrix_exp.matrix_power(3))

#Element wise multplication

'''
x = 1,2,3
y = 4,5,6
1 x 4 = 2
2 x 5 = 10
3 x 6 = 18
'''

z = x * y
print(z)

#Dot product -> Muliplication and summation of all the elements of the product
dot_product = torch.dot(x,y)
print(dot_product)

#Batch matrix Multiplication
batch = 32
n = 10
m = 20
p = 30

#BroadCasting -> Expands to perform the Mathematical operation legally
x1 = torch.rand((5,5))
x2 = torch.rand((1,5))

z = x1 - x2
z = x1 + x2

#other operations
sum_x = torch.sum(x , )

