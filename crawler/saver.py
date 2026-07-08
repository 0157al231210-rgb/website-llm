from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_BASE = BASE_DIR / "datasets" / "raw"
PROCESSED_BASE = BASE_DIR / "datasets" / "processed"
INDEX_BASE = BASE_DIR / "datasets" / "crawl_index"

RAW_BASE.mkdir(parents=True, exist_ok=True)
PROCESSED_BASE.mkdir(parents=True, exist_ok=True)
INDEX_BASE.mkdir(parents=True, exist_ok=True)

def save_html(html, page_id, dataset_name):

    dataset_folder = RAW_BASE / dataset_name
    dataset_folder.mkdir(parents=True, exist_ok=True)

    filename = dataset_folder / f"page_{page_id:06d}.html"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)
        
def save_json(page_data, page_id, dataset_name):

    dataset_folder = PROCESSED_BASE / dataset_name
    dataset_folder.mkdir(parents=True, exist_ok=True)

    filename = dataset_folder / f"page_{page_id:06d}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(page_data, file, ensure_ascii=False, indent=4)
        
def save_metadata(page_id, url, depth, dataset_name):

    metadata = {
        "page_id": page_id,
        "url": url,
        "depth": depth,
        "html_file": f"page_{page_id:06d}.html",
        "json_file": f"page_{page_id:06d}.json"
    }

    index_file = INDEX_BASE / f"{dataset_name}.jsonl"

    with open(index_file, "a", encoding="utf-8") as file:
        file.write(json.dumps(metadata, ensure_ascii=False))
        file.write("\n")
    
