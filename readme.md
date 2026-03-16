# Uconn HPC Cheat Sheet


## Module Management
- `module avail` # List all available modules.
- `module load <module_name>` # Load a specific module.

## Job Management
### Check Cluster Status
See `man sinfo` for more details.
- `sinfo` # View the status of the cluster and available resources.
- `sinfo -N -l` # View detailed information about nodes in the cluster.
- `sinfo -p general` # View information about the 'general' partition.
- `sinfo -p gpu` # View information about the 'gpu' partition.
### Job Submission
- `sinfo -t down,drained,draining` # Check for any nodes that are down or unavailable.
- `sbatch <script.sh>` # Submit a job using a script.
- `sranks | grep username` # View your currently running jobs and their node assignments.

### Job Monitoring
- `squeue --me` # View your current jobs in the queue.
- `squeue -a` # View all jobs in the queue.
- `sjobs` # View all jobs
- `sjobs -j {JOBID}`   # View a specific job
- `scontrol show job {JOBID}` # View detailed information about a specific job.
- `tmux` # Start a tmux session to monitor jobs in real-time.
- `seff {JOBID}` # View the resource usage of a completed job.
- `shist|grep FAIL` # View all failed jobs.
### Job Cancellation
- `scancel <job_id>` # Cancel a specific job.
- ``` scancel -u `whoami` ``` # Cancel all your jobs.
### Job History
- `shist`                   # View all jobs
- `shist -j {JOBID} `       # View a specific job
- `shist -S now-10days`     # View all jobs submitted in the past 10 days
### Interactive jobs
- `srun --pty bash` # Start an interactive session.

## Job Script Template

```
#!/bin/bash
#SBATCH -J jobname # input your job name
#SBATCH --partition=general # partition (sinfo to check all)
#SBATCH --nodes 1 # number of nodes per task
#SBATCH --ntasks 1 # number of CPUs per task
#SBATCH --array 1-10 # task array, i.e., 1, 2, 3, 4, 5, …
#SBATCH --constraint='epyc128' # Target the AMD Epyc node architecture
#SBATCH --mem-per-cpu=10G # specify the memory you need
#SBATCH -o log/%x-out-%A_%4a.out # output file
#SBATCH -e log/%x-err-%A_%4a.err # error report
#SBATCH --cpus-per-task=1
#SBATCH --time=0:02:00 # specify the time you need, e.g., 2 minutes

python script.py $SLURM_ARRAY_TASK_ID

```



