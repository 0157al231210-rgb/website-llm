import hashlib

def content_hash(content: str) -> str:
    """
    Generate a SHA256 hash for the given content.

    Args:
        content (str): The content to hash.

    Returns:
        str: A hexadecimal SHA256 Hash.
    """
    
    
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
