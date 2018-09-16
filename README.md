# eid
**eid** is container wrapper which you can run ml scripts easily.
this is wrapper of docker-compose command.

## Usage
```
# init your ml project
$ eid init [PROJECT NAME]

# build docker image
$ cd [PROJECT NAME]
$ eid build

# run script in docker image
$ eid run example.py

# run on gpu
$ eid run --gpu example.py

# if you want to start ipython shell
$ eid shell

# if you want to start jupyter notebook
$ eid notebook
```
