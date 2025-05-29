# 🤖 AI Tool Usage Log

This document outlines where and how AI tools were used during the development of the Voice-Powered Multi-Agent Finance Assistant.

---

## 📌 Overview

| Tool / API          | Usage Context                                                    |
|---------------------|------------------------------------------------------------------|
| OpenAI GPT-3.5      | Market brief generation (Language Agent)                        |
| ChatGPT             | Code generation, modular structuring, error debugging           |
| FAISS               | Context retrieval via vector similarity (Retriever Agent)       |
| Hugging Face Transformers | Sentence embeddings using all-MiniLM-L6-v2             |
| LangGraph / CrewAI  | [Optional] Agent orchestration for complex coordination         |
| yfinance            | Historical and real-time stock data (TSMC, Samsung)             |
| yahoo_fin           | Earnings data for earnings surprise calculation                 |
| Whisper / Google STT| Speech-to-text conversion from microphone input (Voice Agent)   |
| pyttsx3             | Text-to-speech narration of market brief (Voice Agent)          |

---

## 💡 Prompts Sent to GPT-3.5 (Language Agent)

### 🧠 Prompt Example 1: Morning Brief
