#!/bin/bash


current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

source $current_dir/prepare_pytest.sh

echo "Running pytest"

echo $*

pytest_base_command="pytest --junit-xml=$report_path --tb=native --capture=tee-sys "

if [[ ! -z "$1" ]]; then
	echo "Executing pytest custom commands"
	$pytest_base_command $*
else
	echo "Running all tests from $exirio_backend_root/tests with options and --junit-xml specified"
	$pytest_base_command $exirio_backend_root/tests
fi

# source $current_dir/drop_db.sh

