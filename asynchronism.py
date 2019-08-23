import concurrent.futures
import time

number_list = list(range(1, 11))


def evaluate_item(x: int):
    result_item = count(x)
    print(f'item {x} result P{result_item}')


def count(number):
    for i in range(100000):
        i = i+1
    return i * number


# Sequential execution
start_time = time.clock()
for item in number_list:
    evaluate_item(item)
print(f'Sequential execution in {time.clock() - start_time} seconds.')


# Thread pool execution
start_time_thread = time.clock()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for item in number_list:
        evaluate_item(item)
    print(f'Thread execution in {time.clock() - start_time_thread} seconds.')


# Process pool execution
start_time_process = time.clock()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for item in number_list:
        evaluate_item(item)
    print(f'Process execution in {time.clock() - start_time_process} seconds.')
