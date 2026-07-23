from crawler.hasher import content_hash
from pipeline.rules.base_rule import BaseRule


class DuplicateRule(BaseRule):
    """
    Rejects duplicate documents based on their
    content hash.
    """
    
    
    def __init__(self):
        self.seen_hashes = set()
        
    
    @property
    def name(self) -> str:
        return "Duplicate Detection"
    
        
    def evaluate(self, document: dict, policy: dict) -> None:
        """
        Evaluate the document against the duplicate policy.
        
        updates the shared policy object in place.
        
        Args:
            document:
                Processed document.
                
            policy:
                Shared policy object modified by the rule.    
        """
        
        
        if not policy["accepted"]:
            return
        
        content_fingerprint = content_hash(document["text"])
        
        if content_fingerprint in self.seen_hashes:
            policy["accepted"] = False
            policy["reasons"].append("Duplicate document.")
        
        if policy["accepted"]:
            self.seen_hashes.add(content_fingerprint)
        
        