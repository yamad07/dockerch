import click
import os
import shutil
from .src import command as command
from .src import utils

@click.group('eid command')
@click.option('--use_gpu', default=False, type=bool)
def main(use_gpu):
    if use_gpu:
        utils.write_gpu_config()

@main.command(help='initialize machine learning project')
@click.argument('dir')
def init(dir):
    command.init(dir)


@main.command(help='run script in docker container')
@click.argument('filename')
def run(filename):
    command.run(filename)

@main.command(help='ipython shell in docker container')
def shell():
    command.shell()

@main.command(help='build docker container')
def build():
    command.build()

@main.command(help='run notebook in docker container')
def notebook():
    command.notebook()
