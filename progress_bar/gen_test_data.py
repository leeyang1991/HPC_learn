from lytools import *
T = Tools()

# fdir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar' # hpc
fdir = '/home/yangli/UCONN_Projects/HPC_learn/test_data_pbar' # dell
# fdir = '/Users/liyang/Documents/pycharm_project_temp/HPC_learn/test_data_pbar' # mac m4pro
n_tasks = 100
T.mkdir(fdir)

for i in tqdm(range(n_tasks)):
    # task_str = str(i)
    # task_hash = hashlib.sha256(task_str.encode()).hexdigest()
    f = join(fdir, f'{i:04d}.txt')
    random_number = random.randint(1, 30)
    with open(f, 'w') as f:
        f.write(f'{random_number}\n')
