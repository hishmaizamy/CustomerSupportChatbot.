import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import pickle, os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="AI Chatbot", layout="wide")

# Load FAISS index
def load_faiss():
    with open("faiss_index/index.pkl", "rb") as f:
        index = pickle.load(f)
    faiss_store = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    return faiss_store

st.title("💬 AI Customer Support Chatbot")
st.write("Chat with your own documents powered by FAISS + LangChain!")

# Initialize chat
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.warning("⚠️ Add your OpenAI API key to .env")
else:
    vectorstore = load_faiss()
    llm = ChatOpenAI(temperature=0.3)
    chain = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())

    query = st.chat_input("Ask me anything...")
    if query:
        response = chain({"question": query, "chat_history": st.session_state.chat_history})
        st.session_state.chat_history.append((query, response["answer"]))
        st.write("**You:**", query)
        st.write("**Bot:**", response["answer"])
