import requests
import re


def data_filter(api_url):
    response = requests.get(api_url)
    pattern = re.compile(r'"id":\s(\d+)[^"]+"title":\s"([^"]+)')
    api_json = []

    for match in pattern.finditer(response.text):
        api_id = match.group(1)
        api_title = match.group(2)
        api_json.append(
            {
                "id": api_id,
                "title": api_title,
            },
        )

    return api_json

