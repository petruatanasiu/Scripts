#! /usr/bin/env python3
import click
import datetime
import psutil
import subprocess

@click.group()
def cli():
    """System Health Check CLI"""

@cli.command("datetime", short_help="Show current date and time")
def show_datetime():
    now = datetime.datetime.now()
    click.echo(f"Current Date and Time: {now}")

@cli.command("uptime", short_help="Show system uptime")
def show_uptime():
    try:
        # For Unix-like systems
        uptime = subprocess.check_output(["uptime", "-p"], text=True).strip()
    except:
        # For Windows
        uptime = psutil.boot_time()
        uptime = datetime.datetime.fromtimestamp(uptime).strftime("%Y-%m-%d %H:%M:%S")

    click.echo(f"System Uptime: {uptime}")
@cli.command("disk", short_help="Show disk usage")
def show_disk():
    disk_info = psutil.disk_usage("/")
    click.echo(f"Total Disk Space: {disk_info.total} bytes")
    click.echo(f"Free Disk Space: {disk_info.free} bytes")
    click.echo(f"Used Disk Space: {disk_info.used} bytes")
    click.echo(f"Disk Space Percentage: {disk_info.percent}%")
    print(type(disk_info))
    print(dir(disk_info))

@cli.command("memory", short_help="Show memory usage")
def show_memory():
    memory_info = psutil.virtual_memory()
    click.echo(f"Total Memory: {memory_info.total} bytes")
    click.echo(f"Available Memory: {memory_info.available} bytes")
    click.echo(f"Used Memory: {memory_info.used} bytes")
    click.echo(f"Memory Usage Percentage: {memory_info.percent}%")


@cli.command("cpu", short_help="Show cpu usage")
def show_cpu():
    cpu = psutil.cpu_times()
    print(cpu)

if __name__ == '__main__':
    cli()