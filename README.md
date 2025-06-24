# 🩺 AI Doctor 2.0 — Multimodal Health Assistant

An experimental AI-powered doctor that listens, sees, and responds — all in one interface. Built using speech, image, and text-based interaction powered by cutting-edge models like **Whisper**, **LLaMA Instruct**, and **Groq LLM**, all integrated via **Gradio UI**.

## 🚀 Features

- 🎙️ **Voice Input** via OpenAI Whisper (Speech-to-Text)
- 🖼️ **Image Input** processed using LLaMA Instruct (b64 encoded)
- 🧠 **LLM Response** generated via Groq's fast large language model
- 🔊 **Audio Output** using gTTS (Text-to-Speech)
- 💻 **Interactive UI** built with Gradio

## 🧩 Tech Stack

- [OpenAI Whisper](https://openai.com/research/whisper) — Speech Recognition  
- [LLaMA Instruct](https://ai.meta.com/llama/) — Image Context Handling  
- [Groq LLM](https://groq.com/) — Fast LLM inference  
- [gTTS](https://pypi.org/project/gTTS/) — Text-to-Speech  
- [Gradio](https://gradio.app/) — Web-based UI

## 📦 Setup

```bash
git clone https://github.com/Saket200/AI-Doctor-2.0.git
cd ai-doctor-2.0
pip install -r requirements.txt
python app.py
