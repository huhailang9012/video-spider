import cv2
import os


def extract_cover(storage_path: str):
    """
	extract cover image from video
	"""
    dir = os.path.dirname(storage_path)
    video_name = os.path.basename(storage_path)
    prefix_name = video_name.split('.')[0]
    cover_name = prefix_name + '.jpg'
    vidcap = cv2.VideoCapture(storage_path)
    success, image = vidcap.read()
    n = 1
    while n < 30:
        success, image = vidcap.read()
        n += 1
    imag = cv2.imwrite(os.path.join(dir, cover_name), image)
    if imag:
        print('ok')
    return cover_name, dir + '/' + cover_name


if __name__ == "__main__":
    print(extract_cover('E:/douyin/download/20201108130244.mp4'))