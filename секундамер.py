import time
def stopwatch():
    for i in range(0,24):
        for j in range(1,60):
                time.sleep(1)
                print(f"{i:02d}:{j:02d}")
stopwatch()
