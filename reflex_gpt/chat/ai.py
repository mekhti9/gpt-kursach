from decouple import config
from openai import OpenAI

OPENAI_API_KEY=config("OPENAI_API_KEY", cast=str, default=None)
OPENAI_MODEL="gpt-4o-mini"

def get_clent():
    return OpenAI(api_key=OPENAI_API_KEY)

def get_llm_response(gpt_messages):
    client = get_clent()
    completion = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=gpt_messages
    )
    return completion.choices[0].message.content
