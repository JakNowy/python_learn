import multiprocessing
import time


def f1(i):
    time.sleep(1)
    print(f'called function in process {i}')


process_jobs = []
for i in range(5):
    process = multiprocessing.Process(target=f1, args=(i, ))
    process_jobs.append(process)
    process.start()
    process.join()
