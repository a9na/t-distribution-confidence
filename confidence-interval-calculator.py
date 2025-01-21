# Import necessary libraries
from scipy.stats import t
import numpy as np

# Step 1: Define the sample data
sample = [3, 6, 4, 3, 3, 5, 5, 7, 2, 4, 5, 3]  # Sample data
n = len(sample)  # Sample size
confidence_level = 0.9763  # Confidence level

# Step 2: Calculate the sample mean
sample_mean = np.mean(sample)

# Step 3: Calculate the sample standard deviation
sample_std = np.std(sample, ddof=1)  # ddof=1 ensures this is the sample standard deviation

# Step 4: Calculate degrees of freedom
degrees_of_freedom = n - 1

# Step 5: Find the t-value for the given confidence level
alpha = 1 - confidence_level
t_value = t.ppf(1 - alpha / 2, degrees_of_freedom)  # Two-tailed t-value

# Step 6: Calculate the margin of error
margin_of_error = t_value * (sample_std / np.sqrt(n))

# Step 7: Determine the confidence interval
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Step 8: Print the results
print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_std)
print("Degrees of Freedom:", degrees_of_freedom)
print("t-Value:", t_value)
print("Margin of Error:", margin_of_error)
print("Confidence Interval:", confidence_interval)
