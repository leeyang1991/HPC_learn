import redis
from pathlib import Path

class HPC_redis:

    def __init__(self):
        self.r = self.conn_redis()
        pass

    def conn_redis(self):
        redis_conf = Path.home() / '.config' / 'redis' / 'redis.conf'
        with open(redis_conf) as f:
            redis_conf = f.readlines()
            host = redis_conf[0].strip()
            port = int(redis_conf[1].strip())
            passwd = redis_conf[2].strip()

        r = redis.Redis(
            host=host,
            port=port,
            password=passwd,
        )
        return r

    def hit_redis(self,job_name,task_name,amount=1):
        self.r.hincrby(name=job_name,key=task_name,amount=amount)

    def set_total_num(self,job_name,task_name,total_job=10000):
        # r.delete(job_name+'_total')
        # r.hincrby(name=job_name, key=task_name+'_total', amount=total_job)
        self.r.hset(job_name, task_name+'_total', total_job)


    def query_redis(self,r,job_name):
        print(r.hgetall(job_name))
        pass

def main():

    # r = conn_redis()
    job_name = 'Test_job'
    task_name = 'task:3'


    # r.flushdb()  # delete all data
    # r.delete('job_name')  # refresh job name
    total_job = 9999
    HPC_redis().set_total_num('test_job',total_job)
    # set_total_num(r, job_name, task_name, total_job)
    # for i in range(total_job):
    #     hit_redis(r,job_name,task_name,1)

    # while 1:
    #     query_redis(r,job_name,task_name)
    #     sleep(1)

if __name__ == '__main__':
    main()