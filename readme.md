# Uconn HPC Cheat Sheet


## Module Management
- `module avail` # List all available modules.
- `module load <module_name>` # Load a specific module.

## Job Management
### Job Submission
- `sbatch <script.sh>` # Submit a job using a script.
### Job Monitoring
- `squeue --me` # View your current jobs in the queue.
- `sjobs` # View all jobs
- `sjobs -j {JOBID}`   # View a specific job
- `squeue -a` # View all jobs in the queue.
- `scontrol show job {JOBID}` # View detailed information about a specific job.
### Job Cancellation
- `scancel <job_id>` # Cancel a specific job.
- ``` scancel -u `whoami` ``` # Cancel all your jobs.
### Job History
- `shist`                   # View all jobs
- `shist -j {JOBID} `       # View a specific job
- `shist -S now-10days`     # View all jobs submitted in the past 10 days
### Interactive jobs
- `srun --pty bash` # Start an interactive session.
### Job arrays
- `sbatch --array=1-10 <script.sh>` # Submit a job array with 10 tasks.

## Job Script Template
```
#!/bin/bash
#SBATCH --job-name=my_job           # Job name
#SBATCH --output=output_%j.txt          # Output file name with job ID
#SBATCH --  error=error_%j.txt            # Error file name with job ID
```

