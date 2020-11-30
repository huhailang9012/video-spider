from fastapi import FastAPI, Query
from app import spider as sp
import threading
from typing import List
import json
from database.repository import select_by_ids
from app.thread import stop_thread, MyThread

app = FastAPI()
semaphore = threading.BoundedSemaphore(2)

@app.post("/app/install")
def install(pkg_path: str = None):

    sp.install(pkg_path)
    return {"success": True, "code": 0, "msg": "ok"}


@app.post("/app/start")
def start(pkg_name: str, activity: str):

    sp.start(pkg_name, activity)
    return {"success": True, "code": 0, "msg": "ok"}


@app.post("/app/execute/{key}")
async def execute(key: str):

    if threading.activeCount() > 1:
        print('remove thread', threading.enumerate()[1].name)
        stop_thread(threading.enumerate()[1])
        # semaphore.release()
        t = MyThread(key)
        t.start()
        # thread_pool.append(t)
    else:
        t = MyThread(key)
        t.start()
        # thread_pool.append(t)
    print('main thread()',threading.main_thread())
    print('active thread count',threading.activeCount())
    print('active threads',threading.enumerate())
    # print('total sub thread',len(thread_pool))
    # if len(thread_pool) > 0:
    #     for i in thread_pool:
    #         print(i.name)
    return {"success": True, "code": 0, "msg": "ok"}


@app.post("/app/stop")
def stop(pkg_name: str):

    sp.stop(pkg_name)
    return {"success": True, "code": 0, "msg": "ok"}


@app.get("/video/batch/query")
def batch_query(video_ids: List[str] = Query(None)):
    data = select_by_ids(video_ids)
    result = json.dumps(data, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)
    return {"success": True, "code": 0, "msg": "ok", "data": result}