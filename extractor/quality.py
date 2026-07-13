"""
Quality filtering utilities for extracted text.

This module evaluates whether normalized text is suitable for inclusion
in the AI training dataset. It applies lightweight heuristic rules to
remove low-quality, noisy, or uninformative documents before dataset
creation.

Current quality checks:
- Character count
- Word count
- Alphabetic character ratio

The implementation follows the Single Responsibility Principle by keeping
each quality rule independent and composable. This design allows new
filters, such as language detection, repetition analysis, readability
scoring, or entropy estimation, to be added without modifying the existing
architecture.

Pipeline Position:
    Raw HTML
        ↓
    Content Extraction
        ↓
    Text Normalization
        ↓
    Quality Filtering   ← This module
        ↓
    AI Training Dataset

Main Entry Point:
    is_high_quality(text)
"""


MIN_CHARACTERS = 300
MAX_CHARACTERS = 100_000

MIN_WORDS = 50

MIN_ALPHABET_RATIO = 0.50


def character_count(text: str) -> int:
    return len(text)


def word_count(text: str) -> int:
    return len(text.split())


def alphabet_ratio(text: str) -> float:
    if not text:
        return 0.0
    
    letters = sum(char.isalpha() for char in text)
    
    return letters / len(text)


def passes_length(text: str) -> bool:
    length = character_count(text)
    
    return MIN_CHARACTERS <= length <= MAX_CHARACTERS


def passes_word_count(text: str) -> bool:
    return word_count(text) >= MIN_WORDS


def passes_alphabet_ratio(text: str) -> bool:
    return alphabet_ratio(text) >= MIN_ALPHABET_RATIO



def is_high_quality(text: str) -> bool:
    return (
        passes_length(text)
        and passes_word_count(text)
        and passes_alphabet_ratio(text)
    )