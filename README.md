# Admetricks test
This is the *Full Stack Dev Admetricks* test implementation. In this project I developed the *model* of the *AdobeXD* file, a *graph* with **d3**, and a *RestAPI* to provide the data to the *graph* section.

## RestAPI
The *RestAPI* has the responsability to provide the data of the value of a **USD** (United States Dollar) in **CLP** (Chilean Pesos). You can read [the data's details](docs/DATA.md) to get the description of the data provided by the *RestAPI*.

This application was developed with *python 3.10* and manage the dependencies with *poetry*.

### Run in development mode
You have to go to the **packages/backend** path and execute the following commands:
```sh
# Install the dependencies
poetry install

# Execute the RestAPI server in development mode
poetry run python restapi.py
```
The previous commands initialize the *RestAPI* server listening in the port *5000*.

You can visit the endpoints:
* [The *json* data](http://localhost:5000/)
* [The *csv* file data](http://localhost:5000/document)
* [The *RestAPI* documentation](http://localhost:5000/docs)

You can import the *postman collection* to *postman* from the file called **admetricks.postman_collection.json** to interac with the *RestAPI*.

## Frontend
The frontend application is in **packages/frontend**. You can setup and run the project following the instructions described in the file **packages/frontend/README.md**.

### Setup
You have to define the environment variable *VITE_REST_API* in the file **packages/frontend/.env**. This is the base url to fetch the data for the graph.

If you are running the *RestAPI* in development mode, you can set the variable with the development *RestAPI* url:
```txt
VITE_REST_API=http://localhost:5000
```

### Run in development mode
You have to go to the **packages/frontend** path and execute the following commands:

```sh
# Install dependencies
yarn install
```

```sh
# Execute
yarn run dev
```
The previous commands initialize the *frontend* server listening in the port *5173*.

You have can visit the pages:
* [The model](http://localhost:5173/)
* [The graph](http://localhost:5173/dashboard)

## Deploy
I use [Terraform](https://www.terraform.io/) to describe the containers (docker) to provide the services.

You haven't to prepare the environment files for the projects because this has a default configuration for the containers.

After the containers ran, you have the following endpoints:
* [Model](http://localhost:3000)
* [Dashboard](http://localhost:3000/dashboard)
* [RestAPI](http://localhost:9000)
* [RestAPI Documentation](http://localhost:9000/docs)

You build, create and execute the containers (docker) to provide the services with the following commands:
```sh
# Initialize
terraform -chdir=./infrastructure/terraform init

# Prepare the configuration
terraform -chdir=./infrastructure/terraform plan

# Create and execute the docker items
terraform -chdir=./infrastructure/terraform apply

# (Optional) Destroy the docker items
terraform -chdir=./infrastructure/terraform destroy
```
