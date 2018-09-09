import click
import os
import shutil
from .lib import command as command

@click.group('eid command')
def main():
    pass

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
