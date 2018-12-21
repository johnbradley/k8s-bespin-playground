import click
import json
from ddsc.sdk.client import Client as DukeDSClient
from ddsc.core.upload import ProjectUpload
from ddsc.core.remotestore import ProjectNameOrId


class UploadList(object):
    def __init__(self, cmdfile):
        data = json.load(cmdfile)
        self.destination = data['destination']
        self.paths = data['paths']


@click.command()
@click.argument('cmdfile', type=click.File())
def upload_files(cmdfile):
    upload_list = UploadList(cmdfile)
    click.echo("Uploading {} paths to {}.".format(len(upload_list.paths), upload_list.destination))
    dds_client = DukeDSClient()
    project_upload = ProjectUpload(dds_client.dds_connection.config,
                                   ProjectNameOrId.create_from_name(upload_list.destination),
                                   upload_list.paths)
    click.echo(project_upload.get_differences_summary())
    if project_upload.needs_to_upload():
        click.echo("Uploading")
        project_upload.run()
    else:
        click.echo("Nothing needs to be done.")


if __name__ == '__main__':
    upload_files()
