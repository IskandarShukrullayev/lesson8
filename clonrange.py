def CloneRange(start, stop=None, step=1.0):
    if stop is None:
        stop = start
        start = 0.0
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step

# Example usage:
for i in CloneRange(5, 30, 1.5):
    print(i)