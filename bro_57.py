
# thread = a flow of execution . Like a separate order of instructions.
#          However, each thread takes a turn running to achieve concurrency
#          GIL = global interpreter lock
#         Allows only one thread to hold the control of the python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#              use multiprocessing

# io bound = program/ task spends most of it's time waiting for external events (user input, web scraping)
#              use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3);
    print("You eat breakfast.");

def drink_coffee():
    time.sleep(4)
    print("You drink coffee.");

def study():
    time.sleep(5);
    print("You finished study.");

x = threading.Thread(target = eat_breakfast(), args = ());
x.start();

y = threading.Thread(target = drink_coffee(), args = ());
y.start();

z = threading.Thread(target = study(), args = ());
z.start();

# x.join();
# y.join();
# z.join();

eat_breakfast();
drink_coffee();
study();

print(threading.active_count());
print(threading.enumerate());


