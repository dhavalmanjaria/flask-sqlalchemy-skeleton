#!/bin/bash

source /etc/environment
current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

source $current_dir/create_db.sh
source $current_dir/vars.sh

source $venv_activate_path

source $env_variables_file

pwd=$PWD

cd $exirio_backend_root

export DATABASE_URL=$test_db_url

echo $DATABASE_URL
