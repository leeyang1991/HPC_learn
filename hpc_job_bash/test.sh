#!/bin/bash
# This is a test script for HPC job submission. It will print the current date and time, the hostname, and the job ID.
echo "Current date and time: $(date)"
echo "Hostname: $(hostname)"
echo "Job ID: $SLURM_JOB_ID"

# SBATCH --job-name=Yang_test
# SBATCH --output=Yang_test.out
# SBATCH --error=Yang_test.err
# SBATCH --time=00:10:00
# SBATCH --ntasks=1