import builtins
import sys
import time

def slow_print(*args, sep=' ', end='\n', delay=0.01, per_line_pause=0.1):
    text = sep.join(map(str, args))

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.flush()
    time.sleep(per_line_pause)

origin_print = builtins.print
origin_input = builtins.input

def slow_input(prompt="", delay=0.005):
    slow_print(prompt, end="", delay=delay)
    return origin_input()

def enable():
    builtins.print = slow_print
    builtins.input = slow_input

def disable():
    builtins.print = origin_print
    builtins.input = origin_input
