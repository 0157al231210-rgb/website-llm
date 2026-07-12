from extractor.density import (
    get_word_count, get_link_density, get_paragraph_count
)


def score_tag(tag) -> int:
    """
    Compute a heuristic score indicateing how likely 
    an HTML tag is to contain meaningful content for AI training."""
    
    words = get_word_count(tag)
    links = get_link_density(tag)
    paragraphs = get_paragraph_count(tag)
    
    score = 0
    
    # Heuristic scoring based on content features
    
    # Word count bonus
    if words > 500:
        score += 50
    elif words > 300:
        score += 30
    elif words > 100:
        score += 10
        
    # Paragraph count bonus
    if paragraphs > 5:
        score += 20
    elif paragraphs > 2:
        score += 10
        
    # Link density penalty
    if links > 0.5:
        score -= 30
    elif links > 0.2:
        score -= 10
        
    return score
    