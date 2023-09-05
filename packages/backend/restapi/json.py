from datetime import date, datetime

from flask import Blueprint, request

from repository.data import get_data

json_blueprint = Blueprint('data', 'data', url_prefix='/')

@json_blueprint.route('/', methods=['GET'])
def get_json_data():
    '''
    '''
    # Default from date
    from_date = datetime(2023, 1, 1, 0, 0, 0)
    if 'from' in request.args and not request.args['from'] == '':
        from_date_items = request.args['from'].split('-')
        from_date = datetime(int(from_date_items[0]), int(from_date_items[1]), int(from_date_items[2]), 0, 0, 0)

    # Default to date
    today = date.today()
    to_date = datetime(today.year, today.month, today.day, 0, 0, 0, 0)
    if 'to' in request.args and not request.args['to'] == '':
        to_date_items = request.args['to'].split('-')
        to_date = datetime(int(to_date_items[0]), int(to_date_items[1]), int(to_date_items[2]), 0, 0, 0)

    data = get_data(from_date, to_date)
    return data

'''
from repository.data import get_data

class GetData(Resource):
    def get(self):

        # Default from date
        from_date = datetime(2023, 1, 1, 0, 0, 0)
        if 'from' in request.args and not request.args['from'] == '':
            from_date_items = request.args['from'].split('-')
            from_date = datetime(int(from_date_items[0]), int(from_date_items[1]), int(from_date_items[2]), 0, 0, 0)

        # Default to date
        today = date.today()
        to_date = datetime(today.year, today.month, today.day, 0, 0, 0, 0)
        if 'to' in request.args and not request.args['to'] == '':
            to_date_items = request.args['to'].split('-')
            to_date = datetime(int(to_date_items[0]), int(to_date_items[1]), int(to_date_items[2]), 0, 0, 0)

        data = get_data(from_date, to_date)
        return data

'''
