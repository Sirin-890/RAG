# # import openai 
# # from openai import OpenAI
# # from loguru import logger
# # from prompts import prompt_template
# # import os 
# # openai.api_key = os.getenv("OPENAI_API_KEY")
# # def generate_context(chunk):
# #     client = OpenAI()

# #     prompt = prompt_template.format(chunk=chunk)
# #     response = client.chat.completions.create(
# #         model="gpt-4",
# #         messages=[{"role": "user", "content": prompt}]
# #     )
# #     return response.choices[0].message.content
# # def all_chunks_context(chunks):
# #     for c in chunks:
# #         c_context=generate_context(c)
# #         c["text"]=c_context+c["text"]
# #         logger.debug("contextual retrival done")
    
    
# import os, asyncio
# from openai import OpenAI  # in v0.27+ this also exposes AsyncOpenAI
# from loguru import logger
# from prompts import prompt_template

# API_KEY = os.getenv("OPENAI_API_KEY")
# async_client = OpenAI()

# async def generate_context_async(chunk):
#     prompt = prompt_template.format(chunk=chunk)
#     resp = await async_client.chat.completions.acreate(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}],
#         api_key=API_KEY
#     )
#     return resp.choices[0].message.content

# async def all_chunks_context_async(chunks):
#     tasks = []
#     for c in chunks:
#         tasks.append(asyncio.create_task(generate_context_async(c)))
#     results = await asyncio.gather(*tasks, return_exceptions=True)

#     for c, res in zip(chunks, results):
#         if isinstance(res, Exception):
#             logger.error(f"chunk {c.get('id','?')} failed: {res}")
#         else:
#             c["text"] = res + c["text"]
#             logger.debug(f"contextual retrieval done for chunk {c.get('id','?')}")

# from openai import AsyncOpenAI
# import os, asyncio
# from loguru import logger
# from prompts import prompt_template
# import somewhere

# client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# async def generate_context_async(chunk):
#     prompt = prompt_template.format(chunk=chunk)
#     # note: use client.chat.completions.create (async) on the AsyncOpenAI
#     resp = await client.chat.completions.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}],
#     )
#     return resp.choices[0].message.content

# async def all_chunks_context_async(chunks):
#     tasks = [asyncio.create_task(generate_context_async(c)) for c in chunks]
#     results = await asyncio.gather(*tasks, return_exceptions=True)
#     for c, res in zip(chunks, results):
#         if isinstance(res, Exception):
#             logger.error(f"[chunk {c.get('id','?')}] failed: {res}")
#         else:
#             c["text"] = res + c["text"]
#             logger.debug(f"[chunk {c.get('id','?')}] done")

# if __name__ == "__main__":
#     pass


import openai
from openai import OpenAI
from loguru import logger
from src.prompts import prompt_template
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def generate_context(chunk):
    prompt = prompt_template.format(chunk=chunk)
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content

def all_chunks_context(chunks, max_workers=8):
    # dispatch all jobs to the thread pool
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(generate_context, c): c for c in chunks}
        for fut in as_completed(futures):
            c = futures[fut]
            try:
                ctx = fut.result()
                c["text"] = ctx + c["text"]
                logger.debug(f"contextual retrieval done for chunk {c.get('id','?')}")
            except Exception as e:
                logger.error(f"chunk {c.get('id','?')} failed: {e}")

# usage
