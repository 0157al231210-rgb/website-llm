from urllib.parse import (
    urljoin,
    urlparse,
    urlunparse,
    parse_qsl,
    urlencode,
)

TRACKING_PARAMS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "gclid",
    "fbclid",
    "msclkid",
    "ttclid",
    "mc_eid",
}

def normalize_url(current_url, link):

    absolute_url = urljoin(current_url, link)

    parsed = urlparse(absolute_url)

    netloc = parsed.netloc.lower()

    path = parsed.path

    if path != "/":
        path = path.rstrip("/")
        
    query_params = parse_qsl(parsed.query, keep_blank_values=True)

    filtered_params = [
        (key, value)
        for key, value in query_params
        if key not in TRACKING_PARAMS
    ]
    
    filtered_params = sorted(filtered_params)

    normalized_query = urlencode(filtered_params)

    normalized = urlunparse((
        parsed.scheme,
        netloc,
        path,
        parsed.params,
        normalized_query,
        ""
    ))
    
    return normalized    