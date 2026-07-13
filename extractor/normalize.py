import re


def normalize_text(text: str) -> str:
    """
    Normalize extracted text for downstream processing.
    
    Args:
        text (str): Raw extracted text.
        
    Returns:
        str: Clean, normalized text.
    """
    
    if not text: 
        return ""
    
    # Removing leading and trailing whitespace
    text = text.strip()
    
    # Collapsing multiple spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)
    
    # Collapsing excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    
    return text