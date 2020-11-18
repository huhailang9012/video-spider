from fastapi import FastAPI, Query
import spider as sp
import threading
from typing import List
import json
from repository import select_by_ids
from thread import stop_thread, thread_pool, MyThread

app = FastAPI()


@app.post("/app/install")
def install(pkg_path: str = None):

    sp.install(pkg_path)
    return {"success": True, "code": 0, "msg": "ok"}


@app.post("/app/start")
def start(pkg_name: str, activity: str):

    sp.start(pkg_name, activity)
    return {"success": True, "code": 0, "msg": "ok"}


@app.post("/app/execute")
async def execute(key: str):
    print("key",key)
    if threading.activeCount() == 1:
        t = MyThread(key)
        t.start()
        thread_pool.append(t)
    elif threading.activeCount() == 2:
        stop_thread(thread_pool[0])
        t = MyThread(key)
        t.start()
        thread_pool.append(t)
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