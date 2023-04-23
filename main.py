import os
import json
from code_divider import divide_codebase, load_codebase_from_url
from chatgpt_processor import process_codebase_concurrently, process_repo_insights
from results_integrator import integrate_results
from validation_testing import run_tests

# Load codebase from a GitHub repo URL
repo_url = "https://github.com/your_username/your_repo"
codebase = load_codebase_from_url(repo_url)

# Divide the codebase
code_sections = divide_codebase(codebase)

# Process the codebase concurrently with ChatGPT
chatgpt_responses = process_codebase_concurrently(code_sections)

# Integrate ChatGPT responses into the codebase
modified_codebase = integrate_results(code_sections, chatgpt_responses)

# Save the modified codebase to a new JSON file
with open("modified_codebase.json", "w") as f:
    json.dump(modified_codebase, f, indent=4)

# Run tests on the modified codebase
test_results = run_tests("modified_codebase.json")
print(test_results)

# Process repo insights
repo_digest = 'Example repo digestion summary'  # Replace this with the actual digestion summary
repo_insights = process_repo_insights(repo_digest)

# Save the repo insights to a new JSON file
with open("repo_insights.json", "w") as f:
    json.dump(repo_insights, f, indent=4)

# Print completion message and wait for user input
print("Done digesting your repo! You can submit your feature request.")
input("Press Enter to continue...")

# You can also include the other necessary functions and steps as needed.
