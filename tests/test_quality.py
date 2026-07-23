from extractor.quality import evaluate_quality


def test_high_quality_document():
    """
    Verify that a high-quality document
    passes the quality evaluation.
    """

    good = """
    FastAPI is a modern Python framework.
    """ * 100

    result = evaluate_quality(good)

    assert result["passed"] is True
    assert result["reasons"] == []


def test_low_quality_document():
    """
    Verify that a low-quality document
    fails the quality evaluation.
    """

    bad = "Hello"

    result = evaluate_quality(bad)

    assert result["passed"] is False
    assert len(result["reasons"]) > 0