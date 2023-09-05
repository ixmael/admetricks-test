import csv

from datetime import date, datetime

from flask import Blueprint, request, send_file

from repository.data import get_data

document_blueprint = Blueprint('document', 'document', url_prefix='/document')

@document_blueprint.route('/', methods=['GET'])
def get_document_data():
    '''
    '''
    from_date = datetime(2023, 1, 1, 0, 0, 0)
    if 'from' in request.args and not request.args['from'] == '':
        from_date_items = request.args['from'].split('-')
        from_date = datetime(int(from_date_items[0]), int(from_date_items[1]), int(from_date_items[2]), 0, 0, 0)

    today = date.today()
    to_date = datetime(today.year, today.month, today.day, 0, 0, 0, 0)
    if 'to' in request.args and not request.args['to'] == '':
        to_date_items = request.args['to'].split('-')
        to_date = datetime(int(to_date_items[0]), int(to_date_items[1]), int(to_date_items[2]), 0, 0, 0)

    data = get_data(from_date, to_date)

    hashed_date_name = '{}'.format(int(round(datetime.today().timestamp())))
    from_name = '{}{}{}'.format(from_date.year, from_date.month + 1, from_date.day)
    to_name = '{}{}{}'.format(to_date.year, to_date.month + 1, to_date.day)
    file_generated = './tmp/{}_{}-{}.csv'.format(hashed_date_name, from_name, to_name)
    with open(file_generated, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['date', 'difference', 'close'])
        writer.writeheader()
        writer.writerows(data)

    return send_file(file_generated)
