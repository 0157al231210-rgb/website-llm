from downloader import download
from parser import parse
from frontier import URLFrontier
from urllib.parse import urljoin, urlparse
from saver import save_html, save_json, save_metadata
from url_utils import normalize_url
from hasher import content_hash

page_counter = 1

DATASET_NAME = "quotes_dataset"

seed_url ="https://quotes.toscrape.com"
seed_domain = urlparse(seed_url).netloc
MAX_DEPTH = 2

frontier = URLFrontier()
frontier.add(seed_url, 0)

visited = set()
seen_hashes = set()

while not frontier.is_empty():
    
    url, depth = frontier.get()

    if url in visited:
        continue

    print(f"\n[{depth}] Crawling {url}")
    
    html = download(url)    
    
    if html is None:
        print("Download Failed")
        continue
    
    page_hash = content_hash(html)
    
    if page_hash in seen_hashes:
        print("Duplicate page detected, skipping.")
        continue
    
    seen_hashes.add(page_hash)
    
    visited.add(url)

    page_data, links = parse(html)
    
    save_html(html, page_counter, DATASET_NAME)
    save_json(page_data, page_counter, DATASET_NAME)
    save_metadata(page_counter, url, depth, DATASET_NAME)
    
    print(f"Saved as page_{page_counter:06d}")
    
    page_counter += 1
    
    if depth >= MAX_DEPTH:
            continue
    
    for link in links:

        normalized_url = normalize_url(url, link)
        parsed_url = urlparse(normalized_url)

        if parsed_url.netloc != seed_domain:
            continue

        frontier.add(normalized_url, depth + 1)
    
