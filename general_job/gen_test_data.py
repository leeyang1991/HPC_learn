from lytools import *
T = Tools()

data_dir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data'
T.mkdir(data_dir)

def gen_data():
    task_id_list = list(range(1,1001))
    for task_id in tqdm(task_id_list):
        task_str = str(task_id)
        task_hash = hashlib.sha256(task_str.encode()).hexdigest()
        f = join(data_dir, f'{task_hash[:10]}.txt')
        with open(f, 'w') as f:
            f.write(f'This is task {task_id:04d}, hash {task_hash}\n')
    pass

def main():
    gen_data()
    pass

if __name__ == "__main__":
    main()