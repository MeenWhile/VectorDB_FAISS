# Setup
1. Create Virtual Environment
```bash
virtualvenv venv
```
2. Use Virtual Environment
```bash
venv\Scripts\activate
```
3. Install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```
4. Create .env file and add your OPENAI_API_KEY:
```text
OPENAI_API_KEY=your-api-key-here
```

# Use

## Setup FAISS Class
```python
from src.FAISS import FAISS  # or from FAISS import FAISS if same folder
vectorDB = FAISS()
```

## Add data to VectorDB
```python
vectorDB.insert(data_list, filename = "your_desired_filename")
```

## Search query from VectorDB
```python
result = vectorDB.search(
    query = "your_query_here",
    filename = "your_desired_filename",
    k = 3 # number of results to retrieve
)
print(result)
```