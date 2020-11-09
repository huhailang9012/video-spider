from adbutils import adb
import time
import storage as db

# device
ds = adb.device_list()
d = ds[0]
# pkg_path
pkg_path = "C:/Users/huhai/Downloads/aweme_aweGW_v1015_130401_becf_1604488554.apk"
# pkg_name
pkg_name = "com.ss.android.ugc.aweme"
# activity
activity = ".main.MainActivity"
# source directory
src_dir = "/storage/sdcard0/DCIM/Camera/"
# destination directory
dest_dir = "E:/douyin/download/"


def install():
    """
    Example:
        pkg_path: C:/Users/huhai/Downloads/aweme_aweGW_v1015_130401_becf_1604488554.apk
    """
    d.install(pkg_path, True)


def uninstall():
    """
    Example:
        pkg_name: com.ss.android.ugc.aweme
    """
    d.uninstall(pkg_name)


def start():
    """
    Example:
        pkg_name: com.ss.android.ugc.aweme
        activity: .main.MainActivity
    """
    # d.app_start(pkg_name, activity)
    cmd = "adb shell am start -W -S " + "com.ss.android.ugc.aweme" + "/" + ".main.MainActivity"


def stop():
    """
    Example:
        pkg_name: com.ss.android.ugc.aweme
    """
    d.app_stop(pkg_name)


def share():
    """
    share click
    """
    d.click(980, 1500)


def download():
    """
    download click
    """
    d.click(250, 1680)


def swipe(sx: int, sy: int, dx: int, dy: int, duration: float):
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
    """
    reset click
    """
    d.click(270, 300)


def input_text():
    """
    Example:
        search key: faded
    """
    d.send_keys("faded") # simulate: adb shell input text "hello%sworld\%\^\&\*


def search():
    """
    search click
    """
    d.click(1000, 100)


def bingo():
    """
    select click
    """
    d.click(150, 250)


def select_video():
    """
    select video click
    """
    d.click(250, 250)


def select_first():
    """
    select first video click
    """
    d.click(250, 400)


def run():

    start()
    time.sleep(10)
    search()
    time.sleep(0.5)
    input_text()
    time.sleep(0.5)
    bingo()
    select_video()
    time.sleep(1)
    select_first()
    time.sleep(1)

    try:
        while True:
            share()
            time.sleep(0.5)
            download()
            time.sleep(10)
            files = d.sync.list(src_dir)
            files = list(filter(lambda x: x.name.find("mp4") != -1, files))
            print(len(files))
            if len(files):
                name, format, storage_path, size, src = pull()
                d.remove(src)
                print("remove file", src)
                db.storage(name, format, storage_path, size)
                time.sleep(5)
            else:
                reset()
            swipe(200, 1000, 200, 500, 0.5)
    except KeyboardInterrupt:
        adb.run('kill-server')


if __name__ == "__main__":
    run()