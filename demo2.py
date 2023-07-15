
from asyncio import run, sleep, create_task

async def loopAndSleep(msg, sleepDur):
    for i in range(5):
        await sleep(sleepDur)
        print(msg,i)

async def main():
    a = loopAndSleep('A',1)
    b = loopAndSleep('B',0.7)
    await a
    await b

run(main())
