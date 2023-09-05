from flask import send_file
from flask_swagger_ui import get_swaggerui_blueprint

# docs_blueprint = get_swaggerui_blueprint('docs', 'docs', url_prefix='/docs')
docs_blueprint = get_swaggerui_blueprint('/docs', 'restapi-swagger.json', config={})

@docs_blueprint.route('/restapi-swagger.json', methods=['GET'])
def get_docs():
    return send_file('./docs/openapi3_1.json')

