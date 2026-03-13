
from lytools import *
T = Tools()

fdir = '/gpfs/scratchfs1/ygo26002/ygo26002/results'
task_id_list = []
# task_0371.txt
flag = 0
for f in T.listdir(fdir):
    task_id = f.split('_')[1].split('.')[0]
    task_id = int(task_id)
    task_id_list.append(task_id)
    fpath = join(fdir, f)
    with open(fpath) as fr:
        content = fr.readlines()
        flag += 1
        print(flag)
        print(content)


for task_id in range(1,1001):
    if not task_id in task_id_list:
        print(f'task_{task_id:04d} is missing')

