import toml
from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from repository.data import load_data

from restapi.json import json_blueprint
from restapi.file import document_blueprint
from docs.docs import docs_blueprint

# Read the configuration
with open('.env.toml', 'r') as f:
    config = toml.load(f)

# Load the repository data
load_data(config['repository']['data_file'])

# Setup the RestAPI Server
app = Flask(config['restapi']['name'])
CORS(app)

# Register blueprints
app.register_blueprint(json_blueprint)
app.register_blueprint(document_blueprint)
app.register_blueprint(docs_blueprint)

api = Api(app)

# Development
if __name__ == '__main__':
    # Start the RestAPI server
    app.run(
        debug=True,
    )
