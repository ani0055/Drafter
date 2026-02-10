# 📝 Drafter
An AI-Powered Document Writing Agent using LangGraph & Gemini

Drafter is an interactive, tool-driven AI agent that helps users draft, update, and save documents through natural language conversations.
Built with LangGraph, LangChain, and Google Gemini, it demonstrates modern agent design patterns such as stateful workflows, tool invocation, and graph-based control flow.

# 🌟 Why This Project Matters

This project showcases:

✅ Real-world LLM agent orchestration
✅ Tool-using AI agents (update & save actions)
✅ Stateful conversations using LangGraph
✅ Clean separation of reasoning, tools, and control flow
✅ Production-style agent loop (not a toy chatbot)

Perfect as a portfolio project, college submission, or agent-system reference implementation.

# 🚀 Features

🧠 AI writing assistant with document awareness
✍️ Iterative document updates via natural language
🛠️ Tool calling (update, save) with Gemini
🔄 LangGraph-based execution flo
💾 Save final output as a .txt file
🖥️ Lightweight terminal interface

# 🧱 Architecture Overview

User (Terminal)
   ↓
LangGraph State Machine
   ↓
LLM (Gemini 2.5 Flash)
   ↓
Tool Calls (update / save)
   ↓
Document State + File System

# Core Components

Agent Node → Handles reasoning and responses
Tool Node → Executes document actions
Conditional Edges → Decide when to stop execution
Shared State → Maintains conversation + document content

# 🛠️ Tech Stack

Component	Technology
Language	Python
LLM	Google Gemini (gemini-2.5-flash)
Agent Framework	LangChain
Workflow Engine	LangGraph
Tooling	LangChain Tools
Config	python-dotenv

# 📂 Project Structure
.
├── main.py          # Drafter agent implementation
├── .env             # API keys (ignored in version control)
├── README.md        # Project documentation

# ⚙️ Setup & Installation

1️⃣ Clone the Repository
git clone https://github.com/your-username/drafter-agent.git
cd drafter-agent

2️⃣ Install Dependencies
pip install langchain langgraph langchain-google-genai python-dotenv

3️⃣ Configure Environment Variables
Create a .env file:
GOOGLE_API_KEY=your_google_gemini_api_key

# ▶️ Running the Agent
python main.py


You’ll see:

====== Drafter ======

The agent will guide you step-by-step to create, modify, and save a document.

# 🧪 Example Interaction
What would you like to do with the document?
> Create a project README for an AI agent

AI: (Generates content and updates document)

What would you like to do with the document?
> Save it as drafter_readme

TOOL RESULT:
Document has been saved successfully to 'drafter_readme.txt'

# 🛠️ Available Tools
✍️ update

Updates the entire document content.

update(content: str) -> str

Designed for full document rewrites to keep state consistent.

💾 save

Persists the document and ends the agent workflow.

save(filename: str) -> str

Automatically appends .txt if missing
