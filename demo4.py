
from asyncio import run, sleep, create_task, gather, wait, FIRST_COMPLETED

async def loopAndSleep(msg, sleepDur):
    for i in range(5):
        await sleep(sleepDur)
        print(msg,i)

async def main():
    await gather(loopAndSleep('A',1), loopAndSleep('B',0.7))
    
run(main())
