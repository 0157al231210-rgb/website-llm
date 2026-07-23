from extractor.pipeline import process_html


def test_process_html():
    """
    Verify that the HTML processing pipeline
    extracts meaningful normalized text.
    """

    with open(
        "datasets/raw/quotes_dataset/page_000001.html",
        encoding="utf-8",
    ) as file:
        html = file.read()

    text = process_html(html)

    assert isinstance(text, str)
    assert text.strip() != ""
    assert len(text) > 100

    # Replace with text you know exists in your sample page
    assert "Albert Einstein" in text