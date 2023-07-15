
from time import sleep

def loopAndSleep(msg, sleepDur):
    for i in range(5):
        sleep(sleepDur)
        print(msg,i)

def main():
    loopAndSleep('A',1)
    loopAndSleep('B',0.7)

main()
