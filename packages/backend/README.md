# Backend (Full Stack Dev Admetricks)
This application implements a Rest API writed with **python 3.10** and **poetry** to manage the dependencies.

The endopoints of this are:
* [Get *JSON* data in localhost](http://localhost:5000): Get a json data filtered by from-to dates filter.
* [Get *CSV* data file in localhost](http://localhost:5000/document/): Get a CSV file data filtered by from-to dates filter.

## Setup
This project requires a config file called *.env.toml* placed in the current path. You have an example and the description of the configurations values in the *.env.toml.example* file.

Now, you have to install the dependencies with:
```sh
poetry install
```

### Run in development 
If you require to run the *RestAPI* in development mode execute:
```sh
poetry run python restapi.py
```
