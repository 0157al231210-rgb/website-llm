from bs4 import BeautifulSoup

def parse(html):
    
    soup = BeautifulSoup(html, "lxml")

    title = soup.title.text.strip() if soup.title else "No Title"

    headings = []

    for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        for heading in soup.find_all(tag):
            headings.append(heading.text.strip())

    paragraphs = []

    for p in soup.find_all("p"):
        paragraphs.append(p.text.strip())

    links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            links.append(href)

    page_data = {
        "title": title,
        "headings": headings,
        "paragraphs": paragraphs,
        "links": links
    }

    return page_data, links