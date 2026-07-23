from dataset.writer import DatasetWriter
import json


def test_dataset_writer():
    """
    Verify that DatasetWriter writes documents
    and correctly tracks the number of documents.
    """

    accepted_writer = DatasetWriter(
        output_dir="tests/output",
        filename="accepted.jsonl",
    )

    rejected_writer = DatasetWriter(
        output_dir="tests/output",
        filename="rejected.jsonl",
    )

    good_document = {
        "url": "https://good.com",
        "text": "High quality text",
        "quality": {
            "passed": True,
        },
    }

    bad_document = {
        "url": "https://bad.com",
        "text": "Hi",
        "quality": {
            "passed": False,
        },
    }

    for document in (good_document, bad_document):
        if document["quality"]["passed"]:
            accepted_writer.write(document)
        else:
            rejected_writer.write(document)

    assert accepted_writer.get_document_count() == 1
    assert rejected_writer.get_document_count() == 1