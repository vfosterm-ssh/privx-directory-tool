import click
import privx_api
import config
from rich import print
from rich.table import Table
from rich.align import Align
from rich.traceback import install

install(show_locals=False)


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

api = privx_api.PrivXAPI(
    config.HOSTNAME,
    config.HOSTPORT,
    config.CA_CERT,
    config.OAUTH_CLIENT_ID,
    config.OAUTH_CLIENT_SECRET,
)

api.authenticate(config.API_CLIENT_ID, config.API_CLIENT_SECRET)


@click.group(context_settings=CONTEXT_SETTINGS, chain=True)
def cli():
    """
    PrivX Directory Tool

    For command specific help use: privxdt [command] --help
    """


@cli.command(context_settings=CONTEXT_SETTINGS)
def list_directories():
    resp = api.get_sources()
    if resp.ok:
        data = resp.data.get("items")
    else:
        raise Exception(resp.data)

    table = Table(title="Directories")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Type")
    for dir in data:
        table.add_row(dir["id"], dir["name"], dir["connection"]["type"])
    print(Align.center(table))


@cli.command(context_settings=CONTEXT_SETTINGS)
@click.option("-H", "--host-id", help="ID of host to migrate", required=True)
@click.option(
    "-D", "--directory-id", help="ID of directory to migrate to", required=True
)
def migrate(host_id, directory_id):
    resp = api.get_host(host_id)
    if resp.ok:
        host = resp.data
    else:
        raise Exception(resp.data)
    host["source_id"] = directory_id
    resp = api.update_host(host_id, host)
    if resp.ok:
        print(resp.data)
    else:
        raise Exception(resp.data)
