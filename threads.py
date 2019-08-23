import threading
import time

"""
# THREADS #
"""


class MyThread(threading.Thread):

    def __init__(self, name, store_function=None, print_arg=None):
        super(MyThread, self).__init__()
        self.name = name
        self.store_function = store_function
        self.print_arg = print_arg

    # Instructions of a thread
    def run(self):
        if self.print_arg:
            self.store_function(self.print_arg)
        else:
            self.store_function()


"""
# LOCK #

Lock - once .acquire() locks the resource, it's unavailable to .acquire() anywhere else in the code until .release()
RLock - locks the resource, but it's still available to .acquire() for the same thread

"""
# shared_resource_lock = threading.Lock()
# shared_resource_with_lock = None
# shared_resource_without_lock = None
#
#
# def print_name_with_lock(name):
#     global shared_resource_with_lock
#     shared_resource_lock.acquire()  # locks shared resource, no thread can access it
#
#     # NOTE: using RLock here would work, as it doesnt block resource for the original thread
#     # simple Lock would result in a deadlock situation
#     # shared_resource_lock.acquire()
#
#     shared_resource_with_lock = name
#     time.sleep(2)
#     print(f'Function with lock:')
#     print(shared_resource_with_lock)
#     shared_resource_lock.release()  # unlocks shared resource
#
#
# def print_name_without_lock(name):
#     global shared_resource_without_lock
#     shared_resource_without_lock = name
#     time.sleep(2)
#     print(f'Function without lock:')
#     print(shared_resource_without_lock)


# lock_thread1 = MyThread('', store_function=print_name_with_lock, print_arg='Jan')
# lock_thread2 = MyThread('', store_function=print_name_with_lock, print_arg='Jakub')
#
# no_lock_thread1 = MyThread('', store_function=print_name_without_lock, print_arg='Jan')
# no_lock_thread2 = MyThread('', store_function=print_name_without_lock, print_arg='Jakub')
#
# # Shared resource locked while executing, thread2 wait for thread1 to release the lock
# lock_thread1.start()  # Jan
# lock_thread2.start()  # Jakub
#
# time.sleep(5)
# print()
#
# # Shared resource not locked - executed simultaneously and overridden meantime execution:
# no_lock_thread1.start()  # Jakub
# no_lock_thread2.start()  # Jakub

"""
# SEMAPHORE #

semaphore is a kind of variable that gets locks and releases resources based on it's value
- negative value blocks them, positive releases them.

acquire() method decrements the number of available "semaphore points" while,
release() increments it.
"""


# class Store:
#     semaphore = threading.Semaphore(2)  # 2 semaphore points, designed to protect initial value of len(list) = 2
#     # locks once the number of available points drops to 0 ()
#     items = [1, 2]
#     next_item_id = 3
#
#     def consume(self):
#         # Acquire a semaphore point
#         self.semaphore.acquire()  # Consumes single semaphore point, guards the "items" resource
#         # The consumer has access to the shared resource
#         time.sleep(1)
#         consumed_item = self.items.pop(0)
#         print(f'Consumed item {consumed_item}\n{len(self.items)} items left.\n')
#
#     def produce(self):
#         time.sleep(1)
#         self.items.append(self.next_item_id)  # Create new item
#         self.next_item_id += 1
#         print(f'Produced item {self.items[-1]}\n{len(self.items)} items left.\n')
#         self.semaphore.release()  # Releases a semaphore point, now there is new one to consume (as there's a new item)


# store = Store()
# producer_thread1 = MyThread('Producer thread', store.produce)
# producer_thread2 = MyThread('Producer thread', store.produce)
# producer_thread3 = MyThread('Producer thread', store.produce)
#
# consumer_thread1 = MyThread('Consumer thread', store.consume)
# consumer_thread2 = MyThread('Consumer thread', store.consume)
# consumer_thread3 = MyThread('Consumer thread', store.consume)
# consumer_thread4 = MyThread('Consumer thread', store.consume)
#
# print(0)
# consumer_thread1.start()  # consumed item #1  [1 left]
# consumer_thread2.start()  # consumed item #2  [0 left]
# time.sleep(2)
#
# print(1)
# producer_thread1.start()  # produced item #3  [1 left]
# consumer_thread3.start()  # consumed item #3  [0 left]
# time.sleep(3)
#
# print(2)
# consumer_thread4.start()  # "thread A": no item #4 to consume
#                           # BLOCKS THE CURRENT THREAD ("thread A") - waiting for item #4
#
# producer_thread2.start()  # "thread B": new item #4 produced [1 left] - resumes "thread A"
#
#                           # "thread A": consumes item #4 [0 items left]

"""
CONDITION
"""


class Store:
    condition = threading.Condition()
    items = list(range(5))

    def consume(self):
        for i in range(9):
            time.sleep(1)
            self.condition.acquire()

            if len(self.items) == 0:
                print('Empty store, consumer waits')
                self.condition.wait()  # locks the condition, waits until producer thread releases it

            self.items.pop()
            print(f'Item consumed. {len(self.items)} left!')

            self.condition.notify()  # notify other thread that condition is met
            self.condition.release()

    def produce(self):
        for i in range(100):
            time.sleep(3)
            self.condition.acquire()

            if len(self.items) == 10:
                print('Full store, producer waits')
                self.condition.wait()  # locks the condition, waits until consumer thread releases it

            self.items.append(1)
            print(f'Item produced. {len(self.items)} left!')

            self.condition.notify()  # notify other thread that condition is met
            self.condition.release()


store = Store()

producer_thread = MyThread('Producer thread', store.produce)
consumer_thread = MyThread('Consumer thread', store.consume)

producer_thread.start()
consumer_thread.start()


"""
EVENT
event.wait() - wait until the event flag is .set() to True 
event.set() - sets event flag to True 
event.clear() - sets event flag to False
"""

"""
QUEUE
queue.put() - put's an object (eg. clousure) to the queue
queue.get() - get's removes and returns object from the queue
queue.task_done()
"""

