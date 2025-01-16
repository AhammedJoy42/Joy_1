
# multiprocessing = running tasks in parallel on different CPU cores, bypass GIL used for thread
#          multiprocessing = better for cup bound tasks (heavy CPU usage)
#                multiprocessing = better for io bound tasks(waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0;
    while count < num:
        count += 1;

def main():

    a = Process(target=counter, args=(1000000,));
    a.start();
    a.join();

    print("Finished in: ", time.pref_counter(), "seconds");

if  __name__ == '__main__':
    main();