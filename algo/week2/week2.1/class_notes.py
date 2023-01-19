# import time
# import statistics
# arr = list(range(100000))

# NUM_TRIALS = 10000
# times = []

# for i in range(NUM_TRIALS):
#     before = time.perf_counter()
#     arr.append(999)
#     after = time.perf_counter()
#     arr.pop(49999)
#     difference = (after - before) * 1e9
#     times.append(difference)

# print("mean", statistics.mean((times)))
# print("median", statistics.median((times)))
# print("stdev", statistics.stdev((times)))


# import time
# import statistics
# arr = list(range(10000))

# NUM_TRIALS = 1000
# times = []

# for i in range(NUM_TRIALS):
#     before = time.perf_counter()
#     middle = len(arr)/2
#     if middle in arr:
#         arr.remove(middle)

#     after = time.perf_counter()
#     # arr.pop()
#     difference = (after - before) * 1e9
#     times.append(difference)

# print("mean", statistics.mean((times)))
# print("median", statistics.median((times)))
# print("stdev", statistics.stdev((times)))


class algo:
    def bubble_sort(arr: list) -> list[float]:
        arr = [5, 8, 2, 6, -42, 1.111]
        for num in arr:
            if num[0] < num[1]:
                pass
