from adbutils import adb
from database import repository as repo
import time
import base64
from app import call as c
import requests


# device
remote_addr = '10.170.213.242:21503'
# remote_addr = '10.171.216.55:21503'
adb.connect(remote_addr)
# source directory
src_dir = "/storage/sdcard0/DCIM/Camera/"
# destination directory
dest_dir = "/data/files/videos/"


def install(pkg_path: str = None):
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    Example:
        pkg_path: C:/Users/huhai/Downloads/aweme_aweGW_v1015_130401_becf_1604488554.apk
    """
    d.install(pkg_path, True)


def uninstall(pkg_name: str=None):
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    Example:
        pkg_name: com.ss.android.ugc.aweme
    """
    d.uninstall(pkg_name)


def start(pkg_name: str = 'com.ss.android.ugc.aweme', activity: str = '.main.MainActivity'):
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    Example:
        pkg_name: com.ss.android.ugc.aweme
        activity: .main.MainActivity
    """
    d.app_start(pkg_name, activity)


def stop(pkg_name: str = 'com.ss.android.ugc.aweme'):
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    Example:
        pkg_name: com.ss.android.ugc.aweme
    """
    d.app_stop(pkg_name)


def share():
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    share click
    """
    d.click(980, 1440)


def download():
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    download click
    """
    d.click(250, 1680)


def swipe(sx: int, sy: int, dx: int, dy: int, duration: float):
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    swipe from start point to end point

    Args:
        sx, sy: start point(x, y)
        dx, dy: end point(x, y)
    Example:
        For 540 × 960,
        (sx, sy) = (200, 600)
        (dx, dy) = (200, 200)
    """
    d.swipe(sx, sy, dx, dy, duration)


def pull():
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    Pull file from device:src to local:dst
    Returns:
    file size
    """
    files = d.sync.list(src_dir)
    files = list(filter(lambda x: x.name.find("mp4") != -1, files))
    name = files[0].name
    src = src_dir + name
    print(src)
    dest = dest_dir + name
    size = d.sync.pull(src, dest)
    print("pull size", size)
    return name, "mp4", dest, size, src


def reset():
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    reset click
    """
    d.click(270, 300)


def input_text(key: str = 'faded'):
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    Example:
        search key: faded
    """
    print('execute formally',key)
    charsb64 = str(base64.b64encode(key.encode('utf-8')))[1:]
    d.shell("am broadcast -a ADB_INPUT_B64 --es msg %s" % charsb64)
    # d.send_keys(key)

def search():
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    search click
    """
    d.click(1000, 100)


def bingo():
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    select click
    """
    d.click(150, 250)


def select_video():
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    select video click
    """
    d.click(250, 250)


def select_first():
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    """
    select first video click
    """
    d.click(250, 600)


def execute(key: str = None):
    adb.connect(remote_addr)
    ds = adb.device_list()
    d = ds[0]
    print('search......')
    search()
    time.sleep(2)
    print('input......')
    input_text(key)
    time.sleep(2)
    bingo()
    select_video()
    time.sleep(2)
    select_first()
    time.sleep(2)
    n = 0
    try:
        while n < 20:
            share()
            time.sleep(2)
            download()
            time.sleep(10)
            files = d.sync.list(src_dir)
            files = list(filter(lambda x: x.name.find("mp4") != -1, files))
            print(len(files))
            if len(files):
                name, format, storage_path, size, src = pull()
                d.remove(src)
                id = repo.storage(name, format, storage_path, size)
                c.notify(id, key, storage_path)
                time.sleep(3)
            else:
                reset()
            swipe(200, 1400, 200, 500, 0.5)
            n = n + 1
            time.sleep(2)
    except KeyboardInterrupt:
        adb.run('kill-server')


def notify(video_id: str, related_key: str, local_video_path: str) -> str:
    """
    notify Audio-Extracting to extract audio
    """
    url = 'http://management:8000/spider/callback'
    payload = {'video_id': video_id, 'related_key': related_key, 'local_video_path': local_video_path}
    r = requests.get(url, params=payload)
    return r.text

if __name__ =='__main__':
    # search()
    input_text('中国')
