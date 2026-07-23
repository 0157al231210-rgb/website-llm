from extractor.pipeline import extract
from extractor.text import extract_text


def test_extract_text():
    """
    Verify that text extraction returns
    meaningful content from HTML.
    """

    with open(
        "datasets/raw/quotes_dataset/page_000001.html",
        encoding="utf-8",
    ) as file:
        html = file.read()

    tag = extract(html)

    text = extract_text(tag)

    assert isinstance(text, str)
    assert text.strip() != ""
    assert len(text) > 100