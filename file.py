import os


def split_name():
    path = "C:/Users/huhai/Downloads/aweme_aweGW_v1015_130401_becf_1604488554.apk"
    name = os.path.basename(path)
    print(name)


if __name__ == "__main__":
    split_name()