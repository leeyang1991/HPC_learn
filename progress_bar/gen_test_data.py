from lytools import *
T = Tools()

fdir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar'
n_tasks = 100
T.mkdir(fdir)

for i in tqdm(range(n_tasks)):
    task_str = str(i)
    task_hash = hashlib.sha256(task_str.encode()).hexdigest()
    f = join(fdir, f'{task_hash[:10]}.txt')
    random_number = random.randint(7, 15)
    with open(f, 'w') as f:
        f.write(f'{random_number}\n')
