from lytools import *
import submitit
from pprint import pprint

T = Tools()

starttime = time.time()

def my_function(param):
    x,y = param

    result = x+y
    print('input:',x,y)
    print('result:',result)
    sleep(1)
    return result


executor = submitit.AutoExecutor(folder="/gpfs/scratchfs1/ygo26002/ygo26002/log_dir")

executor.update_parameters(
    slurm_job_name="plus",
    cpus_per_task=1,
    mem_gb=0.5,
    timeout_min=1,
    slurm_array_parallelism=100,
    slurm_partition="general",
)
print('submiting...')
params_list = []
for i in range(1000):
    x = i
    y = i*2
    params_list.append((x,y))
# pprint(params_list)
# exit()
jobs = executor.map_array(my_function, params_list)
print(jobs[0].job_id)