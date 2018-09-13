import click
import os
import shutil
from .src import command as command
from .src import utils

@click.group('eid command')
@click.option('--use-gpu/--no-use-gpu', default=False)
def main(use_gpu):
    pass

@main.command(help='initialize machine learning project')
@click.argument('dir')
def init(dir):
    command.init(dir)


@main.command(help='run script in docker container')
@click.argument('filename')
@click.option('--use-gpu/--no-use-gpu', default=False)
def run(filename, use_gpu):
    if use_gpu:
        utils.write_gpu_config()
    else:
        utils.remove_gpu_config()
    command.run(filename)

@main.command(help='ipython shell in docker container')
@click.option('--use-gpu/--no-use-gpu', default=False)
def shell(use_gpu):
    if use_gpu:
        utils.write_gpu_config()
    else:
        utils.remove_gpu_config()
    command.shell()

@main.command(help='build docker container')
def build():
    command.build()

@main.command(help='run notebook in docker container')
@click.option('--use-gpu/--no-use-gpu', default=False)
def notebook(use_gpu):
    if use_gpu:
        utils.write_gpu_config()
    else:
        utils.remove_gpu_config()
    command.notebook()
