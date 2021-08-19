#!/bin/bash

PGPASSWORD=YRfxmRA4AgPMI7H3YAnE

$backup_file=/home/ubuntu/test/dump-main-latest

# Restore a Test DB
sudo -u postgres pg_restore  --host exirio.cqxgzpfnoggg.eu-west-2.rds.amazonaws.com -d test < $backup_file


# Delete most currency history records since they would blow up the time required to run a test
sudo -u postgres psql \
	--host exirio.cqxgzpfnoggg.eu-west-2.rds.amazonaws.com \
	-d test \
	-c "delete from currency_history where source not in ('USD', 'EUR') and dest not in ('USD', 'EUR') and date >= '2010-01-01 00:00:00';"



