import toml
from flask import Flask

from repository.data import load_data

from restapi.json import json_blueprint
from restapi.file import document_blueprint

# Read the configuration
with open('.env.toml', 'r') as f:
    config = toml.load(f)

# Load the repository data
load_data(config['repository']['data_file'])

# Setup the RestAPI Server
app = Flask(config['restapi']['name'])

# 
app.register_blueprint(json_blueprint)
app.register_blueprint(document_blueprint)

if __name__ == '__main__':
    debug = True
    port = 5000

    # Configuration for the production environment
    if config['environment'] == 'production':
        debug = False
        port = config['restapi']['port']
    
    # Start the RestAPI server
    app.run(
        debug=debug,
        port=port,
    )
