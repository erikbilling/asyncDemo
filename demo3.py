
from asyncio import run, sleep, create_task, gather, wait

async def loopAndSleep(msg, sleepDur):
    for i in range(5):
        await sleep(sleepDur)
        print(msg,i)

async def main():
    a = create_task(loopAndSleep('A',1))
    b = create_task(loopAndSleep('B',0.7))
    await gather(a,b)

run(main())
