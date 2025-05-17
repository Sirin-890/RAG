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
prompt2="a"
QUE_ANS_AGENT_TASK = {
    "description": "Answer the question `{}` based solely on the provided context `{}`. If the answer cannot be determined from the context, respond with a polite and direct message indicating that the information is unavailable. Do not ask for additional input or clarify the question.",
    "expected_output": "The response should directly address the user's question using the context. If the answer cannot be found, state this clearly and avoid asking the user for further inputs."
}