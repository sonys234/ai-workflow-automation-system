from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_policy_retriever():
    # Load the leave policy text file
    loader = TextLoader("data/leave_policy.txt")
    documents = loader.load()

    # Create embeddings using HuggingFace (new package)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Build a FAISS vector store from the documents
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Return a retriever interface (use .invoke(query) instead of .get_relevant_documents)
    return vectorstore.as_retriever()