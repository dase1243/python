import sys

num_steps = int(sys.argv[1])
i = num_steps - 1
while i != -1:
    print(" " * i + "#" * (num_steps - i))
    i -= 1
