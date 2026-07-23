"""
Dataset policy filtering.

This module decides whether a processed document should be accepted
into the training dataset.

Unlike extractor.quality, which evaluates the quality of extracted
text, this module evaluates dataset-level policies.

Examples of future policy checks:
- Duplicate detection
- Language validation
- PII detection
- License compliance
- Readability scoring
- Toxicity filtering
- AI-assisted quality scoring

Pipeline Position:
    Extracted Document
            ↓
    Dataset Policy Filter   ← This module
            ↓
    Accepted / Rejected Dataset
"""
from pipeline.rules.duplicate_rule import DuplicateRule
from pipeline.rules.base_rule import BaseRule


class QualityFilter:
    """
    Applies dataset-level acceptance policies.

    This class acts as the final gatekeeper before a document is written
    into the training dataset.
    """
    
    def __init__(self):
        """
        Initialize the policy engine.
        
        Registers the dataset policy rules that will be
        applied to every processed document.
        """
        self.rules: list[BaseRule] = [
            DuplicateRule(),
        ]


    def evaluate(self, document: dict) -> dict:
        """
        Evaluate a processed document using all registered
        dataset policy rules.

        Creates the shared policy object, executes every
        registered rule, and returns the final policy
        decision.
        """
        
        
        quality = document["quality"]
        
        policy = {
            "accepted": quality["passed"],
            "reasons": list(quality["reasons"]),
        }
        
        for rule in self.rules:
            rule.evaluate(document, policy)
            
        return policy