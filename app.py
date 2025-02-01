import google.generativeai as genai
import gradio as gr
import os

# Load API Key securely from Hugging Face Secrets
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ ERROR: GOOGLE_API_KEY is not set in Repository Secrets!")

genai.configure(api_key=api_key)

# Load Gemini AI model
# 1. gemini-pro: text-based tasks
# 2. gemini-pro-vision: Image-based reasoning, visual question answering
# 3. gemini-nano:  Lightweight & optimized for mobile devices
model = genai.GenerativeModel("gemini-pro")

def chatbot_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Gradio Chatbot UI
iface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Hey! What’s on your mind?", label="Your Message"),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="🤖 Intelligent Chat Assistant",
    description="Chatbot is designed to provide helpful responses using Google Gemini AI."
)

if __name__ == "__main__":
    iface.launch()
