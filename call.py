import requests


def notify(video_id: str, related_key: str, storage_path: str) -> str:
    """
    notify Audio-Extracting to extract audio
    """
    url = 'http://127.0.0.1:8000/spider/callback'
    params = {'video_id': video_id, 'related_key': related_key, 'storage_path': storage_path}
    r = requests.post(url, json=params)
    return r.text
