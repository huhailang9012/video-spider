import psycopg2
from datetime import datetime
import uuid
import hashlib


def insert(id: str, name: str, format: str, md5: str, storage_path: str, size: int, date_created: str):
    """
    insert into videos
    :return:
    """
    # connect
    conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
    # cursor
    cursor = conn.cursor()
    sql = """INSERT INTO videos (id, name, format, md5, storage_path, size, date_created) 
             VALUES
             (%(id)s, %(name)s, %(format)s, %(md5)s, %(storage_path)s, %(size)s, %(date_created)s)"""
    params = {'id': id, 'name': name, 'format': format, 'md5': md5, 'storage_path': storage_path, 'size': size, 'date_created': date_created}
    # 执行语句
    cursor.execute(sql, params)
    print("successfully")
    # 事物提交
    conn.commit()
    # 关闭数据库连接
    conn.close()


def count_by_md5(md5: str) -> int:
    """
    select count(*) from videos
    :return: record size
    """
    # connect
    conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
    # cursor
    cursor = conn.cursor()
    # sql语句 建表
    sql = """SELECT count(*) FROM videos where md5 = %s;"""
    params = (md5,)
    # 执行语句
    cursor.execute(sql, params)
    # 抓取
    row = cursor.fetchone()
    # 事物提交
    conn.commit()
    # 关闭数据库连接
    cursor.close()
    conn.close()
    return row[0]


def storage(name: str, format: str, storage_path: str, size: int):
    """
    storage videos
    :return:
    """
    id = uuid.uuid1().hex
    print(id)
    with open(storage_path, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    print(file_md5)
    count = count_by_md5(file_md5)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if count == 0:
        insert(id, name, format, file_md5, storage_path, size, now)