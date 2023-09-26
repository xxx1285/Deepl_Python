
TINYURL = {
    "request": {
                "url": url,
                "domain": "tiny.one",
                "tags": "example,link",
                "expires_at": "null"
            },
    "response":{
                "tiny_url": "https://tinyurl.com/example-alias",
    }
}

REBRANDLY = {
    "request": {
                "api_key": "YOUR_REBRANDLY_API_KEY",
                "workspace": "YOUR_WORKSPACE_ID",
                "base_url": url,
            },
    "response":{

    }
}

OWO = {
    "request": {
                "link": url,
                "generator": "owo",
                "metadata": "OWOIFY"
            },
    "response":{

    }
}

SHRTCO_DE = {
    "request": {
                "link": f"https://api.shrtco.de/v2/shorten?url={url}",
            },
    "response":{

    }
}
