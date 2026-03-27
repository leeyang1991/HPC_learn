# Uconn HPC Cheat Sheet
## Hint
- `motd` # Hint messages.

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

```bash
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
#SBATCH --exclude=cn[507] # exclude specific nodes

python script.py $SLURM_ARRAY_TASK_ID

```
## Submitit
A python package for submitting jobs to a cluster

`pip install submitit` # Install submitit

### Example usage for array jobs:
```python
import submitit
import time

def my_function(param):
    x,y = param

    result = x+y
    print('input:',x,y)
    print('result:',result)
    time.sleep(1)
    return result

params_list = [(1,2),(3,4),(5,6),(7,8),(9,10)]

executor = submitit.AutoExecutor(folder="log_dir")

executor.update_parameters(
    slurm_job_name="job_name",
    cpus_per_task=1,
    mem_gb=0.5,
    timeout_min=1,
    slurm_array_parallelism=100,
    slurm_partition="general",
    srun_args={"exclude": "cn[473-479,501]"},
)
jobs = executor.map_array(my_function, params_list)
```

### Example usage for single job:
```python
import submitit
def my_function(x):
    return x * x

executor = submitit.AutoExecutor(folder="log")
executor.update_parameters(
    timeout_min=1,
    cpus_per_task=1,
    mem_gb=0.3,
    slurm_partition="general",
)
job = executor.submit(my_function, 10)
print("job id:", job.job_id)
print(job.result())
```
## Monitoring you jobs with a progress bar. 

This requires a Redis server to store the progress information. The following steps will guide you through setting up the Redis server and using submitit with a progress bar.
### Python packages required:
```bash
pip install submitit redis pathos rich 
```
### Step 1: Deploy a Redis service
**DO NOT** deploy it on a HPC nodes. You can use your local machine or a server with a public IP address.
#### Deploy redis via Docker
Compose file for Redis server:
```yaml
services:
  redis-progress:
    image: redis:7
    container_name: redis-progress
    restart: unless-stopped

    ports:
      - "6379:6379"

    volumes:
      - ./redis_data:/data

    command: >
      redis-server
      --appendonly yes
      --requirepass yourpassword
      --maxmemory 2gb
      --maxmemory-policy allkeys-lru
      
    deploy:
      resources:
        limits:
          memory: 3g

```
```docker compose up -d``` # Start the Redis server

#### Test Redis connection
```python
import redis
r = redis.Redis(host='your_redis_host', port=6379, password='yourpassword')
r.set('test_key', 'test_value')
print(r.get('test_key').decode())
```

#### Create redis connection configuration file
Location: ```~/.config/redis/redis.conf```
```txt
your_redis_host
6379
yourpassword
```

### Step 2: Submit your jobs
```python
from HPC_func import *

def my_function(x):
    return x * x

job_name = 'Your_job_name'
params_list = [1,2,3,4,5,6,7,8,9,10]
log_folder = 'Your_log_folder'
init_job(job_name, params_list)
sumbit_jobs_array(my_function, params_list, log_folder,
                  job_name=job_name,
                  job_number_limit=1,
                  parallel_process_per_task=2,
                  slurm_array_parallelism=1,
                  parallel_process_p_or_t='p',
                  cpus_per_task=10,
                  mem_gb=2,
                  timeout_min=10,
                  slurm_partition="general",
                  exclude_nodes=None,
                  pbar_update_freq=1,
                  )
```

### Step 3: Monitor the progress bar
```python
from HPC_func import *
job_name = 'Your_job_name'
progress_bar_monitoring(job_name)
```

### Step 4: Check the log files
```python
from HPC_func import *
log_folder = 'Your_log_folder'
Check_logs(log_folder).read_err_files() # Read error files
Check_logs(log_folder).read_out_files() # Read output files
```