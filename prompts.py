prompt_template = (
    "Given this chunk from a document:\n\n"
    "{chunk}\n\n"
    "Generate a brief summary or surrounding context (50–100 tokens) that helps situate it within the full document."
)
system_prompt = (
    "You are a knowledgeable assistant. "
    "Answer the user's question using the provided context. "
    "If the answer is not in the context, say 'I don't know' instead of making something up."
)