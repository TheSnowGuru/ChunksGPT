import timeit
import pycallgraph
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from code_divider import divide_codebase
from code_summarizer import summarize_code
from chatgpt_processor import process_code_with_chatgpt
from results_integrator import integrate_results
from validation_testing import validate_and_test

def main():
    repo_url = "https://github.com/user/repo_name"
    codebase = load_codebase_from_url(repo_url)
    
    # Time the iteration of the codebase
    start_time = timeit.default_timer()
    
    modules = divide_codebase(codebase)
    summaries = [summarize_code(module) for module in modules]
    
    processed_modules = [
        process_code_with_chatgpt(module, summary)
        for module, summary in zip(modules, summaries)
    ]
    
    new_codebase = integrate_results(processed_modules)
    
    with open(f"{repo_url.split('/')[-1]}_suggestions.md", "w") as f:
        f.write(new_codebase)

    end_time = timeit.default_timer()
    print(f"Time taken: {end_time - start_time} seconds")

    # Generate codebase visualization
    with PyCallGraph(output=GraphvizOutput()):
        validate_and_test(new_codebase)

    # Save code structure in DOT language schema
    pycallgraph.Config(include_stdlib=True)
    graphviz = GraphvizOutput(output_file='code_structure.dot')
    graphviz.done()

if __name__ == "__main__":
    main()
