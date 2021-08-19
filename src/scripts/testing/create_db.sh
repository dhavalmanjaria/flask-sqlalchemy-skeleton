#!/bin/bash

# First we create a dummy DB and import a test file
source /etc/environment
current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

source $current_dir/vars.sh

source $venv_activate_path

echo "DROPPING database $test_db. Enter 'y' to proceed..."

read approve

if [[ $approve != "y" ]]; then
	echo "Not dropping $test_db. Exiting..."
	exit 1
fi

sudo -u postgres psql -c "drop database $test_db"

echo "Creating new DB $test_db"
sudo -u postgres psql -c "create database ${test_db}"

echo "Restore data from $db_backup_file"

sudo -u postgres pg_restore -F tar -d ${test_db} $db_backup_file


