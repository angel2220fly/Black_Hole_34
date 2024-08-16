import os
import subprocess
import glob
from datetime import datetime

# Define the paths to the Python scripts and the expected output .b files
script_a = "Black_Hole_34.A.py"
script_b = "Black_Hole_34.py"
script_c = "Black_Hole_34.B.py"  # Script to check
output_file_a = "output_A.b"
output_file_b = "output_B.b"
output_file_c = "output_C.b"  # Expected output of the new script

# Function to check if a file exists and get its size
def get_file_size(filepath):
    if os.path.exists(filepath):
        return os.path.getsize(filepath)
    else:
        return None

# Check if script C exists
if not os.path.exists(script_c):
    print(f"{script_c} does not exist. Exiting the program.")
    exit()  # Exit if script C does not exist

# Run all scripts
subprocess.run(["python3", script_a])
subprocess.run(["python3", script_b])
subprocess.run(["python3", script_c])

# Get file sizes after the scripts are run
size_a = get_file_size(output_file_a)
size_b = get_file_size(output_file_b)
size_c = get_file_size(output_file_c)

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')

# Find all .b files created today
b_files = []
for file in glob.glob("*.b"):
    file_creation_date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d')
    if file_creation_date == current_date:
        b_files.append(file)

# Initialize the smallest file size and name
smallest_file = None
smallest_size = float('inf')

# Compare sizes and find the smallest file
for file in b_files:
    size = get_file_size(file)
    if size is not None and size < smallest_size:
        smallest_size = size
        smallest_file = file

# Rename the smallest file to 'best_file.b' and delete other .b files
if smallest_file:
    # Rename the smallest file to 'best_file.b'
    new_name = "best_file.b"
    os.rename(smallest_file, new_name)
    print(f"The best file is {smallest_file}, renamed to {new_name} with size {smallest_size} bytes.")
    
    # Delete all other .b files
    for file in b_files:
        if file != new_name:
            os.remove(file)
            print(f"Deleted file: {file}")

else:
    print("No valid .b files found for today's date.")