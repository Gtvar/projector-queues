import redis
import json

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6382, db=0)
#     encoder = json.JSONEncoder()
#     sample = {"hello": "bar"} # converts list to string
#     stream_name = 'mystream'
#
#     for i in range(10):
#         r.xadd(stream_name, sample)

    # "$" doesn't seem to work in python
    read_samples = r.xread({"stream":b"0-0"})

    print(read_samples)