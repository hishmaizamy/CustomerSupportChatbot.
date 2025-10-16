README.md

# AI Customer Support Chatbot

An AI-powered customer support chatbot built with **LangChain**, **FAISS**, and **Streamlit**.  
It allows users to query data from custom documents or knowledge bases.

## 🚀 Features
- Chat with your own data
- FAISS vector index for semantic search
- Streamlit web UI
- OpenAI / Gemini API integration

## 🧠 Tech Stack
- Python 3.10+
- FAISS
- LangChain
- Streamlit
- SentenceTransformers / OpenAI embeddings

## 📂 Project Structure
```
📁 chatbot/
├── app.py
├── requirements.txt
├── README.md
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
└── data/
    └── your_documents.pdf
```

## ⚙️ Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chatbot.git
   cd chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the chatbot:
   ```bash
   streamlit run app.py
   ```

## 🧩 How to Rebuild FAISS Index
If you update your data:
```bash
python ingest.py
```

This recreates `index.faiss` and `index.pkl` in the `faiss_index/` folder.

---

### ⚡ Environment Variables
Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your_key_here
```

---

### ❤️ Credits
Developed with LangChain + Streamlit by Hishy 🚀
