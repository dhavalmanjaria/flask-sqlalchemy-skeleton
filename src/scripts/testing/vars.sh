#!/bin/bash

export env_variables_file=/home/ubuntu/test/exirio-env-vars.sh  # Location of where the environment variables can be exported from
export venv_activate_path=/home/ubuntu/venv/bin/activate  # Location of activate script for python virtual environment
export exirio_backend_root=/home/ubuntu/backend  # Location of the exirio backend source code
export test_db=test  # Name of the test DB
export db_backup_file=/home/ubuntu/test/dump-main-latest  # Backup to restore from
export report_path=/home/ubuntu/test/reports # Folder to hold 
export test_db_url="postgresql://postgres:YRfxmRA4AgPMI7H3YAnE@exirio.cqxgzpfnoggg.eu-west-2.rds.amazonaws.com/$test_db"   # DBURI passed to SQLAlchemy


