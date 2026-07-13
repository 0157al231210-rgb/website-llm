from extractor.pipeline import process_html


with open("datasets/raw/quotes_dataset/page_000001.html", encoding="utf-8") as f:
    html = f.read()

text = process_html(html)

print(text)