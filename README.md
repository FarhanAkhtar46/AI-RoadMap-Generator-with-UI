# AI Roadmap Generator

**AI Roadmap Generator** is a full-stack application that helps users generate personalized learning or career roadmaps using AI. The app guides users through a dynamic, conversational interface, asks follow-up questions based on their answers, and produces a tailored, structured roadmap with visualizations.

---

## Features

- **Conversational UI:** Users interact with an AI assistant that asks context-aware, dynamic follow-up questions to clarify their goals, expertise, tech stack preferences, and more.
- **LLM-Powered:** Uses GPT-4o (or any OpenAI-compatible LLM) to generate the next best question and to summarize user requirements.
- **Personalized Roadmaps:** Generates a step-by-step, module-based learning or career roadmap tailored to the user's answers.
- **Visualizations:** Produces both a structured roadmap view and visual diagrams (Mermaid.js, mindmap, and downloadable HTML).
- **Modern Frontend:** Beautiful, responsive React (Vite) frontend with a clean, user-friendly design.
- **API Backend:** FastAPI backend for conversation management, roadmap generation, and visualization file serving.

---

## Tech Stack

- **Frontend:** React (Vite), TypeScript, Tailwind CSS, Lucide Icons, React Router
- **Backend:** FastAPI, Python, OpenAI API, LangChain (for roadmap logic)
- **Visualization:** Mermaid.js, custom HTML, mindmap diagrams
- **Other:** CORS, static file serving, environment variable support

---

## How It Works

1. **User starts a conversation** by entering a domain (e.g., "web development").
2. **AI assistant asks dynamic follow-up questions** (e.g., expertise, purpose, tech stack, backend/frontend preference, etc.).
3. **Once enough info is collected,** the backend generates a personalized roadmap and visualizations.
4. **User sees the roadmap** in a structured card view and can view/download the generated HTML visualization.

---

## Getting Started

### 1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-roadmap-generator.git
cd ai-roadmap-generator
```

### 2. **Backend Setup**
- Create a Python virtual environment and activate it.
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Set your OpenAI API key in a `.env` file:
  ```
  OPENAI_API_KEY=sk-...
  ```
- Start the FastAPI server:
  ```bash
  uvicorn api_server:app --reload
  ```

### 3. **Frontend Setup**
- Go to the frontend directory:
  ```bash
  cd frontend
  ```
- Install dependencies:
  ```bash
  npm install
  ```
- Start the frontend:
  ```bash
  npm run dev
  ```
- Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## Folder Structure

```
langchain_roadmap_generator/
  api_server.py
  supervisor.py
  visualization_agent.py
  visualization_renderer.py
  dynamic_llm_conversation_agent.py
  ...
frontend/
  src/
    components/
      RoadmapGenerator.tsx
      RoadmapVisualization.tsx
    App.tsx
    ...
  ...
```

---

## Customization

- You can easily add new domains, tech stacks, or visualization types by editing the backend logic.
- The LLM prompt can be tuned for more/less guidance or different conversation styles.

---

## License

MIT

---

## Acknowledgements

- [OpenAI](https://openai.com/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Mermaid.js](https://mermaid-js.github.io/)
- [React](https://react.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)

---

**Feel free to fork, contribute, or open issues!**