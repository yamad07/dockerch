import logging
import os
import yaml

logger = logging.getLogger(__name__)

def get_src_path(dir=''):
    return os.path.join(os.path.dirname(__file__), dir)

def write_gpu_config():
    with open('./docker-compose.yml', 'r') as f:
        data = yaml.load(f)

    with open('./docker-compose.yml', 'w') as f:
        data['services']['experiment']['runtime'] = 'nvidia'
        f.write(yaml.dump(data))

def remove_gpu_config():
    with open('./docker-compose.yml', 'r') as f:
        data = yaml.load(f)

    with open('./docker-compose.yml', 'w') as f:
        data['services']['experiment'].pop('runtime')
        f.write(yaml.dump(data))
