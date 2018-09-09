import logging
import os

logger = logging.getLogger(__name__)

def get_src_path(dir=''):
    return os.path.join(os.path.dirname(__file__), dir)
