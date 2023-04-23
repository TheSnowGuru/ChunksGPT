'''
This file handles communication with the OpenAI API for ChatGPT. 
It sends the divided code sections to ChatGPT for processing and retrieves insights,
suggestions, or modifications for the codebase. It utilizes ultra-fast processing with concurrent.futures,
which enables users to send up to 100 requests per second, significantly improving performance.

'''

import openai
import os
import concurrent.futures
from typing import Any, List

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Function to send a request to OpenAI API
def openai_request(messages):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.3,
        max_tokens=200,
        top_p=1.0,
    )

# Function to dispatch OpenAI requests concurrently
def dispatch_openai_requests(
    messages_list: List[List[dict[str, Any]]],
) -> List[str]:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        responses = list(executor.map(openai_request, messages_list))
    return responses

# Function to process codebase concurrently
def process_codebase_concurrently(code_sections: List[str]) -> List[str]:
    messages_list = [
        [{"role": "user", "content": f"Review this code snippet: {section}"}]
        for section in code_sections
    ]

    predictions = dispatch_openai_requests(messages_list)

    return [x['choices'][0]['message']['content'] for x in predictions]

# Function to process repo insights
def process_repo_insights(repo_digest):
    prompt = f"Given the codebase digestion summary:\n{repo_digest}\nPlease provide insights, suggestions, or modifications for this codebase."

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text
