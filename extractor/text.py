def extract_text(tag) -> str:
    """
    Extract readable text from a BeautifulSoup tag.
    
    Args:
        tag (Tag): BeautifulSoup tag representing the main content.
        
    Returns:
        str: Extracted text with basic spacing preserved.
    """
    
    
    if tag is None:
        return ""
    
    return tag.get_text(separator=" ", strip=True)