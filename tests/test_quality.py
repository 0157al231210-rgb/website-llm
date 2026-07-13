from extractor.quality import *


print("Character Count")
print(character_count("Hello"))
print()

print("Word Count")
print(word_count("FastAPI is awesome"))
print()

print("Alphabet Ratio")
print(alphabet_ratio("ABC123"))
print()

print("Empty String")
print(alphabet_ratio(""))
print()

short_text = "Hello"

print("Length Rule (Short)")
print(passes_length(short_text))
print()

long_text = "Python " * 100

print("Length Rule (Long)")
print(passes_length(long_text))
print()

print("Word Count Rule")
print(passes_word_count(long_text))
print()

print("Alphabet Rule")
print(passes_alphabet_ratio(long_text))
print()

bad = "Hello"

print("Bad Sample")
print(is_high_quality(bad))
print()

good = """
FastAPI is a modern Python web framework for building APIs.
""" * 100

print("Good Sample")
print(is_high_quality(good))
print()

symbols = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" * 20

print("Symbols")
print(alphabet_ratio(symbols))
print(is_high_quality(symbols))
print()

numbers = "1234567890 " * 100

print("Numbers")
print(alphabet_ratio(numbers))
print(is_high_quality(numbers))
print()

technical = """
Python classes encapsulate data and behavior.
FastAPI supports dependency injection.
REST APIs exchange JSON data.
""" * 30

print("Technical Text")
print(is_high_quality(technical))
print()