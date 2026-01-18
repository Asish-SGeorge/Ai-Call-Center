# Ai-Call-Center

# 🤖 AI-Powered Digital Call Center

An **AI-first, agent-driven digital call center** that autonomously handles customer interactions via chat and voice, understands intent and emotion, resolves issues intelligently, and escalates to humans only when required.

This project demonstrates how modern enterprises can **reduce cost, scale instantly, and improve customer experience** using AI agents.

---

## 🚀 Problem Statement

Traditional contact centers are:

* Expensive to operate
* Difficult to scale
* Highly dependent on human agents

Enterprises need **AI-first digital call centers** that can:

* Handle customer queries autonomously
* Understand context, intent, and emotion
* Escalate only when necessary
* Operate at low cost and high scale

---

## ✅ Solution Overview

This project implements a **multi-agent AI architecture** with:

* **Primary Agent** – Handles customer queries using LLMs
* **Supervisor Agent** – Analyzes emotion and response confidence
* **Escalation Agent** – Triggers human handoff when needed
* **Conversation Memory** – Maintains full context across turns
* **Voice + Chat Support** – Text + speech output (free, browser-based)
* **API-First Backend** – Easy enterprise integration

---

## 🧠 AI Agent Architecture

```
Frontend (Chat + Voice)
        |
        v
FastAPI Backend (/chat)
        |
        v
Primary Agent (LLM Response)
        |
        v
Supervisor Agent (Emotion + Confidence)
        |
        +--> ✅ Resolved (AI Response)
        |
        +--> 🚨 Escalated (Human / Ticket)
```

---

## ✨ Key Features

* 🤖 **Autonomous AI Customer Support**
* 🧠 **Emotion & Confidence Detection**
* 🔁 **Intelligent Escalation Logic**
* 🗣️ **Voice Output (Text-to-Speech)**
* 💬 **Real-time Chat UI**
* 🧾 **Conversation Memory**
* 📊 **Resolution vs Escalation Metrics**
* 🔌 **API-First & Modular Design**

---

## 🛠️ Tech Stack

### Frontend

* HTML, CSS (Glassmorphism UI)
* Vanilla JavaScript
* Web Speech API (Text-to-Speech – Free)

### Backend

* FastAPI (Python)
* Gemini LLM (Google Generative AI)
* Modular agent-based architecture

---

## 📂 Project Structure

```
ai_call_center/
│
├── backend/
│   ├── api.py              # FastAPI backend
│   ├── agents.py           # Primary AI agent
│   ├── supervisor.py       # Emotion & confidence analysis
│   ├── escalation.py       # Escalation logic
│   ├── memory.py           # Conversation memory
│   └── .env                # API keys
│
├── frontend/
│   └── index.html          # 3D glass UI + voice support
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-call-center.git
cd ai-call-center
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create a `.env` file inside `backend/`:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

### Start Backend

```bash
cd backend
py -m uvicorn api:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

### Start Frontend

* Open `frontend/index.html` directly in your browser
* No frontend server required 🎉

---

## 🔌 API Usage

### POST `/chat`

**Request**

```json
{
  "message": "I am unable to reset my password"
}
```

**Response**

```json
{
  "reply": "I can help you reset your password...",
  "analysis": {
    "status": "resolved",
    "confidence": 92
  }
}
```

---

## 📊 Analytics (Prototype)

The UI displays:

* Total conversations
* Resolved conversations
* Escalated conversations
* AI confidence score

> Analytics are simulated for this prototype and can be persisted to a database in production.

---

## 🗣️ Voice Support

* Uses **browser-native Web Speech API**
* No backend cost
* Toggle voice output with one click

---

## ☁️ Deployment Strategy

* **Frontend**: Netlify / Vercel / GitHub Pages (Free)
* **Backend**: Docker + Cloud VM / Cloud Run
* **Estimated Cost**: ~$5–10/month for backend

---

## 🔮 Future Enhancements

* CRM & ticketing integration
* Real human-agent dashboard
* Multilingual support
* Model fine-tuning using feedback
* Persistent analytics storage
* Voice input (Speech-to-Text)

---

## 🏆 Why This Project Stands Out

✔ AI-first architecture
✔ Multi-agent design (enterprise-grade)
✔ Clear escalation logic
✔ API-ready for real companies
✔ Low-cost, scalable, cloud-ready

---

## 📜 License

MIT License

---

## 🙌 Acknowledgements

* Google Gemini API
* FastAPI
* Web Speech API

---

If you want, I can next:

* ✨ Optimize this README for **hackathon judging**
* 🧠 Add **architecture diagrams**
* 📄 Write a **submission description**
* 🎤 Prepare **interview explanations**

Just tell me.
