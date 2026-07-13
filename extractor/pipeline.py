from extractor.dom import create_dom
from extractor.cleaner import remove_unwanted_tags
from extractor.extractor import extract_main_content
from extractor.text import extract_text
from extractor.normalize import normalize_text


def extract(html):
    """
    Extract the main content block from raw HTML.
    """
    
    dom = create_dom(html)
    remove_unwanted_tags(dom)
    best = extract_main_content(dom)
    
    return best

def process_html(html: str) -> str:
    """
    Process HTML into clean normalized text.
    
    Args: 
        html (str): Raw HTML page.
        
    Returns:
        str: Clean normalized text.
    """
    
    
    tag = extract(html)
    
    text = extract_text(tag)
    
    text = normalize_text(text)
    
    return text
    