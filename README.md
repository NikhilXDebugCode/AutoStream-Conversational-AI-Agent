# AutoStream Conversational AI Agent

## 📌 Project Overview

AutoStream is a **console-based Conversational AI Agent** built for a fictional SaaS company that provides automated video editing tools for content creators.

This project demonstrates a **working model** of the Conversational AI Agent described in the assessment, focusing on:

- Intent handling  
- Retrieval-Augmented responses from a local knowledge base  
- Clean conversational flow  
- Offline, cost-free execution  

The agent answers product, pricing, feature, and policy-related questions using a **local Markdown knowledge base**, ensuring **accurate, deterministic, and hallucination-free responses**.

✅ **Tested on 30+ different user questions** including pricing, features, platforms, usage, security, and policies.

---

## 🔑 Note on LLM / API Usage (Important)

The assessment allows the use of external LLM APIs such as **OpenAI, Gemini, or Claude**. However, these APIs require **paid billing accounts**.

To keep the project:

- Fully runnable without cost  
- Easy to evaluate  
- Reproducible on any system  

this implementation uses a **local RAG-style approach** instead of calling a paid LLM API.

All required agent behaviors described in the assessment are still implemented and demonstrated.  
The system is designed so that **an API key can be added later with minimal changes** if billing is available.

This is a **design decision**, not a limitation.

---

## 🧠 Agent Capabilities

### 1. Intent Handling

The agent can identify and respond to:

- Casual greetings (e.g., *hi*, *hello*)
- Product and pricing-related questions
- Feature-related questions
- Policy-related questions (refunds, support, security, access)

Intent detection is implemented using **lightweight keyword-based logic** to ensure reliability and offline execution.

---

### 2. RAG-Based Knowledge Retrieval

- The agent retrieves answers **only from a local knowledge base**
- Knowledge is stored in:
- 
- Responses are grounded in predefined product information and company policies

This follows the **Retrieval-Augmented Generation (RAG)** concept using **local data** instead of an external LLM.

---

### 3. Offline & Deterministic Execution

- No external APIs  
- No API keys required  
- No billing  
- Fully offline execution  

This guarantees **consistent output** and avoids hallucinations.

---

## 📂 Project Structure

autostream-agent/
│
├── app/
│ ├── init.py
│ └── main.py
│
├── data/
│ └── knowledge.md
│
├── requirements.txt
└── README.md

---

## 🛠️ Tech Stack

- **Language:** Python 3.9+  
- **Interface:** Command Line (CLI)  
- **Knowledge Source:** Local Markdown file  
- **Dependencies:** None (lightweight by design)

---

## ▶️ How to Run the Project Locally

### 1️⃣ Create and Activate Environment (Recommended)

```bash
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
what features does autostream have
does autostream support youtube
what is the refund policy


To exit:

exit




