#! /usr/bin/env python3
import click
import psutil
import subprocess

@click.group()
def cli():
    """Sample cli"""
#sau pass ^^^

@cli.command("disk_sdk", short_help="show disk information")
def disk_sdk():
    click.echo(psutil.disk_usage("/"))


@cli.command("disk_cmd", short_help="show disk information")
def disk_cmd():
    click.echo(subprocess.run(["df", "-h"]))

if __name__ == '__main__':
    cli()