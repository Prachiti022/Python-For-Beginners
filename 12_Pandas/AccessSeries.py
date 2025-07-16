import pandas as pd
import numpy as np

# Creating simple array
data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'])

# Create Series
ser = pd.Series(data)

# Retrieve first 5 elements
print(ser[:5])
