import openai

# Set up OpenAI API credentials
openai.api_key = "your_openai_api_key"

def process_code_module(module, summary, token_limit=8000):
    """
    Process a code module with ChatGPT, providing the summary and relevant code snippets within the token limit.
    """
    prompt = f"{summary}\n\n{module}"
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=token_limit,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
