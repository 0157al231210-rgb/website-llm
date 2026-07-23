from extractor.pipeline import extract


def test_extract():
    """
    Verify that the extraction pipeline
    returns the primary content node.
    """

    with open(
        "datasets/raw/quotes_dataset/page_000001.html",
        encoding="utf-8",
    ) as file:
        html = file.read()

    best = extract(html)

    assert best is not None

    assert best.get_text(strip=True) != ""

    assert len(best.get_text()) > 100