#!/bin/bash

# Run each individual test module (python file separately)

current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

source $current_dir/vars.sh

pytest_base_command="pytest --junit-xml=$report_path --tb=native --capture=tee-sys "

export DATABASE_URL=$test_db_url





