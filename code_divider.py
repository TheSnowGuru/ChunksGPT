import os

# Define the maximum token limit
MAX_TOKEN_LIMIT = 8000

# Define the path of the codebase directory
CODEBASE_DIR = "/path/to/codebase"

# Define the path of the directory where the divided codebase will be stored
DIVIDED_CODEBASE_DIR = "/path/to/divided/codebase"

# Create the directory to store the divided codebase if it doesn't exist
if not os.path.exists(DIVIDED_CODEBASE_DIR):
    os.makedirs(DIVIDED_CODEBASE_DIR)

# Iterate over the files in the codebase directory
for filename in os.listdir(CODEBASE_DIR):
    filepath = os.path.join(CODEBASE_DIR, filename)
    
    # Read the contents of the file
    with open(filepath, "r") as f:
        code = f.read()
    
    # Divide the code into smaller sections that remain within the token limit
    sections = []
    current_section = ""
    
    for line in code.split("\n"):
       
