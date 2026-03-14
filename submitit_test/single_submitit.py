from lytools import *
import submitit

T = Tools()


starttime = time.time()

def my_function(x):
    return x * x

executor = submitit.AutoExecutor(folder="log")

executor.update_parameters(
    timeout_min=1,
    cpus_per_task=1,
    mem_gb=0.3,
    slurm_partition="general",
)

job = executor.submit(my_function, 32)
# print("job id:", job.job_id)
print(job.result())
endtime = time.time()
duration = endtime - starttime
print(f"Execution time: {duration:.2f} seconds")