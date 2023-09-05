import csv
from datetime import timedelta, datetime

dataSource = {}

def load_data(source_file):
    '''
    '''
    with open(source_file, 'r', newline='') as csvfile:
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
            difference = 0
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
                'difference': difference,
                'close': dataSource[hashedDate] + difference,
            }

            # Add the value
            data.append(value)

        from_date = from_date + timedelta(days=1)

    return data
