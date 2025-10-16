
# 🤖 AI Customer Support Chatbot  

An intelligent chatbot that answers customer queries using **AI + Retrieval-Augmented Generation (RAG)**.  
It reads from your **FAQ PDF dataset** and gives **accurate, context-based answers**.  

---

## 🚀 Features  

- ⚡ **Instant Answers:** Pulls information directly from your uploaded PDF.  
- 🧠 **Smart Search:** Uses FAISS vector database to find the most relevant responses.  
- 💬 **AI-Powered Replies:** Powered by Google’s FLAN-T5 model for natural, fluent answers.  
- 🌐 **Interactive UI:** Simple Streamlit interface for live chat.  

---

## 🧩 Project Structure

CustomerSupportChatbot/
├─ app.py # Streamlit chatbot app
├─ faiss_index/ # FAISS index files (vector database)
├─ AI_Customer_Support_FAQ_Dataset.pdf # Custom dataset
├─ requirements.txt # Python dependencies
├─ README.md # Documentation (this file)


---

## ⚙️ Installation & Setup  

### 1️⃣ Clone this repository  
```bash
git clone https://github.com/YOUR-USERNAME/CustomerSupportChatbot.git
cd CustomerSupportChatbot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit app
streamlit run app.py

💡 Once it runs, open the URL in your terminal — your chatbot will appear in the browser 🌍

🧠 How It Works

The PDF is converted into text using LangChain’s document loader.
Text is embedded into vector form using SentenceTransformer.
The FAISS index stores and retrieves the closest matching answers.
The FLAN-T5 model uses that context to generate smooth, accurate responses.

🧑‍💻 Author

 AI & Computing Enthusiast 
Built with 💖 using LangChain, Streamlit, and Transformers.

⭐ If you like this project, don’t forget to star the repo!
