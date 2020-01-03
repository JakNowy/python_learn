import multiprocessing
import time
import concurrent.futures


# READ BOTH WAYS OF RUNNING MULTIPROCESSING TO HAVE A PROPER UNDERSTANDING

# # PART 1: MANUAL MULTIPROCESSING

# # Define function to be executed in a process.
# def do_something(seconds):
#     print(f'Sleeping {seconds} sec')
#     time.sleep(seconds)
#     print('Done sleeping')
#
#
# # Measure start time
# start = time.perf_counter()
#
# # Create Process objects
# p1 = multiprocessing.Process(target=do_something, args=[1, ])
# p2 = multiprocessing.Process(target=do_something, args=[1, ])
# p3 = multiprocessing.Process(target=do_something, args=[1, ])
#
# # Start the processes in parallel
# p1.start()
# p2.start()
# p3.start()
#
# # Wait until the processes complete
# p1.join()
# p2.join()
# p3.join()
#
# # Measure finish time
# finish = time.perf_counter()
#
# # Program takes 1 second instead of 3 seconds due to being run in parallel.
# print(f'Finished in {round(finish - start, 2)} second(s))')


# PART 2: MULTIPROCESSING WITH CONCURRENT.FUTURES MODULE

# # Define function to be executed in a process.
# def do_something(seconds):
#     print(f'Sleeping {seconds} sec')
#     time.sleep(seconds)
#     return f'Done sleeping...{seconds}'
#
#
# # Measure start time
# start = time.perf_counter()
#
# # Create ProcessPool object
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     # Example 1: Simplest way - submit functions one by one to be executed as parallel processes
#     # f1 = executor.submit(do_something, 1)
#     # f2 = executor.submit(do_something, 1)
#     # print(f1.result())
#     # print(f2.result())
#
#     # Example 2: Pro way
#     seconds = [5, 4, 3, 2, 1, -1]  # todo IMPORTANT: Note that only 1 function per processor core may be executed at once.
#                                    # todo With 4 core processors "1" waits for "2" to be executed first.
#
#     # Submit functions, creating future objects to be executed as soon as possible
#     futures = [executor.submit(do_something, sec) for sec in seconds]
#
#     # Call the results upon process completed.
#     for completed_future in concurrent.futures.as_completed(futures):
#         # Potential exceptions must be handled upon calling results, not during submitting
#         try:
#             print(completed_future.result())
#         except ValueError as e:
#             print('EXCEPTION OCCURED:', e)
#
# # Measure finish time
# finish = time.perf_counter()
#
# print(f'Finished in {round(finish - start, 2)} second(s))')
