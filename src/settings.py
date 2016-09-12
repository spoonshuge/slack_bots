import os
from configparser import ConfigParser

__purpose__ = """Grab variables from config files, making them available globally."""

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Setup ConfigParser to read in data from config file
config = ConfigParser()
config.read(os.path.join(__location__, 'config.conf'))
auth = ConfigParser()
auth.read(os.path.join(__location__, 'auth.conf'))

# Read in config info


# Read in auth info
client_id = auth.get('CREDENTIALS', 'client_id')
client_secret = auth.get('CREDENTIALS', 'client_secret')

