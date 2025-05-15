import fitz  # PyMuPDF
import requests
from bs4 import BeautifulSoup


def pdf_parse(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []

    for pg_num in range(len(doc)):
        page = doc.load_page(pg_num)
        page_text = page.get_text()

        
        for para in page_text.split("\n\n"):
            chunks.append({
                "text": para.strip(),
                "metadata": {
                    "source": "CMU LSTM Notes",
                    "page": pg_num + 1
                }
            })
    return chunks


def html_parse(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    chunks = []
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
        text = tag.get_text().strip()
        if text:
            chunks.append({
                "text": text,
                "metadata": {
                    "source": "Chris Olah Blog",
                    "tag": tag.name
                }
            })
    return chunks
def parse_all(pdf_path,url):
    chunk_pdf=pdf_parse(pdf_path=pdf_path)
    chunk_html=html_parse(url=url)
    chunk=chunk_pdf+chunk_html
    for idx, ch in enumerate(chunk):
        ch["id"] = f"chunk{idx}"

    return chunk