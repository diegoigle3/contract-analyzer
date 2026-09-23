import sys
import pymupdf
from pathlib import Path

def extract_text(pdf_path: str) -> str:

   path=Path(pdf_path)
   if not path.exists():
       raise FileNotFoundError(f"The file {path} does not exist.")

   with pymupdf.open(path) as doc:
       pages = [page.get_text() for page in doc]

   text="\n".join(pages).strip()
   if not text:
       raise ValueError(f"No text could be extracted from the PDF file {path}.")

   return text
if __name__ == "__main__":
    print(extract_text(sys.argv[1]))