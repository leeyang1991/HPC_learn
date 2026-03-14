from lytools import *
T = Tools()
import json
import time
from pathlib import Path
from rich.progress import Progress
from pprint import pprint
fdir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar'
pbar_dir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar_progress'
flist = T.listdir(fdir)
# pprint(flist)
# exit(0)
progress_dir = Path(pbar_dir)

with Progress() as progress:
    task_map = {}
    # 每个 tile 一个 progress bar
    # for f in flist:
    #     fpath = progress_dir / f"{f}.json"
    #     task_map[f] = progress.add_task(f"{f}", total=len(flist))

    while True:

        finished = 0

        for f in flist:

            fpath = progress_dir / f"{f}.json"

            if fpath.exists():

                with open(fpath) as fp:
                    data = json.load(fp)
                task_map[f] = progress.add_task(f"{f}", total=data["total"])
                step = data["step"]

                progress.update(task_map[f], completed=step)

                if step >= data["total"]:
                    finished += 1

        if finished == len(flist):
            break

        time.sleep(1)
