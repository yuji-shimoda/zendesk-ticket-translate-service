import os
import json
import boto3
from zenpy import Zenpy
from zenpy.lib.api_objects import Comment
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
TOKYO = 'ap-northeast-1'
# Get credentials
secret_name = os.environ['ZENDESK_SECRET']
secretsmanager = boto3.client('secretsmanager', region_name=TOKYO)
resp = secretsmanager.get_secret_value(SecretId=secret_name)
secret = json.loads(resp['SecretString'])
credentials = {
    "token": secret['token'],
    "email": secret['email'],
    "subdomain": secret['subdomain']
}
# Create a Zenpy instance
zenpy_client = None


def update_ticket(ticket_id, message):
    global zenpy_client
    comment = "```\n{}\n```".format(message)
    try:
        zenpy_client = Zenpy(**credentials)
        ticket = zenpy_client.tickets(id=ticket_id)
        ticket.comment = Comment(body=comment, public=False)
        zenpy_client.tickets.update(ticket)
    except Exception as e:
        logger.exception("update_ticket {}".format(e))
        raise


def get_description(ticket_id):
    global zenpy_client
    try:
        zenpy_client = Zenpy(**credentials)
        ticket = zenpy_client.tickets(id=ticket_id)
        return ticket.description
    except Exception as e:
        logger.exception("get_description {}".format(e))
        raise
