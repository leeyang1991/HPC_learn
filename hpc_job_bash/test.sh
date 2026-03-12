#!/bin/bash
# This is a test script for HPC job submission. It will print the current date and time, the hostname, and the job ID.
echo "Current date and time: $(date)"
echo "Hostname: $(hostname)"
echo "Job ID: $SLURM_JOB_ID"

#!/bin/bash
#SBATCH --job-name=yang_analysis
#SBATCH --time=0:02:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --output=log.out
#SBATCH --error=log.err

PYTHON=/home/ygo26002/miniforge3/envs/lytools/bin/python

echo "Start job"
hostname
date

$PYTHON /home/ygo26002/Remote_SSH_Project/hpc_test/test.py

echo "Finished"
date

