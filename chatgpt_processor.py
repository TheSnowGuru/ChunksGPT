# chatgpt_processor.py
import openai
import os
import concurrent.futures
from typing import Any, List

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Other functions and imports ...

def openai_request(messages):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.3,
        max_tokens=200,
        top_p=1.0,
    )

def dispatch_openai_requests(
    messages_list: List[List[dict[str, Any]]],
) -> List[str]:
    """Dispatches requests to OpenAI API concurrently.
    
    Args:
        messages_list: List of messages to be sent to OpenAI ChatCompletion API.
    Returns:
        List of responses from OpenAI API.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        responses = list(executor.map(openai_request, messages_list))
    return responses

def process_codebase_concurrently(code_sections: List[str]) -> List[str]:
    messages_list = [
        [{"role": "user", "content": f"Review this code snippet: {section}"}]
        for section in code_sections
    ]

    predictions = dispatch_openai_requests(messages_list)

    return [x['choices'][0]['message']['content'] for x in predictions]

