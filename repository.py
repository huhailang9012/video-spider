from datetime import datetime
import uuid
import hashlib

from database_pool import PostgreSql
from preprocessor import extract_cover
from uploader import fpush_video, fpush_image


def count_by_md5(md5: str) -> int:
    """
    select count(*) from videos
    :return: record size
    """
    # sql语句 建表
    sql = """SELECT count(*) FROM videos where md5 = %s;"""
    params = (md5,)
    db = PostgreSql()
    count = db.count(sql, params)
    return count


def insert(id: str, name: str, format: str, md5: str, local_video_path: str, cloud_video_path: str,
           cloud_cover_path: str, size: int, date_created: str):
    sql = """INSERT INTO videos (id, name, format, md5, local_video_path, cloud_video_path, cloud_cover_path, size, date_created) 
                     VALUES
                     (%(id)s, %(name)s, %(format)s, %(md5)s, %(local_video_path)s, %(cloud_video_path)s, %(cloud_cover_path)s, %(size)s, %(date_created)s)"""
    params = {'id': id, 'name': name, 'format': format, 'md5': md5, 'local_video_path': local_video_path,
              'cloud_video_path': cloud_video_path, 'cloud_cover_path': cloud_cover_path, 'size': size,
              'date_created': date_created}
    db = PostgreSql()
    db.execute(sql, params)


def storage(name: str, format: str, local_video_path: str, size: int) -> str:
    """
    storage videos
    :return:
    """
    id = uuid.uuid1().hex
    print(id)
    cloud_video_path = fpush_video(name, local_video_path)
    cover_name, local_cloud_cover_path = extract_cover(local_video_path)
    cloud_cloud_cover_path = fpush_image(cover_name, local_cloud_cover_path)
    with open(local_video_path, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    print(file_md5)
    count = count_by_md5(file_md5)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if count == 0:
        insert(id, name, format, file_md5, local_video_path, cloud_video_path, cloud_cloud_cover_path, size,
               now)
    return file_md5


if __name__ == '__main__':
    print(count_by_md5('5840ff508024f0ce80d04332f8e10109'))
