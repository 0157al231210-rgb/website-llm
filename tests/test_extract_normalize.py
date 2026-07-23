from extractor.normalize import normalize_text


def test_normalize_text():
    """
    Verify that text normalization removes
    unnecessary whitespace while preserving content.
    """

    sample = """
    Python        is      awesome.




    FastAPI\t\tis modern.




    Async programming.
    """

    normalized = normalize_text(sample)

    assert isinstance(normalized, str)

    assert normalized.strip() != ""

    assert "\t" not in normalized

    assert "Python is awesome." in normalized

    assert "FastAPI is modern." in normalized

    assert "Async programming." in normalized