from extractor.pipeline import extract
from extractor.text import extract_text

with open("datasets/raw/quotes_dataset/page_000001.html", encoding="utf-8") as f:
    html = f.read()

tag = extract(html)

text = extract_text(tag)

print(text)