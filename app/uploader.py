# 引入MinIO包。
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)
video_bucket = 'videos'
image_bucket = 'images'
endpoint = 'minio:9000'

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio(endpoint,
                    access_key='AKIAIOSFODNN7EXAMPLE',
                    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                    secure=False)


def fpush_video(object_name: str, file_path: str):
    """
    push a video to remote server
    """
    # 调用make_bucket来创建一个存储桶。
    try:
        if not minioClient.bucket_exists(video_bucket):
            minioClient.make_bucket(video_bucket, location="us-east-1")
            # todo
            # minioClient.set_bucket_policy(video_bucket,
            #                               {"policy": "Read-And-Write"})
    except BucketAlreadyOwnedByYou as err:
        pass
    except BucketAlreadyExists as err:
        pass
    except ResponseError as err:
        raise
    else:
        try:
            minioClient.fput_object(video_bucket, object_name, file_path)
        except ResponseError as err:
            print(err)
    return 'http://' + endpoint + "/" + video_bucket + "/" + object_name


def fpush_image(object_name: str, file_path: str):
    """
    push a image to remote server
    """
    # 调用make_bucket来创建一个存储桶。
    try:
        if not minioClient.bucket_exists(image_bucket):
            minioClient.make_bucket(image_bucket, location="us-east-1")
            # todo
            # minioClient.set_bucket_policy(image_bucket, 'Read-And-Write')
    except BucketAlreadyOwnedByYou as err:
        pass
    except BucketAlreadyExists as err:
        pass
    except ResponseError as err:
        raise
    else:
        try:
            print(minioClient.fput_object(image_bucket, object_name, file_path))
        except ResponseError as err:
            print(err)
    return 'http://' + endpoint + "/" + image_bucket + "/" + object_name


if __name__ == "__main__":
    print(fpush_video('0b03f867d40d87d3ef191119874c1b4e.mp4', 'E:/docker_data/files/videos/0b03f867d40d87d3ef191119874c1b4e.mp4'))
