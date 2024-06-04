from typing import Optional
from typing_extensions import Annotated

import json

import os

import typer
from openai import OpenAI

from jsonstore import *

def main(name: Annotated[Optional[str], typer.Argument()]=None):
    """
    test docstring, check using --help
    """

    tags = [
        "networking",
        "python",
        "java",
        "cybersecurity",
        "data",
        "system design",
        "deep learning",
        "web development",
    ]

    prompt = "prompt: " + name + "tags: " + str(tags)

    openai = OpenAI(
        api_key=os.getenv("CLAINOTE_API_KEY"),
        base_url=os.getenv("CLAINOTE_BASE_URL"),
    )

    chat_completion = openai.chat.completions.create(
        model="meta-llama/Meta-Llama-3-70B-Instruct",
        messages=[
            {
                "role": "system", 
                "content": 
                    """
                    Please respond to the following prompt with only a JSON 
                    object (no newlines) that contains 4 fields: title, short, long, and tags.

                    title should only be the topic discussed in the content.

                    short should be a rewritten form of the prompt with
                    any missing info added, and should be less than 100 words.

                    long should be a detailed technical summary of the topic,
                    emphasizing any features 
                    and may be up to 300 words.

                    tags should be chosen from the list provided based on 
                    relevance to the title and content.

                    Thank you!
                    """
            },
            {"role": "user", "content": prompt}
        ],
    )

    data = json.loads(chat_completion.choices[0].message.content)

    current_path = get_file_path()
    append_to_json_file(current_path, data)

    # print(data['title'])
    # print(data['tags'])
    # print(data['short'])
    # print(chat_completion.usage.prompt_tokens, chat_completion.usage.completion_tokens)
    # print(get_file_path())
    print("done")

if __name__ == "__main__":
    typer.run(main)
