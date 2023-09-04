# Backend (Full Stack Dev Admetricks)
This application implements a Rest API writed with **Python 3**.

The endopoints of this Rest API are:
* Get a json data filtered by from and to date, in the default path (/).
* Get a CSV file data filtered by from an to date in the document path (/document).

## Setup
First, install the dependencies with:
```sh
poetry install
```

### Work with the project

```sh
poetry run python restapi.py
```

## Data source
I got the historical data in [USD-Chilean Pesos historical data](https://mx.investing.com/currencies/usd-clp-historical-data) and stored in the file **data/source.csv**.