"""
HTML cleaning utilities.

This module removes HTML elements that are unlikely 
to contain meaningful textual content for AI training.
"""

from extractor.dom import get_all_nodes


REMOVE_TAGS = {
    "script",
    "style",
    "noscript",
    "svg",
    "canvas",
    "iframe",
    "nav",
    "footer",
    "aside",
}


def remove_unwanted_tags(soup):
    """
    Remove unwanted HTML tags from the DOM.

    Args:
        soup (BeautifulSoup): Parsed DOM tree.
    
    Returns:
        BeautifulSoup: Cleaned DOM tree.
    """
    for tag in get_all_nodes(soup):
        if tag.name in REMOVE_TAGS:
            tag.decompose()
    
    return soup
