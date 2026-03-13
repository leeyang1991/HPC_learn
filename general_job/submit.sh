#!/bin/bash
#SBATCH --job-name=array_job_test
#SBATCH --time=0:02:00
#SBATCH --array=1-1000%20
#SBATCH --cpus-per-task=1
#SBATCH --mem=300M
#SBATCH --output=./log_array_job_test/log_%A_%a.out


PYTHON=/home/ygo26002/miniforge3/envs/lytools/bin/python
SCRIPT=/home/ygo26002/Remote_SSH_Project/hpc_test/my_test/run.py

$PYTHON $SCRIPT $SLURM_ARRAY_TASK_ID
