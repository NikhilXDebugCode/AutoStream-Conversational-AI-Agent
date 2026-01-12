AutoStream Conversational AI Agent
📌 Project Overview

AutoStream is a console-based Conversational AI Agent built for a fictional SaaS company that provides automated video editing tools for content creators.

This project demonstrates a working model of the Conversational AI Agent described in the assessment, focusing on:

Intent handling

Retrieval-Augmented responses from a local knowledge base

Clean conversational flow

Offline, cost-free execution

The agent answers pricing and policy-related questions using a local Markdown knowledge base, ensuring accurate and deterministic responses.

🔑 Note on LLM / API Usage (Important)

The assessment allows the use of external LLM APIs such as OpenAI, Gemini, or Claude. However, these APIs require paid billing accounts.

To keep the project:

Fully runnable without cost

Easy to evaluate

Reproducible on any system

this implementation uses a local RAG-style approach instead of calling a paid LLM API.

All required agent behaviors described in the assessment are still implemented and demonstrated.
The system is designed so that an API key can be added later with minimal changes if billing is available.

This is a design decision, not a limitation.

🧠 Agent Capabilities
1. Intent Handling

The agent can identify and respond to:

Casual greetings (e.g., hi, hello)

Product and pricing-related questions

Policy-related questions (refunds, support)

Intent detection is implemented using lightweight keyword-based logic to ensure reliability and offline execution.

2. RAG-Based Knowledge Retrieval

The agent retrieves answers only from a local knowledge base

Knowledge is stored in:

data/knowledge.md


Responses are grounded in predefined product pricing and company policies

This follows the Retrieval-Augmented Generation (RAG) concept using local data instead of an external LLM.

3. Offline & Deterministic Execution

No external APIs

No API keys required

No billing

Fully offline execution

This guarantees consistent output and avoids hallucinations.

📂 Project Structure
autostream-agent/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── data/
│   └── knowledge.md
│
├── requirements.txt
└── README.md

🛠️ Tech Stack

Language: Python 3.9+

Interface: Command Line (CLI)

Knowledge Source: Local Markdown file

Dependencies: None (lightweight by design)

▶️ How to Run the Project Locally
1️⃣ Create and Activate Environment (Recommended)
conda create -n autostream_clean python=3.10 -y
conda activate autostream_clean

2️⃣ Navigate to Project Folder
cd Desktop/autostream-agent

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Run the Agent
python -m app.main

5️⃣ Example Queries
hi
tell me about pricing
what is the refund policy?


To exit:

exit

🧩 Architecture Explanation (≈200 Words)

This project follows a simple and reliable conversational architecture aligned with the assessment requirements. The agent operates in a command-line interface and processes one user query at a time. Each input is analyzed to determine user intent, after which the system retrieves relevant information from a local knowledge base.

The knowledge base is stored as a Markdown file containing structured product pricing and company policy information. When a query is received, the agent performs keyword-based retrieval to identify relevant sections of the knowledge base and returns accurate, grounded responses. This approach follows the principles of Retrieval-Augmented Generation (RAG) while remaining fully offline.

State management is intentionally minimal, as the agent is designed for clarity and ease of evaluation rather than complex multi-session memory. This keeps the system lightweight, predictable, and easy to extend.

Although the assessment allows frameworks such as LangChain or LangGraph, this implementation avoids external dependencies and paid APIs to ensure reproducibility and accessibility. The modular design allows the retrieval and response layer to be upgraded to an LLM-backed system in the future without refactoring the overall architecture.

📲 WhatsApp Deployment (Conceptual Explanation)

To deploy this agent on WhatsApp:

Use WhatsApp Business Cloud API or Twilio WhatsApp API

Set up a backend server using Flask or FastAPI

Configure a Webhook to receive incoming WhatsApp messages

Pass messages to the agent logic

Send the agent’s response back via the WhatsApp API

The current CLI-based logic can be reused directly within the webhook handler.

🎥 Demo Video Guidelines

The demo video (2–3 minutes) should show:

Agent greeting the user

Agent answering a pricing question

Agent responding to a policy-related question

✅ Evaluation Readiness

✔ Intent handling implemented

✔ Local RAG-based knowledge retrieval

✔ Clean, readable code

✔ No paid APIs or billing

✔ Fully runnable and reproducible

✔ Aligned with assessment requirements

📌 Final Notes

This submission represents a working, offline implementation of the Conversational AI Agent described in the assessment.
The project prioritizes correctness, clarity, and real-world deployability while remaining cost-free for reviewers.
