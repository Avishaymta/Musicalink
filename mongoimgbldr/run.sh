#!/bin/bash

eval "((mongod -config /etc/mongod.conf --bind_ip_all) &)"

while [ ! "$(ps aux | grep "mongod.conf" | grep -v grep)" ]
do
    printf "Waiting for MongoDB PID...\n"
    sleep 5
done

printf ":: MongoDB Started ::\n"

while [ ! -f /var/log/mongodb/mongod.log ]
do
    echo "Waiting for MongoDB log file..."
    sleep 5
done

echo "--- MongoDB proc started; Reading logs ---"
printf "Running on $(tput bold)$(netstat -tulpn | grep mongod | awk '{print $4}')\n"

tail -f /var/log/mongodb/mongod.log | jq .