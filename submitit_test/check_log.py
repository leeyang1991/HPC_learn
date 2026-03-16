from lytools import *
T = Tools()

def read_err_files(log_folder):
    log_folder = Path(log_folder)
    for f in T.listdir(log_folder):
        if not f.endswith(".err"):
            continue
        fpath = log_folder / f
        # print(fpath)
        with open(fpath) as fr:
            err_content = fr.read()
            if len(err_content) == 0:
                print('==============')
                print(f"Error in file: {fpath}")
                print(err_content)

def read_out_files(log_folder):
    log_folder = Path(log_folder)
    count = 0
    for f in T.listdir(log_folder):
        if not f.endswith(".out"):
            continue
        fpath = log_folder / f
        # print(fpath)
        with open(fpath) as fr:
            log_content = fr.read()
            print(log_content)
            print('------------')
            count += 1
    print(f'Total files: {count}')
    pass


def read_result_files(log_folder):
    log_folder = Path(log_folder)
    count = 0
    for f in T.listdir(log_folder):
        if not f.endswith("_result.pkl"):
            continue
        fpath = log_folder / f
        # print(fpath)
        content = pickle.load(open(fpath, 'rb'))
        print(content)
        print('------------')
        count += 1
    print(f'Total files: {count}')
    pass

def read_submit_files(log_folder):
    log_folder = Path(log_folder)
    count = 0
    for f in T.listdir(log_folder):
        if not f.endswith("_submitted.pkl"):
            continue
        fpath = log_folder / f
        # print(fpath)
        content = pickle.load(open(fpath, 'rb'))
        print(content)
        print('------------')
        count += 1
    print(f'Total files: {count}')
    pass

if __name__ == '__main__':
    # fpath = "/gpfs/scratchfs1/ygo26002/ygo26002/log_dir/23182196_39_0_result.pkl"
    # content = pickle.load(open(fpath, "rb"))
    # array = content[1][-1]
    # plt.imshow(array)
    # plt.show()
    # print(type(array))
    # print(content)
    # log_folder = "/gpfs/scratchfs1/ygo26002/ygo26002/log_dir"
    # log_folder = "/home/yangli/UCONN_Projects/HPC_learn/log_dir"
    log_folder = "/Users/liyang/Documents/pycharm_project_temp/HPC_learn/log_dir"
    # read_err_files(log_folder)
    # read_out_files(log_folder)
    read_result_files(log_folder)
    # read_submit_files(log_folder)