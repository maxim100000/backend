import httpx

def check_similarity(text_1: str, text_2: str):
    body = {'text_1': text_1,
            'text_2': text_2}
    api_url = 'https://api.api-ninjas.com/v1/textsimilarity'

    response = httpx.post(api_url, headers={
            'X-Api-Key': 'w3u5ivZXPlttcK3e47fetQ==xrn6CLM5WTSYuE8K'},
                                     json=body)
    if response.status_code != httpx.codes.OK:
        raise httpx.HTTPError(message='Something with request or server')
    return response.json()['similarity'] > 0.85   


