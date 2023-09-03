import random
from datetime import date, timedelta

from flask import Flask, request, send_file
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class GetData(Resource):
    def get(self):
        from_date = date(2023, 1, 1)
        if 'from' in request.args and not request.args['from'] == '':
            from_date_items = request.args['from'].split('-')
            from_date = date(int(from_date_items[0]), int(from_date_items[1]), int(from_date_items[2]))

        to_date = date.today()
        if 'to' in request.args and not request.args['to'] == '':
            to_date_items = request.args['to'].split('-')
            to_date = date(int(to_date_items[0]), int(to_date_items[1]), int(to_date_items[2]))

        data = []
        max_value = random.randint(21, 41)
        current_value = random.randint(7,max_value)
        value = {
            'date': '{year}-{month}-{day}'.format(year=from_date.year, month=from_date.month, day=from_date.day),
            'close': current_value,
            'difference': current_value,
        }
        data.append(value)

        from_date = from_date + timedelta(days=1)
        while from_date < to_date:
            current_value = random.randint(7,max_value)
            value = {
                'date': '{year}-{month}-{day}'.format(
                    year=from_date.year,
                    month=from_date.month,
                    day=from_date.day
                ),
                'close': current_value,
                'difference': current_value - data[:1][0]['close'],
            }
            data.append(value)

            from_date = from_date + timedelta(days=1)

        return data
    
class GetDataAsFile(Resource):
    def get(self):
        return send_file('./path/example.csv')

api.add_resource(GetData, '/')
api.add_resource(GetDataAsFile, '/document')

if __name__ == '__main__':
    app.run(debug=True)
