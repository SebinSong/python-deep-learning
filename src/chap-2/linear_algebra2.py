import torch

t1 = torch.arange(30).reshape(3, 5, 2).to(torch.float32)
mean = t1.mean()

# tensor.sum() returns a 0-dim tensor, tensor.numel() is a scalar (python int type)
mean_manual = t1.sum() / t1.numel()

### Vector Norm

# 1. Euclidian norm, L2 Norm
t2 = torch.tensor([3, 4]).to(torch.float32)
norm_t2 = t2.norm()

# 2. L1 Norm
t3 = torch.tensor((-1, 3, -5, 4.5)).to(torch.float32)
norm_t3 = torch.abs(t3).sum()
print(norm_t3)
