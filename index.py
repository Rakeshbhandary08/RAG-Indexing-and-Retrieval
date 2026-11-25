from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

pdf_path=Path(__file__).parent /"synopsis.pdf"

print(pdf_path)

#Load the file into the python program
loader=PyPDFLoader(file_path=str(pdf_path))

docs=loader.load()

#Split the documents into smaller chunks
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=400)

chunks=text_splitter.split_documents(documents=docs)

#vector emdedding
embedding_model=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vector_store=QdrantVectorStore.from_documents(documents=chunks,
                                              embedding=embedding_model,
                                              url="http://localhost:6333",
                                              collection_name="indexing_genai")


print("Indexing of the documents is done.")