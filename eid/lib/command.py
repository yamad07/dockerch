from .utils import logger, get_src_path
import shutil
import os

def init(dir):
    src_path = get_src_path()
    os.mkdir(dir)
    logger.info('copy Dockerfile')
    shutil.copyfile(os.path.join(src_path, 'docker/Dockerfile'), '{}/Dockerfile'.format(dir))
    logger.info('copy docker-compose.yml')
    shutil.copyfile(os.path.join(src_path, 'docker/docker-compose.yml'), '{}/docker-compose.yml'.format(dir))
