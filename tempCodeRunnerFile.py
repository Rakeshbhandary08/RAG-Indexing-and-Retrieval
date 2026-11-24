from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path=Path(__file__).parent /"nodejs.pdf"

print(pdf_path)

#Load the file into the python program
loader=PyPDFLoader(file_path=str(pdf_path))
