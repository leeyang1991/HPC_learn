from lytools import *
import submitit
from pprint import pprint
T = Tools()
import json
fdir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar'
progress_dir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar_progress'
T.mkdir(progress_dir)


def my_func_with_pbar(params):
    fpath, json_fpath = params
    with open(fpath) as fr:
        content = fr.readlines()[0]
        random_number = int(content.strip())
        # print(f'Processing {f}, random number: {random_number}')
        # exit(0)
        for step in range(random_number+1):
            progress_data = {
                "step": step,
                "total": random_number
            }
            progress_fpath = json_fpath
            with open(progress_fpath, 'w') as fw:
                json.dump(progress_data, fw)
            sleep(1)

def hpc_run():
    executor = submitit.AutoExecutor(folder="/gpfs/scratchfs1/ygo26002/ygo26002/log_dir")

    executor.update_parameters(
        slurm_job_name="pbar",
        cpus_per_task=1,
        mem_gb=0.5,
        timeout_min=1,
        slurm_array_parallelism=10,
        slurm_partition="general",
    )
    print('submiting...')
    params_list = []
    for f in T.listdir(fdir):
        fpath = join(fdir, f)
        json_fpath = join(progress_dir, f+'.json')
        params_list.append((fpath, json_fpath))
    jobs = executor.map_array(my_func_with_pbar, params_list)
    print(jobs[0].job_id)


def main():
    hpc_run()
    pass

if __name__ == "__main__":
    main()