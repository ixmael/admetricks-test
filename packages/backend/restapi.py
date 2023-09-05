from datetime import date, timedelta, datetime
import csv

from flask import Flask, request, send_file
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

dataSource = {}

with open('./data/source.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        dateTuple = row['\ufeff"Fecha"'].split('.')
        rowDate = datetime(
            int(dateTuple[2]),
            int(dateTuple[1]),
            int(dateTuple[0]),
            0,
            0,
            0
        )

        key = '{}'.format(int(round(rowDate.timestamp())))
        dataSource[key] = float(row['Cierre'].replace(',', ''))

def get_data(from_date, to_date):
    '''
    '''
    data = []

    while from_date < to_date:
        # Prepare the date as a hash
        hashedDate = '{}'.format(int(round(from_date.timestamp())))

        # Search the hashed key
        if hashedDate in dataSource:
            difference = 0

            # Check if this has an element to compare
            if len(data) > 0:
                difference = dataSource[hashedDate] - data[:1][0]['close']

            # Prepare the value
            value = {
                'date': '{year}-{month:02d}-{day:02d}'.format(
                    year=from_date.year,
                    month=from_date.month,
                    day=from_date.day
                ),
                # The difference respect the previous value
                'close': dataSource[hashedDate] + difference,
            }

            # Add the value
            data.append(value)

        from_date = from_date + timedelta(days=1)

    return data

class GetData(Resource):
    '''
    '''
    def get(self):
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
        return data

class GetDataAsFile(Resource):
    '''
    '''
    def get(self):
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

api.add_resource(GetData, '/')
api.add_resource(GetDataAsFile, '/document')

if __name__ == '__main__':
    app.run(debug=True)
