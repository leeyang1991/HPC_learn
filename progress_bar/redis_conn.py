import redis
# print(redis)

r = redis.Redis(
    host='10.10.0.1',
    port=6380,
    password="yourpassword",
)

# r.

r.hincrby(name="global_progress",key="job1",amount=1)
r.hincrby(name="global_progress",key="job2",amount=2)
r.hincrby(name="global_progress",key="job3",amount=3)
r.hincrby(name="global_progress",key="job4",amount=5)
r.hincrby(name="global_progress",key="job5",amount=2)

print(r.hgetall("global_progress"))
# r.delete("global_progress")