from dataset.writer import DatasetWriter
from pipeline.dataset_pipeline import DatasetPipeline
from pipeline.quality_filter import QualityFilter


def test_dataset_pipeline():
    """
    Verify that the complete dataset pipeline
    processes, evaluates, filters, and writes
    a valid document.
    """

    quality_filter = QualityFilter()

    accepted = DatasetWriter(
        output_dir="tests/output",
        filename="accepted.jsonl",
    )

    rejected = DatasetWriter(
        output_dir="tests/output",
        filename="rejected.jsonl",
    )

    pipeline = DatasetPipeline(
        accepted,
        rejected,
        quality_filter,
    )

    html = """
    <html>
    <body>

    <article>

    <h1>FastAPI Tutorial</h1>

    <p>
    """ + ("FastAPI is awesome. " * 200) + """

    </p>

    </article>

    </body>
    </html>
    """

    document = pipeline.process(
        "https://example.com",
        html,
    )

    assert document["quality"]["passed"] is True

    assert document["policy"]["accepted"] is True

    assert accepted.get_document_count() == 1

    assert rejected.get_document_count() == 0

    assert accepted.filepath.exists()