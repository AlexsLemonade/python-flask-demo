#!/bin/bash

export FLASK_RUN_PORT=5001
export FLASK_APP=resources_portal
export FLASK_ENV=development

flask run
