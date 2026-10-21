import os #used for interacting with the os including environment
#variables and filesystem operations
from pathlib import Path #imports the python class from python's 
#built-in pathlib module

#this line finds the project root from this file's location so the
#code works no matter which folder you run it from.
#_file_ identifies model file path, path(_file) converts that path into
#a path object so you can manipulate it conveniently
#resolves the path into an absolute path, making it easier to work with
#the first parent moves up the hybridrag directory to the project roo.
#the second parent moves it up one more level.
root = Path(__file__).resolve().parent.parent
#/'data' appends a folder named data to the root path and stores it 
#in data_dir
data_dir = root / 'data'
# creates a path to a subdirectory named index. 
index_dir = data_dir / 'index'
# this points to results directory of project root. 
results_dir = root / 'results'

#stores url to download dataset
scifact_url = 'https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/scifact.zip'
#BGE small english embedding model
embed_model = 'BAAI/bge-small-en-v1.5'
rerank_model = 'Xenova/ms-marco-MiniLM-6-v2'
llm_model = os.getenv('HR_model', 'qwen2.5:3b')

for p in (data_dir, index_dir, results_dir):
    p.mkdir(parents=True, exist_ok=True)