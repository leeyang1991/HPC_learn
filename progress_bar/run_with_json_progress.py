import submitit
import time
import os
import json
import shutil

fdir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar'

def mkdir(dir, force=False):
    if not os.path.isdir(dir):
        if force == True:
            os.makedirs(dir)
        else:
            os.mkdir(dir)


def join(*args):
    args_new = []
    for path in args:
        path_new = path.replace('\\','/')
        args_new.append(path_new)
    return os.path.join(*args_new)


def listdir(fdir):
    '''
    Mac OS
    list the names of the files in the directory
    return sorted files list without '.DS_store'
    '''
    list_dir = []
    for f in sorted(os.listdir(fdir)):
        if f.startswith('.'):
            continue
        list_dir.append(f)
    return list_dir

def sleep(seconds):
    time.sleep(seconds)

def my_func_with_pbar(params):
    fpath, json_fpath,sub_job_name,current_job_id,total_job_num = params
    print(fpath)
    with open(fpath) as fr:
        content = fr.readlines()[0]
        random_number = int(content.strip())
        for step in range(random_number+1):
            progress_data = {
                "step": step,
                "total": random_number,
                'total_job': total_job_num,
                'jobid': current_job_id,
                'sub_job_name': sub_job_name,
            }
            progress_fpath = json_fpath
            with open(progress_fpath, 'w') as fw:
                json.dump(progress_data, fw)
            sleep(1)

def hpc_run():
    log_folder = "/gpfs/scratchfs1/ygo26002/ygo26002/log_dir"
    progress_dir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar_progress'

    if os.path.exists(log_folder):
        shutil.rmtree(log_folder)
    if os.path.exists(progress_dir):
        shutil.rmtree(progress_dir)
    mkdir(progress_dir, force=True)

    executor = submitit.AutoExecutor(folder=log_folder)

    executor.update_parameters(
        slurm_job_name="pbar",
        cpus_per_task=1,
        mem_gb=0.5,
        timeout_min=3,
        slurm_array_parallelism=30,
        slurm_partition="general",
    )
    print('submiting...')
    total_job_num = len(listdir(fdir))

    params_list = []
    flag = 1
    for f in listdir(fdir):
        fpath = join(fdir, f)
        json_fpath = join(progress_dir, f + '.json')
        current_job_id = flag
        flag += 1
        sub_job_name = f
        params_list.append((fpath, json_fpath, sub_job_name, current_job_id, total_job_num))
    jobs = executor.map_array(my_func_with_pbar, params_list)
    print(jobs[0].job_id)


def main():
    hpc_run()
    pass

if __name__ == "__main__":
    main()