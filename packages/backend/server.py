import toml
from flask import Flask
from flask_cors import CORS

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
CORS(app)

#
app.register_blueprint(json_blueprint)
app.register_blueprint(document_blueprint)

# Development
if __name__ == '__main__':
    # Start the RestAPI server
    app.run(
        debug=True,
    )
