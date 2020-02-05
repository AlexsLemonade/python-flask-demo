#!/bin/sh

# This script should always run as if it were being called from
# the directory above the one it lives in.
script_directory="$(perl -e 'use File::Basename;
 use Cwd "abs_path";
 print dirname(abs_path(@ARGV[0]));' -- "$0")"
cd "$script_directory" || exit
cd ..

export FLASK_APP=resources_portal
export FLASK_RUN_PORT=5001
export FLASK_ENV=development
export RESOURCES_PORTAL_CONFIG_FILE=environments/dev.cfg

flask run
