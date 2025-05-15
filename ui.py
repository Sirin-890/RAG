import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/ask"

def call_rag_api(user_input, history):
    try:
        res = requests.post(API_URL, json={"question": user_input})
        data = res.json()
        answer = data["answer"]
        chunks = data["chunks"]

        # Combine both answer and source chunk list
        full_response = f"{answer}\n\n📄 **Top Matching Chunks:**\n{chunks}"
        history.append((user_input, full_response))
        return "", history
    except Exception as e:
        history.append((user_input, f"❌ Error: {e}"))
        return "", history

with gr.Blocks(title="🧠 LSTM RAG Chatbot") as demo:
    gr.Markdown("# 📘 Ask Me Anything about LSTMs")
    chatbot = gr.Chatbot(label="LSTM Assistant")
    user_input = gr.Textbox(show_label=False, placeholder="Ask a question about LSTMs...", scale=7)
    send_btn = gr.Button("Send", scale=1)
    clear_btn = gr.Button("🧹 Clear Chat")

    send_btn.click(call_rag_api, [user_input, chatbot], [user_input, chatbot])
    user_input.submit(call_rag_api, [user_input, chatbot], [user_input, chatbot])
    clear_btn.click(lambda: ([], ""), None, [chatbot, user_input])

demo.launch()
