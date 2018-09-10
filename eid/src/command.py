from .utils import logger, get_src_path
import shutil
import os
import subprocess

def init(dir):
    src_path = get_src_path()
    os.mkdir(dir)
    shutil.copyfile(os.path.join(src_path, 'templates/Dockerfile'), '{}/Dockerfile'.format(dir))
    shutil.copyfile(os.path.join(src_path, 'templates/docker-compose.yml'), '{}/docker-compose.yml'.format(dir))
    shutil.copyfile(os.path.join(src_path, 'templates/requirements.txt'), '{}/requirements.txt'.format(dir))

def run(filename):
    args = ['docker-compose', 'run', 'experiment', 'python', filename]
    try:
        res = subprocess.check_call(args)
        logger.info(res)
    except Exception as E:
        print(E)

def shell():
    args = ['docker-compose', 'run', 'experiment', 'ipython']
    try:
        res = subprocess.check_call(args)
        logger.info(res)
    except Exception as E:
        print(E)

def build():
    args = ['docker-compose', 'build']
    try:
        res = subprocess.check_call(args)
        logger.info(res)
    except Exception as E:
        print(E)

def notebook():
    args = ['docker-compose', 'run', '--service-ports', 'experiment', 'jupyter', 'notebook', '--ip=0.0.0.0', '--port', '8888']
    try:
        res = subprocess.check_call(args)
        logger.info(res)
    except Exception as E:
        print(E)
