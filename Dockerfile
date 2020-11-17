FROM python:3.8

MAINTAINER Jerry<huhailang@yahoo.cn>
RUN pip install fastapi uvicorn requests minio adbutils psycopg2 opencv-python -i https://mirrors.aliyun.com/pypi/simple/
RUN apt update
RUN apt install libgl1-mesa-glx
WORKDIR /code
COPY ./ /code/
RUN cd /code


CMD uvicorn controller:app --reload --port 8000 --host 0.0.0.0