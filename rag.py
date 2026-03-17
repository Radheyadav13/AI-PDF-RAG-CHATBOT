from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Load PDF
loader = PyPDFLoader("data/sample.pdf")
docs = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# Embeddings
embeddings = OllamaEmbeddings(model="phi3")

# Vector DB
db = Chroma.from_documents(chunks, embeddings)

# LLM
llm = OllamaLLM(model="phi3")

# Retriever
retriever = db.as_retriever()

# Chat loop
while True:
    query = input("\nAsk: ")

    if query.lower() in ["exit", "quit"]:
        break

    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer ONLY from the context below:

{context}

Question: {query}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:", response)