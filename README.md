# 🧠 Voice-Powered Multi-Agent Finance Assistant

This project is a sophisticated, open-source, modular finance assistant that listens to your voice query and responds with a spoken market brief. It integrates real-time market data, document retrieval, language generation, and speech synthesis — all orchestrated via microservices.

---

## 📌 Use Case: Morning Market Brief

> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

✅ The system understands this query and responds with:

> "Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday. TSMC beat estimates by 4%, Samsung missed by 2%. Regional sentiment is neutral with a cautionary tilt due to rising yields."

---

## 🏗 Architecture

```mermaid
graph TD
    A[Voice Input (Mic)] --> B[Speech-to-Text (STT)]
    B --> C[Orchestrator (FastAPI)]
    C --> D1[API Agent: yFinance]
    C --> D2[Scraping Agent: Earnings]
    C --> D3[Retriever Agent: FAISS]
    C --> D4[Language Agent: OpenAI]
    D4 --> E[Text-to-Speech (TTS)]
    E --> F[Streamlit UI Output]
