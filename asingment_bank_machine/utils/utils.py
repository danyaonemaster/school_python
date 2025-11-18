# -------------------------------
# LOADING ANIMATION (rotating dots)
# -------------------------------
import itertools
import threading
import time
import sys
import random

def loading_animation(message="Processing",
                      completion_message="Done!",
                      duration=random.choice([4, 6])):
    done = False

    # Internal function — runs the animation
    def animate():
        # Loop through '.', '..', '...', '' repeatedly
        for c in itertools.cycle(['.', '..', '...', '']):
            if done:
                break
            sys.stdout.write(f"\r{message}{c}")
            sys.stdout.flush()
            time.sleep(0.5)

    # Start animation in a separate thread
    t = threading.Thread(target=animate)
    t.start()

    # Keep animation running for 'duration' seconds
    time.sleep(duration)
    done = True

    # Print final completion message
    if completion_message != 0:
        print(f"\r{completion_message}", "" * 20)


# -------------------------------
# TIMER (simple delay)
# -------------------------------
def timer():
    time.sleep(4)

