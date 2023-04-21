import re

# Constants
TOKEN_LIMIT = 8000

# Function to divide codebase into manageable sections
def divide_codebase(codebase):
    sections = []
    current_section = ""
    token_count = 0
    
    # Split codebase into lines
    lines = codebase.split("\n")
    
    for line in lines:
        # Check if line exceeds token limit
        if len(line) > TOKEN_LIMIT:
            print(f"Error: Line exceeds token limit ({len(line)} > {TOKEN_LIMIT})")
            return None
        
        # Check if adding line will exceed token limit
        if token_count + len(line) > TOKEN_LIMIT:
            sections.append(current_section)
            current_section = ""
            token_count = 0
        
        current_section += line + "\n"
        token_count += len(line)
    
    # Add last section to list
    sections.append(current_section)
    
    return sections

# Function to summarize code section
def summarize_section(section):
    # Split section into lines
    lines = section.split
