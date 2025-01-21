from fastapi import FastAPI
import threading
import time
import os  

app = FastAPI()

def threaded_funtion(old_thread):
    while True:
        print("Running this thread")
        os.environ["VALUE"] = str(time.time())
        time.sleep(20)

current_thread = threading.current_thread()


sub_thread = threading.Thread(target=threaded_funtion, kwargs={"old_thread":current_thread})
sub_thread.start()


@app.get("/")
def gell():
    # print(threading.current_thread())
    # print(threading.main_thread())
    print(os.getenv("VALUE"))
    return {"hello":"world"}