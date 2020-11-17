from fastapi import FastAPI
import spider as sp
import threading

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


@app.post("/app/run")
async def run(key: str):
    print("key",key)
    if threading.activeCount() == 1:
        print("当前活跃线程数为1")
        t = MyThread(key)
        t.start()
        thread_pool.append(t)
    elif threading.activeCount() == 2:
        print("当前活跃线程数为2")
        print(thread_pool[0].name)
        stop_thread(thread_pool[0])
        t = MyThread(key)
        print(t.name)
        t.start()
        thread_pool.append(t)
    return {"success": True, "code": 0, "msg": "ok"}


@app.post("/app/stop")
def stop(pkg_name: str):

    sp.stop(pkg_name)
    return {"success": True, "code": 0, "msg": "ok"}