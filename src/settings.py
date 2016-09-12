import os
from configparser import ConfigParser

__purpose__ = """Grab variables from config files, making them available globally."""

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Setup ConfigParser to read in data from config file
_config = ConfigParser()
_config.read(os.path.join(__location__, 'config.conf'))
_auth = ConfigParser()
_auth.read(os.path.join(__location__, 'auth.conf'))

# Read in config info


# Read in auth info
client_id = _auth.get('CREDENTIALS', 'client_id')
client_secret = _auth.get('CREDENTIALS', 'client_secret')

