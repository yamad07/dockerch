from .utils import logger, get_src_path, base_command, run_command
import shutil
import os
import subprocess

def init(dir):
    src_path = get_src_path()
    os.mkdir(dir)
    shutil.copyfile(os.path.join(src_path, 'templates/Dockerfile'), '{}/Dockerfile'.format(dir))
    shutil.copyfile(os.path.join(src_path, 'templates/docker-compose.yml'), '{}/docker-compose.yml'.format(dir))
    shutil.copyfile(os.path.join(src_path, 'templates/docker-compose-gpu.yml'), '{}/docker-compose-gpu.yml'.format(dir))
    shutil.copyfile(os.path.join(src_path, 'templates/requirements.txt'), '{}/requirements.txt'.format(dir))

def run(filename, use_gpu):
    args = run_command(use_gpu)
    args.extend(['experiment', 'python', filename])
    try:
        res = subprocess.check_call(args)
        logger.info(res)
    except Exception as E:
        print(E)

def shell(use_gpu):
    args = run_command(use_gpu)
    args.extend(['experiment', 'ipython'])
    try:
        res = subprocess.check_call(args)
        logger.info(res)
    except Exception as E:
        print(E)

def build(use_gpu):
    args = base_command(use_gpu)
    args.append('build')
    try:
        res = subprocess.check_call(args)
        logger.info(res)
    except Exception as E:
        print(E)

def notebook(use_gpu):
    args = run_command(use_gpu)
    args.extend(['--service--ports', 'experiment', 'jupyter', 'notebook', '--ip=0.0.0.0', '--port', '8888'])
    try:
        res = subprocess.check_call(args)
        logger.info(res)
    except Exception as E:
        print(E)
