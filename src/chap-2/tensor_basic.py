import torch

# 1. multiple ways of creating tensors
x1 = torch.arange(0, 12, 1)
reshaped_x1 = x1.reshape(3, 4)
x2 = torch.ones(3, 4) # torch.zeros()
x3 = torch.zeros_like(x1)
x4 = torch.tensor([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]) * 2

# 2. concatenation / stacking
concat1 = torch.cat((reshaped_x1, x4), dim=0)
concat2 = torch.cat((reshaped_x1, x4), dim=1)
stack1 = torch.stack([reshaped_x1, x4], dim=2)

# 3. summing all elements of a tensor
sum_x4 = x4.sum()
print(float(sum_x4))

# 4. To a numpy ndarray / vise versa
np1 = x4.numpy()
back1 = torch.from_numpy(np1)

# 5. In memory position ID
id1 = id(x4)

# 6. in-place operation saves extra memory usage.
reshaped_x1 += x4
reshaped_x1[:] = reshaped_x1 + x4

# 7. Getting a scalar value
t1 = torch.tensor([100])
scalar1 = t1.item() # or int(t1), float(t1)

# 8. tensor broadcasting
# https://numpy.org/doc/stable/user/basics.broadcasting.html
a = torch.ones(3, 4) * 5
b = torch.tensor([1, 0, 1, 0])
c = a + b # b is expanded to 3 * 4 2D tensors and then the plus operation

