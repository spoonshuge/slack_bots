from slackclient import SlackClient
# Local modules
from src import settings

__purpose__ = """Main file from which the application will run."""

slack_client = SlackClient(settings.client_id)

