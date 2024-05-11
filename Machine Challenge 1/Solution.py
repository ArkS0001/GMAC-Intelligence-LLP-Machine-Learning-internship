import torch

# __define-ocg__ Creating tensors and performing operations
varOcg_ones = torch.ones(3, 3)  # Creating a 3x3 tensor filled with ones
varOcg_zeros = torch.zeros(3, 3)  # Creating a 3x3 tensor filled with zeros

result_tensor = varOcg_ones * varOcg_zeros  # Element-wise multiplication
print("Resulting tensor after element-wise multiplication:", result_tensor)

result_tensor += 5  # Adding scalar value of 5
print("Resulting tensor after adding scalar value of 5:", result_tensor)

mean = result_tensor.mean().item()  # Computing mean
std_dev = result_tensor.std().item()  # Computing standard deviation
print("Mean of final tensor:", mean)
print("Standard deviation of final tensor:", std_dev)

reshaped_list = result_tensor.tolist()  # Converting final tensor to a Python list
print(reshaped_list)
