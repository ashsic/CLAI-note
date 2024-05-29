from typing import Optional
from typing_extensions import Annotated

import os

import typer
from openai import OpenAI


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
        "deep learning"
    ]

    prompt = "prompt: " + name + "tags: " + str(tags)

    openai = OpenAI(
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )

    chat_completion = openai.chat.completions.create(
        model="meta-llama/Meta-Llama-3-70B-Instruct",
        messages=[
            {
                "role": "system", 
                "content": 
                    """
                    Please respond to the following prompt with only a JSON 
                    object that contains 4 fields: title, short, long, and tags.

                    title should only be the topic discussed in the content.

                    short should be a rewritten form of the prompt with
                    any missing info added, and should be less than 100 words.

                    long should be a detailed technical summary of the topic
                    and may be up to 300 words.

                    tags should be chosen from the list provided based on 
                    relevance to the title and content.

                    Thank you!
                    """
            },
            {"role": "user", "content": prompt}
        ],
    )

    print(chat_completion.choices[0].message.content)
    print(chat_completion.usage.prompt_tokens, chat_completion.usage.completion_tokens)


if __name__ == "__main__":
    typer.run(main)
