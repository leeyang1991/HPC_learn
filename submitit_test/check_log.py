from lytools import *
T = Tools()

def read_log_files(log_folder):
    log_folder = Path(log_folder)
    for f in T.listdir(log_folder):
        if not f.endswith(".err"):
            continue
        fpath = log_folder / f
        # print(fpath)
        with open(fpath) as fr:
            err_content = fr.read()
            if len(err_content) > 0:
                print('==============')
                print('==============')
                print(f"Error in file: {fpath}")
                print(err_content)
                # exit(0)
                print('----------')
                fpath_log = log_folder / f.replace(".err", ".out")
                with open(fpath_log) as fr_log:
                    log_content = fr_log.read()
                    print(f"Error in file: {fpath_log}")
                    print(log_content)
                    exit(1)

if __name__ == '__main__':
    log_folder = "/gpfs/scratchfs1/ygo26002/ygo26002/log_dir"
    read_log_files(log_folder)