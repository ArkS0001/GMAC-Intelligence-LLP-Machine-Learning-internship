import torch

# __define-ocg__ Reshaping and calculating statistics
varOcg = torch.tensor(list(range(1, 11)), dtype=torch.float32)  # Creating a 1D tensor of size 10 with values from 1 to 10
reshaped_tensor = varOcg.reshape(2, 5)  # Reshaping to a 2D tensor of size 2x5
mean = reshaped_tensor.mean().item()  # Computing mean
std_dev = reshaped_tensor.std().item()  # Computing standard deviation

print("Mean of reshaped tensor:", mean)
print("Standard deviation of reshaped tensor:", std_dev)

reshaped_list = reshaped_tensor.tolist()  # Converting reshaped tensor to a Python list
print(reshaped_list)
