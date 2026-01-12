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

