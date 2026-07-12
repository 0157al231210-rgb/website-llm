from extractor.scorer import score_tag


def extract_main_content(dom):
    """
    Return the HTML  element that most likely 
    contains the primary content of the page.
    """
    
    candidates = dom.find_all(
        ["main", "article", "section", "div"]
    ) 
    
    best_tag = None
    best_score = float("-inf")
    
    for tag in candidates:
        score = score_tag(tag)
        
        if score > best_score:
            best_score = score
            best_tag = tag
    
    return best_tag