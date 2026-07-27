import streamlit as st
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama

# Title in app
st.title("Society by Laws Engine")
st.write("Ask questions about the society by laws document.")

# Step 1: Load PDF
loader = PyPDFLoader("society_by_law2.pdf")
docs = loader.load()

# Step 2: Split PDF into small chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs) # It Split the document into small chunks of 500 characters with an overlap of 50 characters between chunks.

# Step 3: Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
) # It creates embeddings for the text chunks using a pre-trained model.

# Step 4: Store embeddings in FAISS
vectorstore = FAISS.from_documents(chunks, embeddings)

# Step 5: Load Ollama model
llm = ChatOllama(
    model="deepseek-r1:1.5b",#llama3
    temperature=0
)# It loads the deepseek/Ollama model for generating responses.

# Step 6: Create input box
query = st.text_input("Ask your question")

# Step 7: If user enters a question
if query:
    try:
        # Search relevant chunks from vector database
        result_docs = vectorstore.similarity_search(query, k=3)

        # Combine those chunks into one context
        context = "\n\n".join([doc.page_content for doc in result_docs])

        # Create final prompt
        prompt = f"""
You are a helpful assistant for answering questions from the society by laws document.

Use only the context below to answer the question.
If the answer is not present in the context, say:
I could not find that in the society by laws document.

Context:
{context}

Question:
{query}

Answer:
"""

        # Send prompt to LLM
        response = llm.invoke(prompt) # It sends the prompt to the LLM and gets the response.

        # Display answer
        st.write("### Answer")
        st.write(response.content)

    except Exception as e:
        st.error(f"Error: {e}")