from extractor.normalize import normalize_text

sample = """
Python        is      awesome.




FastAPI\t\tis modern.




Async programming.
"""

print("Before:")
print(repr(sample))

print("\nAfter:")
print(repr(normalize_text(sample)))