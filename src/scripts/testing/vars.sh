#!/bin/bash

export env_variables_file=/home/dhaval/exirio/exirio-env-vars.sh  # Location of where the environment variables can be exported from
export venv_activate_path=/home/dhaval/exirio/venv-exirio/bin/activate  # Location of activate script for python virtual environment
export exirio_backend_root=/home/dhaval/exirio/backend  # Location of the exirio backend source code
export test_db=wealth_tracker_test  # Name of the test DB
export db_backup_file=/home/dhaval/exirio/exirio-postgres-backups/dump-plaid-latest  # Backup to restore from
export report_path=/home/dhaval/exirio/exirio-test-report.xml  # Name of the XML file where the JUnit report will be kept
export test_db_url="postgres://postgres:dhaval@localhost:5432/$test_db"  # DBURI passed to SQLAlchemy
