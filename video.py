
class Video(object):

    def __init__(self, id: str, name: str, md5: str, format: str, local_video_path: str,cloud_video_path: str,cloud_cover_path: str,
                 size: int, date_created: str):
        self.id = id
        self.name = name
        self.md5 = md5
        self.cloud_video_path = cloud_video_path
        self.local_video_path = local_video_path
        self.cloud_cover_path = cloud_cover_path
        self.format = format
        self.date_created = date_created
        self.size = size