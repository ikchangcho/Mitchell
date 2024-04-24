import scipy.io
import pandas as pd
import numpy as np

# Load the .mat file
mat_contents = scipy.io.loadmat('muscleNucleiStripes.mat')
#field_name = list(mat_contents.keys())[3]  # Adjust the index as needed, usually the first field after '__header__', '__version__', and '__globals__'
data = mat_contents['dat']

for i in range(60):
    for str in ['v', 'f', 'vn', 'u', 'avgpts_um', 'radius_um']:
        meshdata = data[i][0]['mesh'][0][0][str][0][0]
        np.savetxt(f'mesh_{str}_time{i+1}.csv', meshdata, delimiter=',')

# # Check what are the inside
# # Access the first structure (for example)
# first_struct = dat[0, 0]
#
# # Iterate through the fields and print the data
# fields = ['mesh', 'curv1', 'curv2', 'curv3', 'curv4']
# for field in fields:
#     value = first_struct[field][0, 0]  # Accessing the field value
#     print(f"Field: {field}")
#     print(f"  Type: {type(value)}")
#     print(f"  Array shape: {value.shape}")
#
#     # Print the entire array if it's small or a part of it if it's large
#     if value.size <= 10:  # Adjust this threshold as necessary
#         print(f"  Data: {value}")
#     else:
#         print(f"  Data (first 5 elements): {value[:5]}")
#     print()  # Add an empty line for better readability


# # Convert curv data to csv files
# # Load the .mat file
# mat_contents = scipy.io.loadmat('muscleNucleiStripes.mat')
# dat = mat_contents['dat']
#
# # Iterate over each structure in 'dat'
# for i in range(dat.shape[0]):  # Loop through the 60 structures
#     struct = dat[i, 0]  # Access each structure
#
#     # Iterate over the curvature fields
#     for curv in ['curv1', 'curv2', 'curv3', 'curv4']:
#         # Extract the data from the current field
#         data = struct[curv][0, 0]  # Accessing the field value
#
#         # Ensure the data is in a 2D array form for DataFrame conversion
#         if data.ndim == 1:
#             data = np.expand_dims(data, axis=1)
#
#         # Convert the data to a DataFrame
#         df = pd.DataFrame(data)
#
#         # Define the file name
#         file_name = f'structure_{i + 1}_{curv}.csv'
#
#         # Save the DataFrame to a CSV file
#         df.to_csv(file_name, index=False)
#         print(f'Saved {file_name}')