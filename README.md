# 🤖 AI IT Support Agent

## 🚀 Overview
An AI agent that converts natural language IT support requests into browser actions and executes them on a mock admin panel.

## 🧠 Architecture
User Input → LLM (Groq LLaMA 3) → Action Steps → Playwright → Flask Admin Panel

## ✨ Features
- Create user accounts
- Reset passwords
- Activity logs
- Natural language input
- Browser automation (human-like)

## 🛠 Tech Stack
- Python
- Flask
- Playwright
- Groq (LLaMA 3)
- Replit (Deployment)

## ▶️ Run Locally 

```bash
pip install flask playwright groq
python -m playwright install

python app.py
python agent.py

https://ai-it-support-agent--shravanij941.replit.app
