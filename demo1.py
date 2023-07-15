
from asyncio import run, sleep, create_task

async def loopAndSleep(msg, sleepDur):
    for i in range(5):
        await sleep(sleepDur)
        print(msg,i)

async def main():
    a = create_task(loopAndSleep('A',1.5))
    b = create_task(loopAndSleep('B',1))
    await a
    await b

run(main())
