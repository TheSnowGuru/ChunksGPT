# ChunksGPT - Codebase Refactoring Assistant

This project aims to assist developers with refactoring and improving their codebases using OpenAI's ChatGPT. The goal is to create a collaborative environment where the community can contribute, enhance, and build upon the codebase refactoring process.

## Overview

The Codebase Refactoring Assistant divides a codebase into smaller modules, generates summaries for each module, processes the modules iteratively with ChatGPT, integrates the insights and suggestions provided by ChatGPT back into the codebase, and validates and tests the modified codebase to ensure it works as intended.

## Features

- Load codebase from a GitHub repository URL
- Divide the codebase into smaller modules within ChatGPT's token limit
- Generate summaries for each module to provide context to ChatGPT
- Process each module with ChatGPT and validate the output
- Integrate the results back into the codebase
- Validate and test the modified codebase using Python's unittest framework

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/codebase-refactoring-assistant.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable:

   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

4. Update `main.py` with the GitHub URL of your code file.

5. Run `main.py`:

   ```
   python main.py
   ```

6. Run the unittests in `validation_testing.py`:

   ```
   python validation_testing.py
   ```

## Contributing

We welcome contributions from the community to improve and expand the Codebase Refactoring Assistant. If you're interested in contributing, please feel free to submit a pull request or open an issue to discuss your ideas.

### Ideas for Improvement

- Improve code summarization techniques
- Add support for more programming languages
- Enhance validation and testing capabilities
- Optimize and improve the ChatGPT integration process
- Implement a user-friendly interface or integrate with popular code editors

## License

This project is released under the [MIT License](LICENSE).

## Acknowledgements

This project is built using OpenAI's ChatGPT API. We would like to thank the OpenAI team for providing an amazing AI language model, and we appreciate the support and contributions from the community in helping to improve this project.
