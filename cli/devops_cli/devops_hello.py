import click

@click.command()
@click.option('--name',prompt="Name",help="the name")
@click.option('--age',default=20,help="Age")
def hello(name, age):
    click.echo(f"Hello {name}, you are {age}")

if __name__ == '__main__':
    hello()