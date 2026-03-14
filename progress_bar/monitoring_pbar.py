# from lytools import *
# T = Tools()
import json
import time
from pathlib import Path
from rich.progress import Progress
import os
from pprint import pprint
fdir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar'
pbar_dir = '/gpfs/scratchfs1/ygo26002/ygo26002/test_data_pbar_progress'


import json
import time
from pathlib import Path
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    TimeRemainingColumn,
    TimeElapsedColumn,
)

progress_dir = Path(pbar_dir)
print(f"Monitoring progress in directory: {progress_dir}")


refresh_interval = 1
# refresh_interval = 5

task_map = {}

with Progress(
    TextColumn("[bold yellow]{task.description}"),
    BarColumn(),
    TextColumn("{task.completed}/{task.total} {task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
    TimeRemainingColumn(),
) as progress:

    overall_task = None
    total_jobs = None

    while True:

        files = list(progress_dir.glob("*.json"))
        finished_jobs = 0

        for f in files:

            try:
                with open(f) as fp:
                    data = json.load(fp)
            except:
                continue

            jobid = data["jobid"]
            step = data["step"]
            total = data["total"]
            total_job = data["total_job"]
            sub_job_name = data["sub_job_name"]


            # 初始化 total progress
            if total_jobs is None:
                total_jobs = total_job
                overall_task = progress.add_task(
                    "[bold green]TOTAL", total=total_jobs
                )

            # 判断是否完成
            if step >= total:

                finished_jobs += 1

                if jobid in task_map:
                    progress.remove_task(task_map[jobid])
                    del task_map[jobid]

                continue

            # 创建 bar
            if jobid not in task_map:
                task_map[jobid] = progress.add_task(
                    f"({jobid}/{total_job}) {sub_job_name}", total=total
                )

            progress.update(task_map[jobid], completed=step)

        # 更新 total bar
        if overall_task is not None:
            progress.update(overall_task, completed=finished_jobs)

        # 所有任务完成
        if total_jobs and finished_jobs == total_jobs:
            break

        time.sleep(refresh_interval)