# 🚀 ChiefAI – Multi-Agent Startup Intelligence Platform

> **Transform startup ideas into investor-ready intelligence using autonomous AI agents.**

ChiefAI is an AI-powered startup intelligence platform built for the **Microsoft Agents League Hackathon**. It leverages **12 specialized AI agents** working collaboratively to analyze startup ideas, generate business insights, assess investment readiness, evaluate market opportunities, identify risks, and produce comprehensive startup reports.

Powered by **Microsoft Azure AI Foundry** and **Azure OpenAI**, ChiefAI acts as an intelligent co-founder for entrepreneurs, founders, incubators, and investors.

---

## 🌟 Features

- 🤖 12 Specialized AI Agents
- 📊 Market Analysis
- 💼 Business Strategy Generation
- 💰 Investor Readiness Assessment
- ⚠️ Risk Analysis
- 🏢 Competitor Analysis
- 📈 Growth Strategy Recommendations
- 📋 Executive Summary Generation
- 🎯 SWOT Analysis
- 📑 Presentation Generation
- 📚 Research Insights
- 🔄 Multi-Agent Orchestration
- 📂 PDF Startup Proposal Analysis
- 📈 Interactive Dashboard
- 📜 Report History
- 📤 Export Startup Reports

---

# 🧠 Multi-Agent Architecture

ChiefAI uses a collaborative multi-agent architecture where each AI agent specializes in one aspect of startup evaluation.

```
                  Startup Proposal
                         │
                         ▼
             Startup Orchestrator
                         │
 ┌────────────────────────────────────────────┐
 │                                            │
 ▼                                            ▼
Market Agent                         Business Agent
Research Agent                       Investor Agent
Competitor Agent                     SWOT Agent
Risk Agent                           Strategy Agent
Funding Agent                        Presentation Agent
Execution Agent                      Executive Summary Agent
 │
 ▼
 Unified Startup Intelligence Report
```

Each agent independently analyzes the startup before the orchestrator combines their outputs into a single comprehensive report.

---

# 🤖 AI Agents

| Agent | Responsibility |
|-------|----------------|
| 📈 Market Agent | Market size, TAM, SAM, SOM, trends |
| 💼 Business Agent | Business model, customer segments, revenue streams |
| 💰 Investor Agent | Funding readiness and investment scoring |
| ⚠️ Risk Agent | Startup risks and mitigation analysis |
| 🏢 Competitor Agent | Competitor discovery and benchmarking |
| 📊 SWOT Agent | Strengths, Weaknesses, Opportunities, Threats |
| 🚀 Strategy Agent | Growth roadmap and scaling strategy |
| 📚 Research Agent | Industry research and insights |
| 📝 Executive Summary Agent | Executive summary and AI recommendations |
| 💵 Funding Agent | Funding recommendations and valuation |
| 🎨 Presentation Agent | Investor pitch content generation |
| ⚙️ Execution Agent | Startup execution roadmap |

---

# 📷 Platform Modules

## Dashboard

- Startup Overview
- AI Insights
- Executive Summary
- Market Metrics
- Startup Health Score
- Investment Readiness
- Multi-Agent Execution Status

---

## Market Analysis

- Market Size
- CAGR
- TAM / SAM / SOM
- Industry Trends
- Customer Insights
- Competitor Landscape

---

## Business Strategy

- Business Model
- Value Proposition
- Revenue Streams
- Pricing Strategy
- Customer Segments
- Growth Strategy
- SWOT Snapshot

---

## Investor Readiness

- Readiness Score
- Funding Recommendation
- Investment Outlook
- Risk Assessment
- Due Diligence Metrics

---

## Compare Startups

Compare multiple startup analyses side-by-side.

---

## Report History

Every startup analysis is automatically saved for future viewing.

---

# 🛠 Tech Stack

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend

- FastAPI
- Python

### AI

- Microsoft Azure AI Foundry
- Azure OpenAI
- GPT-4.1

### Database

- JSON-based report storage

### Other

- REST APIs
- Concurrent Agent Execution
- Multi-threading

---

# 📁 Project Structure

```
ChiefAI/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── services/
│   │   ├── orchestrator.py
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── services/
│   └── public/
│
├── docs/
├── demo/
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/ChiefAI.git
cd ChiefAI
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```
AZURE_AI_KEY=your_key
AZURE_AI_ENDPOINT=your_endpoint
AZURE_DEPLOYMENT_NAME=your_deployment
```

Run backend:

```bash
uvicorn app.main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Open:

```
http://localhost:3000
```

---

# 🚀 Workflow

1. Upload a startup proposal (PDF)
2. ChiefAI extracts startup information
3. 12 AI agents analyze the startup concurrently
4. The orchestrator aggregates all results
5. A comprehensive startup intelligence report is generated
6. Reports are saved for future reference

---

# 🎯 Use Cases

- Startup Founders
- Entrepreneurs
- Incubators
- Accelerators
- Venture Capital Firms
- Angel Investors
- University Innovation Labs
- Startup Competitions

---

# 🌐 Powered By

- Microsoft Azure AI Foundry
- Azure OpenAI Service
- FastAPI
- Next.js
- TypeScript
- Python

---

# 🏆 Microsoft Agents League Hackathon

ChiefAI was developed as a submission for the **Microsoft Agents League Hackathon**, demonstrating how autonomous AI agents can collaborate to solve complex startup evaluation tasks.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Amreen Bashir**

Built with ❤️ using Microsoft Azure AI Foundry.