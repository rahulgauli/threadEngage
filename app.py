import asyncio
from fastapi import FastAPI
import threading
import time
import os  

app = FastAPI()


async def threaded_funtion(old_thread):
    while old_thread.is_alive():
        print("Running this thread")
        os.environ["VALUE"] = str(time.time())
        print(os.getenv("VALUE"))
        time.sleep(10)


# async def some_callback(args):
#     await threaded_funtion()


def between_callback(old_thread):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(threaded_funtion(old_thread))
    loop.close()

current_thread = threading.current_thread()

_thread = threading.Thread(target=between_callback, kwargs={"old_thread":current_thread})
_thread.start()




# sub_thread = threading.Thread(target=asyncio.run(threaded_funtion), kwargs={"old_thread":current_thread})
# sub_thread.start()


@app.get("/")
def gell():
    print(os.getenv("VALUE"))
    return {"hello":"world"}