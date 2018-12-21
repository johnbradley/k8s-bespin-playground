import click
import json
from ddsc.sdk.client import Client as DukeDSClient


class DownloadList(object):
    def __init__(self, cmdfile):
        data = json.load(cmdfile)
        self.files = data['files']

    def items(self):
        items = []
        for file_data in self.files:
            key = file_data['key']
            dest = file_data['dest']
            items.append((key, dest))
        return items


@click.command()
@click.argument('cmdfile', type=click.File())
def download_files(cmdfile):
    dds_client = DukeDSClient()
    download_list = DownloadList(cmdfile)
    items = download_list.items()
    click.echo("Downloading {} files.".format(len(items)))
    for key, dest in items:
        click.echo("Downloading file {} to {}.".format(key, dest))
        dds_file = dds_client.get_file_by_id(file_id=key)
        dds_file.download_to_path(dest)


if __name__ == '__main__':
    download_files()
