from extractor.dom import create_dom, get_all_nodes
from extractor.cleaner import remove_unwanted_tags


def test_remove_unwanted_tags():
    """
    Verify that unwanted HTML tags are removed while
    preserving meaningful content.
    """

    html = """
    <html>

    <head>

    <style>
    body { color:red; }
    </style>

    <script>
    alert("Hello");
    </script>

    </head>

    <body>

    <nav>
    Home
    About
    </nav>

    <main>

    <h1>FastAPI</h1>

    <p>
    FastAPI is a modern Python framework.
    </p>

    </main>

    <footer>
    Copyright
    </footer>

    </body>

    </html>
    """

    soup = create_dom(html)

    remove_unwanted_tags(soup)

    tag_names = [
        tag.name
        for tag in get_all_nodes(soup)
    ]

    # Unwanted tags should be removed
    assert "script" not in tag_names
    assert "style" not in tag_names
    assert "nav" not in tag_names
    assert "footer" not in tag_names

    # Useful tags should remain
    assert "main" in tag_names
    assert "h1" in tag_names
    assert "p" in tag_names