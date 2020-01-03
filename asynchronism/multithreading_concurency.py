import random
import concurrent.futures
import time
import threading

# READ BOTH WAYS OF RUNNING MULTITHREADING TO HAVE A PROPER UNDERSTANDING

# PART 1: MANUAL MULTITHREADING

# Define function to be executed in a process.
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# Measure start time
start = time.perf_counter()

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    # Make the main thread wait until sub-threads terminate.
    thread.join()

# Measure finish time
finish = time.perf_counter()
# # Program takes 1.5 second instead of 15 seconds due to being run concurrently.
print(f'Finished in {round(finish - start, 2)} second(s))')


# PART 2: MULTITHREADING WITH CONCURRENT.FUTURES MODULE

# Define function to be executed in a process.
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# Measure start time
start = time.perf_counter()

# Create ThreadPool object and submit functions to be executed as concurrent threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Example 1: Simplest way - submit functions one by one to be executed as concurrent threads.
    futures = [executor.submit(do_something, random.randint(-10, 10)) for _ in range(10)]

    # Call the results upon thread completed.
    for completed_future in concurrent.futures.as_completed(futures):
        # Potential exceptions must be handled upon calling results, not during submitting
        try:
            print(completed_future.result())
        except ValueError as e:
            print('EXCEPTION OCCURED:', e)

# Measure finish time
finish = time.perf_counter()
# Program takes just 2 seconds to being run concurrently.
print(f'Finished in {round(finish - start, 2)} second(s))')
