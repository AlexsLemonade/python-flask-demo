#!/bin/bash

export FLASK_APP=resources_portal
export FLASK_RUN_PORT=5001
export FLASK_ENV=development
export RESOURCES_PORTAL_CONFIG_FILE=environments/dev.cfg

flask run
