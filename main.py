import time
from utils.runner import run

# get the start time
exec_start_time = time.time()
cpu_start_time = time.process_time()

run()

# get the end time
exec_elapsed_time = time.time() - exec_start_time
cpu_elapsed_time = time.process_time() - cpu_start_time

print("\n==========TIME RESOURCE SPENT==========")
print("\nClock execution time: %s minutes" % (exec_elapsed_time/60))
print('Clock execution time:', time.strftime("%H:%M:%S", time.gmtime(exec_elapsed_time)))
print("\nCPU/GPU execution time: %s minutes" % (cpu_elapsed_time/60))
print('CPU/GPU execution time:', time.strftime("%H:%M:%S", time.gmtime(cpu_elapsed_time)),'\n')