from lytools import *
T = Tools()
from pprint import pprint

def main():
    data_dir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data'
    outdir = join('/gpfs/scratchfs1/ygo26002/ygo26002/results')
    params_dict_f = '/gpfs/scratchfs1/ygo26002/ygo26002/params.dict.pkl'
    T.mkdir(outdir)
    flag = 1
    params_dict = {}
    for f in tqdm(T.listdir(data_dir)):
        fpath = join(data_dir, f)
        outfile = join(outdir, f)
        params_dict[flag] = {'input': fpath, 'output': outfile}
        flag += 1
    T.save_dict_to_binary(params_dict, params_dict_f)

if __name__ == '__main__':

    main()