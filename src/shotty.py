import os
from dotenv import load_dotenv
import boto3
import click

load_dotenv

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))

    return

if __name__ == '__main__':
    list_instances()
