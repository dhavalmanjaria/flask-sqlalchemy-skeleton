#!/bin/bash

source /etc/environment
current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

source $current_dir/vars.sh

sudo -u postgres psql -c "drop database $test_db"

