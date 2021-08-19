pkill gunicorn

echo "Output of pkill: $?"

source /etc/environment

dos2unix /home/ubuntu/backend/scripts/start_application.sh

chmod +x /home/ubuntu/backend/scripts/start_application.sh

/home/ubuntu/backend/scripts/start_application.sh
