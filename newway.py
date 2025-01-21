import asyncio
import threading

from app import threaded_funtion

async def some_callback(args):
    await threaded_funtion()

def between_callback(args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(some_callback(args))
    loop.close()

_thread = threading.Thread(target=between_callback, args=("some text"))
_thread.start()