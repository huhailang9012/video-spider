FROM python:3.8

MAINTAINER Jerry<huhailang@yahoo.cn>
RUN pip install fastapi uvicorn requests minio adbutils psycopg2 opencv-python -i https://mirrors.aliyun.com/pypi/simple/

#RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
#RUN apt-get clean
#ADD sources.list /etc/apt/
RUN apt update
RUN apt install -y libgl1-mesa-glx
RUN wget www.baidu.com
RUN apt install -y android-tools-adb
RUN adb version
WORKDIR /code

RUN cd /code
CMD uvicorn controller:app --reload --port 8000 --host 0.0.0.0