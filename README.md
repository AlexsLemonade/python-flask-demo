# Python Flask Demo

This is a demo of the python Flask framework implementing an API for a portion of the data model for the Resources Portal project.

## Installation

Create and activate a virtualenv with:

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

Install the python dependencies with:

```bash
pip3 install -r requirements.txt
```

Run and configure the database (requires Docker):

```bash
./scripts/run_postgres.sh
./scripts/install_db_docker.sh
```

## Run the API Server

```bash
./scripts/serve.sh
```

## Run the Tests

```bash
./scripts/run_tests.sh
```
