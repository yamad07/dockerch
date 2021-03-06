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

        if 'runtime' in data['services']['experiment']:
            with open('./docker-compose.yml', 'w') as f:
                data['services']['experiment'].pop('runtime')
                f.write(yaml.dump(data))

def base_command(use_gpu):
    if use_gpu:
        return ['docker-compose', '-f', 'docker-compose-gpu.yml']
    return ['docker-compose']

def run_command(use_gpu):
    args = base_command(use_gpu)
    args.append('run')

    return args
