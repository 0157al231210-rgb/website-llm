"""
Base class for dataset policy rules.

Every dataset rule must implement the evaluate()
method.

Rules inspect a document and may update the shared
policy object.
"""

from abc import ABC, abstractmethod


class BaseRule(ABC):
    """
    Base interface for all dataset policy rules.
    """
    
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    
    @abstractmethod
    def evaluate(
        self,
        document: dict,
        policy: dict,
    ) -> None:
        """
        Evaluate a document and update the shared
        policy object.

        Args:
            document:
                The processed document produced by the
                dataset pipeline.

            policy:
                Shared policy object that rules may
                modify.
        """
        pass