# Python Flask Demo

This is a demo of the python Flask framework implementing an API for a portion of the data model for the Resources Portal project.

## Installation

Create a virtualenv with:

```
virtualenv -p python3 venv
```

Install the python dependencies with:

```
pip3 install -r requirements.txt
```

Run and configure the database (requires Docker):

```
./scripts/run_postgres.sh
./scripts/install_db_docker.sh
```

## Run the API Server

```
./scripts/serve.sh
```

## Run the Tests

```
./scripts/run_tests.sh
```
