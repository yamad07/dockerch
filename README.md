# dockerch
**dockerch** is container wrapper which you can run scripts easily using PyTorch.
this is wrapper of docker-compose command.

## Usage
```
# in your ml repository
$ git clone https://github.com/yamad07/dockerch
$ dockerch/setup.sh

# build docker image
$ bin/dockerch build

# run script in docker image
$ bin/dockerch run example.py

# if you want to start console
$ bin/dockerch console

# if you want to add library
$ bin/dockerch install gym # default using pip. if you want to use conda, use `--using conda` option.
```
