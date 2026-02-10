# 📝 Drafter – AI Document Writing Agent

Drafter is an interactive AI-powered document assistant built using **LangGraph**, **LangChain**, and **Google Gemini**.  
It allows users to create, update, and save documents using natural language through a terminal-based interface.

This project demonstrates **tool-using AI agents**, **stateful workflows**, and **graph-based execution control**.

---

## 🚀 Features

- ✍️ AI-assisted document drafting
- 🔁 Iterative document updates
- 🛠️ Tool-based actions (`update`, `save`)
- 🧠 Stateful conversation using LangGraph
- 💾 Save documents as `.txt` files
- 🖥️ Simple terminal-based interaction

---

## 🧱 Architecture Overview

User Input (Terminal)
↓
LangGraph State Machine
↓
Gemini LLM (Tool Calling)
↓
Document Update / Save Tools
↓
Local File System

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **LangGraph**
- **Google Gemini (gemini-2.5-flash)**
- **python-dotenv**

---

## 📂 Project Structure
.
├── main.py # Drafter agent implementation
├── .env # API keys (not committed)
├── README.md # Documentation

---

## ⚙️ Installation & Setup

```bash
### 1️⃣ Clone the Repository

git clone https://github.com/your-username/drafter-agent.git
cd drafter-agent 

2️⃣ Install Dependencies

pip install langchain langgraph langchain-google-genai python-dotenv

3️⃣ Configure Environment Variables
Create a .env file in the root directory:

GOOGLE_API_KEY=your_google_gemini_api_key
