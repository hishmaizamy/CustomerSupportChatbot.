import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load FAISS index
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Load FLAN-T5 model
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
rag_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device='cpu')

# Set up retriever
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":3})

def answer_query(query):
    docs = retriever.get_relevant_documents(query)
    context = " ".join([doc.page_content for doc in docs])

    # Truncate context to avoid token overflow
    max_context_tokens = 400
    if len(context.split()) > max_context_tokens:
        context = " ".join(context.split()[:max_context_tokens])

    # Prepare input for FLAN-T5
    input_text = f"Answer the question based on the context below:\nContext: {context}\nQuestion: {query}"
    output = rag_pipeline(input_text, max_new_tokens=256)
    return output[0]['generated_text']

# Streamlit UI
st.title("Customer Support Chatbot 🤖")
st.write("Ask me anything about your products or support.")

query = st.text_input("Your question:")
if query:
    answer = answer_query(query)
    st.write("**Answer:**", answer)
