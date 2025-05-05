# region Prepare data

import os

# Read data from .txt file
def read_bugs_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split data
    bugs = content.split("\n\n")
    return bugs

# Get bug report
filename = os.path.join("data","dataset_test_bug_report.txt")
bugs_data = read_bugs_from_file(filename)

# -----------------------------------------------------------------------------------------------------------------------------------------
# region FAISS

from src.FAISS import FAISS

# Setup FAISS Class
vectorDB = FAISS()

filename = os.path.join("src","faiss_data","bug_report")

# Add data to VectorDB
vectorDB.insert(bugs_data, filename = filename)

# Search query from VectorDB
result = vectorDB.search("What are the issues reported on email notification?", filename = filename, k = 3)

# Show result
print(result)

# -----------------------------------------------------------------------------------------------------------------------------------------

