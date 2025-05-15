import openai 
from openai import OpenAI
from loguru import logger
from prompts import prompt_template
import os 
openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_context(chunk):
    client = OpenAI()

    prompt = prompt_template.format(chunk=chunk)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
def all_chunks_context(chunks):
    for c in chunks:
        c_context=generate_context(c)
        c["text"]=c_context+c["text"]
        logger.debug("contextual retrival done")
    
    