import builtins
import sys
import time

# Save the original print and input functions
# so they can be restored later if needed.
origin_print = builtins.print
origin_input = builtins.input


# -------------------------------
# SLOW TEXT PRINTING FUNCTION
# -------------------------------
def slow_print(*args, sep=' ', end='\n', delay=0.01, per_line_pause=0.1):
    # Combine all arguments into a single string
    text = sep.join(map(str, args))

    # Print the text one character at a time
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)      # delay between characters

    # End of line
    sys.stdout.write(end)
    sys.stdout.flush()

    time.sleep(per_line_pause)  # short pause after the whole line


# -------------------------------
# SLOW INPUT (like in games/visual novels)
# -------------------------------
def slow_input(prompt="", delay=0.005):
    # Slowly print the input prompt
    slow_print(prompt, end="", delay=delay)
    # Then read the user's input
    return origin_input()


# -------------------------------
# ENABLE SLOW PRINT
# -------------------------------
def enable():
    # Replace built-in print with slow_print and input with slow_input
    builtins.print = slow_print
    builtins.input = slow_input