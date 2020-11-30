import requests

def notify(video_id: str, related_key: str, local_video_path: str) -> str:
    """
    notify Audio-Extracting to extract audio
    """
    url = 'http://management:8000/spider/callback'
    payload = {'video_id': video_id, 'related_key': related_key, 'local_video_path': local_video_path}
    r = requests.get(url, params=payload)
    return r.text
