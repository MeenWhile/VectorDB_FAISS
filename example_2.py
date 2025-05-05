# region Prepare data

import os

# Read data from .txt file
def read_bugs_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # แยกข้อมูล bug แต่ละตัว
    bugs = content.split("\n")
    return bugs

# Get bug report
filename = os.path.join("data","dataset_test_user_feedback.txt")
bugs_data = read_bugs_from_file(filename)

# -----------------------------------------------------------------------------------------------------------------------------------------
# region FAISS

from src.FAISS import FAISS

# Setup FAISS Class
vectorDB = FAISS()

filename = os.path.join("src","faiss_data","user_feedback")

# Add data to VectorDB
vectorDB.insert(bugs_data, filename = filename)

# Search query from VectorDB
result = vectorDB.search("What did users say about the search bar?", filename = filename, k = 3)

# Show result
print(result)

# -----------------------------------------------------------------------------------------------------------------------------------------

