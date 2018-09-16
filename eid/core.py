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
@click.option('--gpu/--cpu', default=False)
def run(filename, gpu):
    command.run(filename, gpu)

@main.command(help='ipython shell in docker container')
@click.option('--gpu/--cpu', default=False)
def shell(gpu):
    command.shell(gpu)

@main.command(help='build docker container')
@click.option('--gpu/--cpu', default=False)
def build(gpu):
    command.build(gpu)

@main.command(help='run notebook in docker container')
@click.option('--gpu/--cpu', default=False)
def notebook(gpu):
    command.notebook(gpu)
