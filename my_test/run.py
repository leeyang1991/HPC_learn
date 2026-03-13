from lytools import *
T = Tools()

task_id = int(sys.argv[1])
params_dict_f = '/gpfs/scratchfs1/ygo26002/ygo26002/params.dict.pkl'

params_dict = T.load_dict_from_binary(params_dict_f)
fpath = params_dict[task_id]['input']
outf = params_dict[task_id]['output']
with open(fpath) as fr:
    content = fr.readlines()[0]
    with open(outf, 'w') as fw:
        fw.write(content+'\n')
        fw.write(f'task_{task_id:04d} is done\n')
print("Running task:", task_id)
sleep(2)
print('Done')
now = datetime.datetime.now()
print(now)