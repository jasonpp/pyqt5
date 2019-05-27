#协程嵌套

import asyncio
import time

async  def doWork(x):
    print("This is coroutine waiting:",x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

now = lambda :  time.time()

coroutine1 = doWork(1)
coroutine2 = doWork(2)
coroutine3 = doWork(3)


async  def main():
    tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
    ]

    dones, pending = await asyncio.wait(tasks)

    for task in dones:
        print(task.result())

start = now()

loop = asyncio.get_event_loop()

loop.run_until_complete(main())

print("Total use time:", now() - start)

