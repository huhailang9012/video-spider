import requests
protocol = 'http'
ip_addr = '127.0.0.1'
port = '8002'
uri = '/audio/extract'


def notify(file_md5: str, storage_path: str) -> str:
    """
    notify Audio-Extracting to extract audio
    """
    url = protocol + ':' + '//' + ip_addr + ':' + port + uri
    params = {'file_md5': file_md5, 'storage_path': storage_path}
    r = requests.post(url, json=params)
    return r.text
