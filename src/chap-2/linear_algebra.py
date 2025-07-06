import torch

def float_and_print (*args):
  print(*(float(arg) for arg in args), sep=', ')

# Scalar is represented by a tensor with just one element.
s1 = torch.tensor(3.0)
s2 = torch.tensor(2.0)

float_and_print(
  s1 + s2,
  s1 * s2,
  s1 / s2,
  s1**s2
)

# Vector is simply a list of scalar values and is represented by a one-dimensional tensor.
v1 = torch.arange(2, 30, 3)
v2 = torch.tensor([5, 15, 0.25, 100.25]) # can also be generated using an iterable. eg) a list

# Creating a matrix
m1 = torch.ones(5, 7)

# Assignments to a certain range of a matrix
m1[1:5, 2:6] = 5

# extracting sub-matrix from a matrix
m1_sub = m1[1:4, :5]

# Flipping a matrix (Transpose of a matrix)
m1_sub_flipped = m1_sub.T
is_true = bool(m1_sub_flipped[1][2] == m1_sub[2][1])

# Binary operations on two tensors (with the same shape
t1 = torch.arange(2, 41, 2).reshape(4, 5)

t2 = t1[:] # Also can be done using t1.clone()

# Arithmetic operation on two tensors are done element-wise.
t3 = t1 + t2
t4 = t1 - t2 # All elements of t4 here are 0 as t2 is the clone of t1.

t4 += 5

# Updating the dtype of an existing tensor.
t4 = t4.to(dtype=torch.float32)
t4 /= 3

# summing up all elements of a tensor: .sum() method
t5 = torch.arange(50).reshape(2,5,5)
print(t5)
sum = t5.sum(axis=0)
print('sum:', sum)
