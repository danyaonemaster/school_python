import itertools
import threading
import time
import sys
import random

def loading_animation(message="Processing", completion_message = "Done!", duration= random.choice([4,6])):
    done = False
    def animate():
        for c in itertools.cycle(['.', '..', '...', '']):
            if done:
                break
            sys.stdout.write(f"\r{message}{c}")
            sys.stdout.flush()
            time.sleep(0.5)
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(duration)
    done = True
    if completion_message != 0:
        print(f"\r{completion_message}", ""*20)

def timer():
    time.sleep(4)

