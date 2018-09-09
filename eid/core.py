import click
import os
import shutil
from .lib.command import init as init_command

@click.group('eid command')
def main():
    pass

@main.command(help='initialize machine learning project')
@click.argument('dir')
def init(dir):
    init_command(dir)
